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

class LRUCaller:

    def __init__(self, lru_pool, job_generator):
        self._lru_pool = lru_pool
        self._job_generator = job_generator

    def run(self):
        all_threads = []
        for i in range(0, 1000):
            job_type = next(self._job_generator)
            thread = self._lru_pool.exec_job(job=i, job_type=job_type)
            all_threads.append(thread)
        logging.info("Finished caller, waiting for threads to finish")
        for thread in all_threads:
            thread.join()