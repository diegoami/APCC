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
import logging

class Caller:

    def __init__(self, callee_pools, job_generator):
        self._callee_pools = callee_pools
        self._job_generator = job_generator

    def run(self):
        all_threads = []
        for i in range(0, 1000):
            job_type = next(self._job_generator)
            callee_pool = self._callee_pools[job_type]
            thread = callee_pool.exec_job(i)
            all_threads.append(thread)
        logging.info("Finished caller, waiting for threads to finish")
        for thread in all_threads:
            thread.join()