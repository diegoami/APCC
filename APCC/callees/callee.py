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


class Callee():

    PROCESS_TIME = 2
    SWITCH_TIME = 5

    def __init__(self, job_type):
        self.__job_type = job_type

    def process_job(self, job):
        print('Start processing job {} on {}:'.format(job, id(self)))
        time.sleep(Callee.PROCESS_TIME)
        print('Processed job: ', job)

    def switch_job_type(self, job_type):
        print('Start switching job type: ', job_type)
        time.sleep(Callee.SWITCH_TIME)
        print('Switched to job_type: ', job_type)
