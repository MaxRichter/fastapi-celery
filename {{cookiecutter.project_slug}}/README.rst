===============
chatapp-backend
===============

To-Do
-----

1. Make tests run - ok
2, Understand alembic - ok
3. User Management - ok

    1. Create user by Email - ok
    2. Edit user (as admin) - ok
    3. Edit user (as same user) - ok
    4. Delete user (as admin) - ok

4. Integrate celery as task queue - ok
5. Cleanup project - ok
6. Make docker-compose.yml work - ok
7. Cleanup documentation - ok
8. Deploy on AWS/Localhost
9. Create basic UI in React Native
10. Couple Front and Backend
11. Make it a cookiecutter template

Further add-ons
_______________________
1. User Profile Management

    1. Profile picture
    2. Name
    3. Gender
    4. Phone
    5. Password
    6. Contact details

2. Geolocation features
3. Postings

    1. Images
    2. Videos

4. Apply:

    1. Effects
    2. Filter
    3. Smiley
    4. Emoticons

5. Search:

    1. Username
    2. Hashtag

6. Social Sharing

Setup
-----

1. Initialize docker-compose with

    .. code-block:: bash

        docker-compose up -d
        docker-compose down

2. You can reach pgadmin (postgres) under: `http://localhost:8000/`

    - Useful `link <https://gist.github.com/tingwei628/8584ddefc5d8e85f73566d5ab96bdc84>`_ for setup
    - Table create statement

    .. code-block:: bash

       -- Table: public.user

        -- DROP TABLE public."user";

        CREATE TABLE public."user"
        (
            id SERIAL PRIMARY KEY NOT NULL,
            email character varying(50) COLLATE pg_catalog."default" NOT NULL,
            first_name character varying(100) COLLATE pg_catalog."default",
            last_name character varying(100) COLLATE pg_catalog."default",
            address character varying(100) COLLATE pg_catalog."default",
            hashed_password character varying(100) COLLATE pg_catalog."default" NOT NULL,
            is_active boolean NOT NULL,
            is_superuser boolean NOT NULL
        )

        TABLESPACE pg_default;

        ALTER TABLE public."user"
            OWNER to postgres;

3. Create super-user by running: `python app/initial_data.py`

4. Generate secure key:

    .. code-block:: bash

        $ generate secret key
        openssl rand -hex 32

5. Locally run the backend:

    .. code-block:: bash

        (venv) max@einstein:~/PycharmProjects/chatapp-backend/backend$ python app/main.py

    You can now see it under: `http://localhost:8888/api/docs#`

Develop
-------

Change into your project directory and run:

    .. code-block:: bash

        chmod +x scripts/build.sh
        ./scripts/build.sh

This will build and run the docker containers, run the alembic migrations, and load the initial data (a test user).

It may take a while to build the first time it's run since it needs to fetch all the docker images.

Once you've built the images once, you can simply use regular docker-compose commands to manage your development environment, for example to start your containers:

    .. code-block:: bash

        docker-compose up -d

Once this finishes you can navigate to the port set during setup (default is localhost:8000):

    - The backend docs will be at http://localhost:8000/api/docs.

Development
-----------

The only dependencies for this project should be docker and docker-compose.

Quick Start
___________
Starting the project with hot-reloading enabled (the first time it will take a while):

    .. code-block:: bash

        docker-compose up -d

To run the alembic migrations (for the users table):

    .. code-block:: bash

        docker-compose run --rm backend alembic upgrade head

And navigate to http://localhost:{{cookiecutter.port}}

Note: If you see an Nginx error at first with a 502: Bad Gateway page, you may have to wait for webpack to build the development server (the nginx container builds much more quickly).

Auto-generated docs will be at http://localhost:{{cookiecutter.port}}/api/docs

Rebuilding containers:
______________________

    .. code-block:: bash

        docker-compose build

Restarting containers:
______________________

    .. code-block:: bash

        docker-compose restart

Bringing containers down:
_________________________

    .. code-block:: bash

        docker-compose down

Migrations
----------

Migrations are run using alembic. To run all migrations:

    .. code-block:: bash

        docker-compose run --rm backend alembic upgrade head

To create a new migration:

    .. code-block:: bash

        alembic revision -m "create users table"

And fill in upgrade and downgrade methods. For more information see `Alembic's official documentation <https://alembic.sqlalchemy.org/en/latest/tutorial.html#create-a-migration-script>`_.

Testing
--------

There is a helper script for both frontend and backend tests:

    .. code-block:: bash

        chmod +x scripts/test.sh
        ./scripts/test.sh

Backend Tests
_____________

    .. code-block:: bash

        docker-compose run backend pytest

any arguments to pytest can also be passed after this command

Logging
-------

    .. code-block:: bash

        docker-compose logs

Or for a specific service:

    .. code-block:: bash

        docker-compose logs -f name_of_service # frontend/backend/db

Project Layout
--------------

.. code-block:: bash

    backend
    └── app
        ├── alembic
        │   └── versions # where migrations are located
        ├── api
        │   └── api_v1
        │       └── endpoints
        ├── core    # config
        ├── db      # db models
        ├── tests   # pytest
        └── main.py # entrypoint to backend

    frontend
    └── public
    └── src
        ├── components
        │   └── Home.tsx
        ├── config
        │   └── index.tsx   # constants
        ├── __tests__
        │   └── test_home.tsx
        ├── index.tsx   # entrypoint
        └── App.tsx     # handles routing

Links
-----

- https://github.com/Buuntu/fastapi-react

Dependency Inversion Principle (DIP):
- Our classes should depend upon abstractions, not on concrete details.
- Example: Implementation of StockExchange

Single Responsibility Principle (SRP):
- A class or module should have one, and only one, reason to change
- This gives both a definition of responsibility and a guideline for class size.

Open-Closed Principle (OCP):
- Classes should be open for extension but closes for modification
- Sql class (example) is open to allow new functionality via subclassing, bet we can make this change while keeping every other class closed.

Classes should be small: We count responsibilities!
