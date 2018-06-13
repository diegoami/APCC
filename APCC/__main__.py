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




from callees.callee_pool import CalleePool
from callees.callee import Callee
from callees.lru_pool import LRUPool

from callers.caller import Caller
from callers.lru_caller import LRUCaller

from lib.job_types import JOB_TYPES
from lib.job_generator import balanced_job_generator, unbalanced_job_generator
import logging
import time

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)


def exec_callee(job_type):
    callee = Callee(job_type)
    callee.process_job()

def main_vanilla():

    calle_pools = dict()
    for job_type in JOB_TYPES:
        calle_pools[job_type] = CalleePool(job_type=job_type, pool_size=10)

    logging.info("Starting Caller 10/10 - balanced scenario")
    start_time = time.time()
    caller = Caller(calle_pools, balanced_job_generator())
    caller.run()
    elapsed_time= time.time() - start_time
    logging.info("Finished Caller 10/10 - balanced scenario. Elapsed time : {}".format(elapsed_time))

    logging.info("Starting Caller 10/10 - unbalanced scenario")
    start_time = time.time()
    caller = Caller(calle_pools, unbalanced_job_generator())
    caller.run()
    elapsed_time = time.time() - start_time
    logging.info("Finished Caller 10/10 - unbalanced scenario. Elapsed time : {}".format(elapsed_time))


def main_lru():

    logging.info("Starting LRUCaller 10/10 - balanced scenario")
    start_time = time.time()
    lru_pool = LRUPool(job_types=JOB_TYPES, pool_size=10)
    caller = LRUCaller(lru_pool, balanced_job_generator())
    caller.run()
    elapsed_time = time.time() - start_time
    logging.info("Finished LRUCaller  10/10 - balanced scenario. Elapsed time : {}".format(elapsed_time))

    logging.info("Starting LRUCaller  10/10 - unbalanced scenario")
    lru_pool = LRUPool(job_types=JOB_TYPES, pool_size=10)
    caller = LRUCaller(lru_pool, unbalanced_job_generator())
    caller.run()
    elapsed_time = time.time() - start_time
    logging.info("Finished Caller 10/10 - unbalanced scenario. Elapsed time : {}".format(elapsed_time))


if __name__ == '__main__':
    logging.info("Hello, world!")
    logging.info("This is Architrave Python Coding Challenge.")
    logging.info("You should customize __main__.py to your liking (or delete it).")

    main_lru()
