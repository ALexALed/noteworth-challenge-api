==============================
Noteworth Coding Challenge API
==============================

Scenario
========

One of the Noteworth healthcare provider partners doesn't want to manually
update clinicians in our platform. Instead, they have provided an API for
us to use to peridically reach out and add them in our system ourselves.
Unfortunately this API is not very stable and has a tendancy to misbehave
with dropping connections, periodic unexplained errors, and other issues. 

For this challenge you will need to make two calls to the API, one to get an 
auth token and another to retrieve the list of providers.

Criteria
========


All submissions MUST contain a README.

Write your README as if it was for a production service with a team of 
collaborators. Include the following items:

- Description of the problem and solution.
- Instruction to setup and run application, tests, etc.
- Trade-offs you might have made, anything you left out, or what you might do differently if you were to spend additional time on the project.

The submission must be written in Python/Django.
The submission must make calls to both APIs and save the results in a database.


This challenge is intended to be completed in about 2 hours. If you find you
have spent significantly more time on this project, please stop and get in
contact and we will discuss options for next steps. 

Lastly, we value **quality over feature-completeness**. It is fine to leave
things aside provided you call them out in your project's README. The goal of
this code sample is to help us identify what you consider production-ready code.
You should consider this code ready for final review with your colleague, i.e.
this would be the last step before deploying to production.

 
Details
=======

Both the ``/auth`` and ``/providers`` API endpoints may fail. In order to pass this
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


Assessment
==========

The aspects of your code we will assess include:

- **Architecture**: Fault-tolerance, backward compatibility, extensibility, reliability, maintainability, availability, security, usability, and other such –ilities
- **Clarity**: Does the README clearly and concisely explain both the problem and solution? Are technical tradeoffs explained? Does it accurately reflect the state of the application?
- **Correctness**: Does the application do what was asked? If there is anything missing, does the README explain why it is missing?
- **Code quality**: Is the code simple, easy to understand, and maintainable? Are there any code smells or other red flags? Does object-oriented code follows principles such as the single responsibility principle? Is the coding style consistent with the language's guidelines? Is it internally consistent throughout the codebase?
- **Security**: Are there any obvious vulnerabilities?
- **Testing**: How thorough is the test suite? Is it flexible to update with code changes? Are there some unit and some integration tests? 100% code coverage is not expected, we're looking at the approach.
- **UX:** Is the web interface understandable and pleasing to use? Is the API intuitive?
- **Technical choices**: Do the choices of libraries, databases, architecture etc. seem appropriate for the implementation?

Bonus points (these items are optional):

    
- **Scalability**: Will technical choices scale well? If not, is there a discussion of those choices in the README?
- **Production-readiness**: Does the code include error handling, logging, debugging/secrets, etc?

Get Started
===========

This application was developed using Poetry_ and python 3.8. 
You can intialize the VM with ``$ poetry install`` and then
the API from the project root with ``$ poetry run flask run``

If everything is configured and running as expected, you should get a response
welcoming you to the challenge at ``http://localhost:5000/``


Good luck! If you have any questions along the way, please don't hesitate to ask!

.. _Poetry: https://python-poetry.org/docs/