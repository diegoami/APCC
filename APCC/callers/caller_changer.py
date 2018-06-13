# -*- encoding: utf-8 -*-
# Architrave Python Coding Challenge v0.1.0
# Project Structure for coding challenge
# Copyright © 2018, Richard Klemm.
# See /LICENSE for licensing information.

"""
Architrave Python Coding Challenge.

:Copyright: © 2018, Richard Klemm.
:License: BSD (see /LICENSE).
"""

import random
import time
from collections import defaultdict
from threading import Thread, Lock
class CallerChanger:

    def __init__(self, callees, job_generator):
        self._callees = callees
        self._job_generator = job_generator
        self.__job_distribution = defaultdict(int)
        self.threads = []
        self.lock = Lock()

    def execute_job(self,  job_type):
        if (self.__job_distribution.get(job_type, 0) > len(self._callees[job_type])):
            print("Job_type {} has {} callees and {} executions".format(job_type, self.__job_distribution.get(job_type, 0), len(self._callees[job_type])))
        while (self.__job_distribution.get(job_type, 0) > len(self._callees[job_type])):
            list_callees = sorted([(it_job_type, job_count, len(self._callees[it_job_type])) for it_job_type, job_count in self.__job_distribution.items()], key=lambda x : x[2] - x[1], reverse=True)
            for it_job_type, job_count, available_workers in list_callees:
                if (available_workers - job_count > 5):
                    print("Before: callees distribution : {}".format(list_callees))

                    job_to_move = it_job_type
                    print("Trying to pop from {}".format(job_to_move))
                    self.lock.acquire()
                    job_processor = self._callees[job_to_move].pop()
                    self.lock.release()
                    job_processor.switch_job_type(job_type)
                    self.lock.acquire()
                    self._callees[job_type].append(job_processor)
                    self.lock.release()
                    print("After : callees distribution : {}".format([(k, len(v), len(self._callees[k])) for k,v in self._callees.items()]))
                    break
                else:
                    break
            else:
                time.sleep(0.4)
        callee = random.choice(self._callees[job_type])
        self.lock.acquire()
        self.__job_distribution[job_type] = self.__job_distribution.get(job_type, 0) + 1
        self.lock.release()
        callee.process_job(job_type)
        self.lock.acquire()
        self.__job_distribution[job_type] = self.__job_distribution.get(job_type, 0) - 1
        self.lock.release()

    def run(self):
        for i in range(0, 1000):
            job_type = next(self._job_generator)
            print("Processing job_type : {}".format(job_type))
            thread = Thread(target=self.execute_job, args=(job_type,))
            self.threads.append(thread)
            thread.start()
        for thread in self.threads:
            thread.join()
