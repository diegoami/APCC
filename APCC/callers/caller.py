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
class Caller:

    def __init__(self, callees, job_generator):
        self._callees = callees
        self._job_generator = job_generator
        self.__job_distribution = defaultdict(int)
        self.threads = []



    def execute_job(self,  job_type):
        while (self.__job_distribution.get(job_type, 0) >= 10):
#            print('Waiting for available worker... type : {} , {} executing '.format(job_type, self.__job_distribution.get(job_type)))
            time.sleep(0.5)

        self.lock.acquire()
        print('Ok to execute worker... type : {} , executing : {} '.format(job_type,
                                                                           self.__job_distribution.get(job_type)))

        self.__job_distribution[job_type] = self.__job_distribution.get(job_type, 0) + 1
        callee = random.choice(self._callees[job_type])
       # self.lock.release()

        callee.process_job(job_type)
       # self.lock.acquire()
        self.__job_distribution[job_type] = self.__job_distribution.get(job_type, 0) - 1
        print('Distribution after calling : {}'.format(self.__job_distribution))
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
