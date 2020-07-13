==============================
Noteworth Coding Challenge API
==============================

Scenario
========

One of the Noteworth healthcare provider partners doesn't want to manually
update clinicians in our platform. Instead, they have provided an API for
us to use to retrieve the latest list of providers and add them in our system.
Unfortunately, this API is not very stable and has a tendancy to drop 
connections. To complete this challenge, you will need to retrieve an auth
token to authenticate yourself with the api and use it to send a valid request
to retrieve the list of providers, then add these providers into your database.
 
Details
=======

Both the `/auth` and `/providers` API endpoints may fail. In order to pass this
challenge, your solution should **retry** a maximum of 2 times **for each** API 
before exiting gracefully. Potential misbehaviors include API timeouts and
incomplete response data, be on your guard!

Authentication
--------------

The API requires that you authenticate your requests by first asking for an
auth token and use it to generate a checksum that will be used to validate 
your subsequent request to retrieve the list of providers.

You can retrieve a token via a GET request to ``/auth``. This will return a
token for your request in the ``Super-Secure-Token`` header.

To retrieve the list of providers, you will need to calculate a checksum from
the provided auth token and assign the hexidecimal hash to the 
``X-Request-Checksum`` header for the API request. To calculate this checksum, 
you should compute: ``sha256(<auth_token><request path>)``

For example, if you had auth token ``12345`` and were requesting ``/providers``,
the checksum would be:

``sha256("12345/providers") = "bf6fa075e6d928d530fd4516e1671526ff1fe7f953209f0941553927bf16e9f8"``

Note: Calling ``/auth`` will always generate a new token. Take care of it!


Providers
---------
GET ``/providers`` will return a JSON blob of 10 providers. The JSON response
will contain a consistent fieldset though the data returned may change. You 
should use the JSON reponse to determine how to create your model(s). The 
challenge is complete when we can run your code and validate your app is 
consuming and storing data provided by this API.


Criteria
========

This challenge is intended to be completed in about 2 hours and can be taken
as a take-home assignement in which case we expect the quality level to be 
quite high, or can be provided as a pair-programming exercise lasting an hour
emphasizing implementation and thought process instead of feature-completeness.


Setup
=====

This application was developed using Poetry_ and python 3.8.3. To run the
application in a local dev environment, from the project root run
`$ poetry run flask run`

If everything is configured and running as expected, you should get a response
"Healthy" when hitting ``http://localhost:5000/health/``. More endpoints to come.

To evaluate tests:
``$ poetry run pytest``

Contributing
============

TBD

Credits
=======

This challenge is inspired by https://homework.adhoc.team/noclist/

.. _Poetry: https://python-poetry.org/