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

import time
import logging

class Callee():

    PROCESS_TIME = 2
    SWITCH_TIME = 5

    def __init__(self, job_type):
        self.job_type = job_type

    def process_job(self, job):
        logging.info('Start processing job {} of type {} on {}:'.format(job, self.job_type, id(self)))
        time.sleep(Callee.PROCESS_TIME)
        logging.info('Processed job: {} '.format(job))

    def switch_job_type(self, job_type):
        logging.info('Start switching job type: {} '.format(job_type))
        time.sleep(Callee.SWITCH_TIME)
        self.job_type = job_type
        logging.info('Start switching job type: {} '.format(job_type))

