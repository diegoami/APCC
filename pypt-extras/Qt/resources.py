# -*- encoding: utf-8 -*-
# Architrave Python Coding Challenge v0.1.0
# Project Structure for coding challenge
# Copyright © 2018, Richard Klemm.
# See /LICENSE for licensing information.
# This file was adapted from Chris Warrick’s Python Project Template.

"""
Adapt Qt resources to Python version.

:Copyright: © 2018, Richard Klemm.
:License: BSD (see /LICENSE).
"""

__all__ = ()

import sys

if sys.version_info[0] == 2:
    import APCC.ui.resources2  # NOQA
elif sys.version_info[0] == 3:
    import APCC.ui.resources3  # NOQA
else:
    print('FATAL: python version does not match `2` nor `3`')
    sys.exit(0)
