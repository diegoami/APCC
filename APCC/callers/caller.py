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


class Caller:

    def __init__(self, callees, job_generator):
        self._callees = callees
        self._job_generator = job_generator

    def run(self):
        for i in range(0, 1000):
            job_type = next(self._job_generator)
            callee = random.choice(self._callees[job_type])
            callee.process_job(i)
