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
from callees.variable_pool import VariablePool

from callers.caller import Caller
from callers.variable_caller import VariableCaller

from lib.job_types import JOB_TYPES
from lib.job_generator import balanced_job_generator, unbalanced_job_generator
import logging
import time

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)

"""10 workers assigned to different 10 types of jobs, which never switch to other jobs
on a balanced and on an un balanced source
"""

def main_vanilla():
    logging.info("Executing vanilla caller")
    callee_pools = dict()
    for job_type in JOB_TYPES:
        callee_pools[job_type] = CalleePool(job_type=job_type, pool_size=10)

    logging.info("Starting Caller 10/10 - balanced scenario")
    start_time = time.time()
    caller = Caller(callee_pools, balanced_job_generator())
    caller.run()
    elapsed_time= time.time() - start_time
    logging.info("Finished Caller 10/10 - balanced scenario. Elapsed time : {}".format(elapsed_time))

    logging.info("Starting Caller 10/10 - unbalanced scenario")
    start_time = time.time()
    caller = Caller(callee_pools, unbalanced_job_generator())
    caller.run()
    elapsed_time = time.time() - start_time
    logging.info("Finished Caller 10/10 - unbalanced scenario. Elapsed time : {}".format(elapsed_time))
    logging.info("Finished Executing vanilla caller")

"""10 workers assigned to different 10 types of jobs, which can switch to other jobs
on a balanced and on an un balanced source
"""

def main_variable():
    logging.info("Executing intelligent caller")
    logging.info("Starting LRUCaller  - balanced scenario")
    start_time = time.time()
    variable_pool = VariablePool(job_types=JOB_TYPES, pool_size=10)
    caller = VariableCaller(variable_pool, balanced_job_generator())
    caller.run()
    elapsed_time = time.time() - start_time
    logging.info("Finished LRUCaller - balanced scenario. Elapsed time : {}".format(elapsed_time))

    logging.info("Starting LRUCaller - unbalanced scenario")
    start_time = time.time()
    variable_pool = VariablePool(job_types=JOB_TYPES, pool_size=10)
    caller = VariableCaller(variable_pool, unbalanced_job_generator())
    caller.run()
    elapsed_time = time.time() - start_time
    logging.info("Finished LRUCaller  - unbalanced scenario. Elapsed time : {}".format(elapsed_time))
    logging.info("Finished Executing intelligent caller")

if __name__ == '__main__':
    logging.info("Hello, world!")
    logging.info("This is Architrave Python Coding Challenge.")
    logging.info("You should customize __main__.py to your liking (or delete it).")
    main_vanilla()
    main_variable()
