==============================
Noteworth Coding Challenge API
==============================

Solution Architecture
=====================
Data will be loaded automatically after application starts.
For this purpose used Celery (https://docs.celeryproject.org/en/stable/) and RabbitMQ (https://www.rabbitmq.com/) as a broker

You can check `http://localhost:8080/employees` for employees (This endpoint added for development purposes)

On backend used Django (base setup, ORM and routing) and Django Rest Framework (for serialization and representation)


Description of the problem and solution.
========================================
The most challenging part of this task is the instability of API.
I decided to use `request` library with a Retry adapter.
I didn't fount any restriction about timeout issues, so I leave the default timeout value.

For project I used `docker-compose` because of:

1. It's easy to setup composed application
2. It's highly available and configurable on every platform
3. It's close to production setup 

I move existing flask api into `noteworth_challenge_api` folder and add Dockerfile

Logging system implemented on default python logging, 
but I think for future development and production usage 
I will be use combination of `structlog` (https://www.structlog.org/en/stable/) + `Sentry` (https://sentry.io/welcome/)
or something similar

Instruction to setup and run application
=========================================

The setup process is pretty simple:

`docker-compose build` - for build application

`docker-compose up` - for run application

`sh tests.sh` - for run tests


Trade-offs
==========

1. Apllication runs in development mode (`DEBUG=True`), it is not ready for production
2. Docker and docker-compose setup is not finished (need to add volumes and env vars)
3. Need to add envs for secrets, ports and hosts 
4. Need to add reverse proxy server and python application server
5. Need to add pre-commit hooks and CI/CD integration (github actions maybe)
