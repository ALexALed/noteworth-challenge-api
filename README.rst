==============================
Noteworth Coding Challenge API
==============================

This challenge is derived from https://homework.adhoc.team/noclist/ and 
requires users to retrieve an authentication token and use it to retrieve data
from an API containing a list of users. And oh yeah, the API is really flakey!

What we are evaluating is:
1) Can a candidate think on their feet?
2) Can the candidate code defensively?
3) What does "quality" mean to a candidate?

This challenge is intended to be completed in about 2 hours and can be offered
as a take-home assignement in which case we expect the quality level to be 
quite high, or can be provided as a pair-programming exercise lasting an hour
but with an emphasis on implementation and thought process instead of feature-
completeness.

=====
Setup
=====

This application was developed using `Poetry`_ and python 3.8.3. To run the
application in a local dev environment, from the project root run
`$ poetry run flask run`

If everything is configured and running as expected, you should get a response
"Healthy" when hitting `http://localhost:5000/health/`. More endpoints to come.

To evaluate tests:
`$ poetry run pytest`

============
Contributing
============

TBD

.. _Poetry: https://python-poetry.org/