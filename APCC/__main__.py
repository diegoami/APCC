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
import time


def main():
    """Main routine of Architrave Python Coding Challenge."""
    print("Hello, world!")
    print("This is Architrave Python Coding Challenge.")
    print("You should customize __main__.py to your liking (or delete it).")

    print("Create Callers")
    callees = defaultdict(list)
    start = time.time()


    for job_type in JOB_TYPES:
        for i in range(0, 10):
            callees[job_type].append(Callee(job_type))

#    caller = CallerChanger(callees, job_generator())
    caller = Caller(callees, job_generator())

    caller.run()

    end = time.time()
    elapsed = end - start

    print("Elapsed time : {}".format(elapsed) )
if __name__ == '__main__':
    main()
