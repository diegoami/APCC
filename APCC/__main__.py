# -*- encoding: utf-8 -*-
# Architrave Python Coding Challenge v0.1.0
# Project Structure for coding challenge
# Copyright © 2018, Richard Klemm.
# See /LICENSE for licensing information.

"""
Main routine of Architrave Python Coding Challenge.

:Copyright: © 2018, Richard Klemm.
:License: BSD (see /LICENSE).
"""

__all__ = ('main',)

from collections import defaultdict

from callers.caller import Caller
from callers.caller_changer import CallerChanger
from callees.callee import Callee
from lib.job_generator import job_generator
from lib.job_types import JOB_TYPES
from threading import BoundedSemaphore, Thread

import time




def main():
    """Main routine of Architrave Python Coding Challenge."""
    print("Hello, world!")
    print("This is Architrave Python Coding Challenge.")
    print("You should customize __main__.py to your liking (or delete it).")

    print("Create Callers")
    callees = defaultdict(list)
    start = time.time()
    semaphores = {}
    threads = []
    sem_count = defaultdict(int)
    for job_type in JOB_TYPES:
        semaphores[job_type] = BoundedSemaphore(10)
        for i in range(0, 10):
            callees[job_type].append(Callee(job_type))
    job_generator_o = job_generator()
    for i in range(0, 1000):
        job_type = next(job_generator_o)
        print("Processing job_type : {}".format(job_type))
        semaphores[job_type].acquire()
        sem_count[job_type] += 1
        cjob_type = callees[job_type]
        csem = cjob_type[ sem_count[job_type]]
        thread = Thread(target=csem.process_job, args = (job_type,))
        thread.start()
        threads.append(thread)
        sem_count[job_type] -= 1
        semaphores[job_type].release()
    for thread in threads:
        thread.join()

    end = time.time()
    elapsed = end - start

    print("Elapsed time : {}".format(elapsed) )
if __name__ == '__main__':
    main()
