===================================
Architrave Python Coding Challenge.
===================================
:Info: This is the README file for Architrave Python Coding Challenge.
:Author: Richard Klemm <klemm@architrave.de>
:Copyright: © 2018, Richard Klemm.
:Date: 2018-01-08
:Version: 0.1.0

.. index: README

PURPOSE
-------
Image the following scenario:

You've one master machine and 100 workers.
There are 10 different kinds of jobs that need to be processed.
Each worker is capable of processing each kind of job.
Switching between jobs kinds takes 5 Minutes for a worker (during which he can't process any job)
The number of pending jobs is dynamic and incoming order isn't strict.
The average processing time of a job is on average 2 Minutes.


INSTALLATION
------------
It's easiest to install this module as development package:
`pip install -r requirements.txt
`pip install -e .`
That way, it will automatically update to changes in the code

USAGE
-----
`cd` into the APCC directory and exceute
`python __main__.py`

update documentation:
`sphinx-build -b html docs docs/html`

NOTES
-----
The __main__.py implements the task in a very very basic (and broken)
way. Mainly, it serves to define a common vocabulary and show
the idea of the task.


QUESTIONS / TASKS
---------

Questions:

1. How is the current implementation broken? When does it make sense to deviate from the
   specs that far?
2. Describe a possible solution that would optimally use available resources.
   We figured it would take too long to actually implement but are interested in the
   solutions you come up with

Tasks:

1. Make the workers run in parallel.


ANSWER
------------------

1. In the current implementation the workers do not run in parallel and there is no guarantee that a maximum of 10
workers run at any time for a job type.
Not sure what the constraints would actually be, but rather then creating workers with a fixed job type,
I would create them only when I know the jobtype at runtime. If this is not possible or too expensive, I would allocate
the workers accordingly to the expected distribution of job_types.

2. If the distribution of job types is not known, the system could slowly reallocate workers to job_types that appear more
frequently. I tried implementing a solution "variable_pool" which does just that.

Task: Now the workers run in parallel