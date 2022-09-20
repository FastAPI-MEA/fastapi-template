# FastAPI Template
A FastAPI template with Redis, Docker and PostgreSQL

## Introduction
This FastAPI template was created out of a need for consistent structure for projects with a setup that's easy to understand and use with as minimal additional setup as possible.

### What is hoped to be achieved
- Simplicity; no need for bloated classes and huge utils that you'll likely never use. Everything here should be very much needed in most projects
- Low barrier for entry; a template that is easy to start with and does not seem too advanced for beginners to use
- Production-ready; the above does not remove the important fact that this should be always production-ready without obvious faults
- Consistency; a smell for codebases is you not having a 'knowing' of where certain code is located. A wanted structure is one that's easy to navigate

### What is not hoped to be achieved
- Batteries-included; this template, whilst influenced by Django, does not aim to provide Django-like capabilities or to have a 'Django, but for FastAPI' setup
- Utility dump; this template will not be where all sorts of utilities are dumped because, 'why not?'.


## How to use
- Copy `.example.env` into a file, `.env`
- Run `docker-compose up --build` to build and run container. Yes, I expect you to use Docker in this day and age.

The above is enough to run your project except you need more than that if you are working on a real application. So, this:

### Personalizing the template
First, head to `app/settings` and edit `Settings.APP_NAME` to reflect the name of your application.

Next, you'll want to run `pipenv install` to ensure you get a Python environment you can attach to your IDE to allow for autocomplete and auto-imports so you don't have yellow and red lines everywhere

After this, we head to the .env to edit some of the values to your taste. Each value is explained in the [Config section](#config).

### Databases
Databases can be quite dicey and I'm happy to say Alembic is used to handle migrations and whatnots. This coupled with SQLAlchemy makes the world a better place. Whilst PostgreSQL is assumed to be the default database. You can of course edit things to your liking.

- Create migrations with `docker-compose run web alembic revision -m "Migration message here"`.
- Run migrations within Docker with `docker-compose run web alembic upgrade head`.


## Config
This section documents configuration options and the meaning of settings values and how to use them.

### Environmental Variables
The environmental variables in the [.example.env](./.example.env) file have specific purposes:
|Key | Description| Default
|---|---|---|
|ALLOWED_HOST|The domain you intend to run this application on|0.0.0.0|
|SECRET_KEY|A secret value used to hash and sign tokens and other security-related stuffs. | meandyouaretogether|
|DEBUG|A value that evaluates to a boolean to determine whether the app is run in debug mode or production.|True|
|PORT|Port the application will run on. If you change this from default, you will have to change the value in the [docker-compose.yml](./docker-compose.yml) file.|11000|
|POSTGRES_USER|This is the default user for the PostgreSQL database. On first run, Docker will use this value to initialize a postgres user so you'll want to set it before your first execution.|sasori|
|POSTGRES_PASSWORD|This is the default password for the PostgreSQL database. On first run, Docker will use this value to initialize a postgres database so you'll want to set it before your first execution.|sasori|
|POSTGRES_DB|This is the default PostgreSQL database created. On first run, Docker will use this value to initialize a postgres database so you'll want to set it before your first execution|akatsuki|
|POSTGRES_TEST_DB|This is the database created for test cases. It is flushed after every test case is run.| hebi
|POSTGRES_PORT|The port Postgres will run on. Don't change it except you know what you're doing, and if you do, change the value in the [docker-compose.yml](./docker-compose.yml) file.|5432|
|POSTGRES_HOST|The host set in the docker container where the PostgreSQL instance will be running. Don't change it except you know what you're doing, and if you do, change the value in the [docker-compose.yml](./docker-compose.yml) file.|postgres|
|REDIS_HOST|The host set in the docker container where the Redis instance will be running. Don't change it except you know what you're doing, and if you do, change the value in the [docker-compose.yml](./docker-compose.yml) file.|redis|
|REDIS_PORT|The port the application will use to connect to Redis. Don't change it except you know what you're doing, and if you do, change the value in the [docker-compose.yml](./docker-compose.yml) file.|6379|

### Application Settings
Application settings are set in the `app.settings.Settings` class and are used to store app wide configurations. Values are so:

|key|Description|Default|
|---|---|---|
|APP_TITLE|Name of the application, will show in the documentation|App Name|
|ALLOWED_HOST|The domain you intend to run this application on|Derived from `.env` with key `ALLOWED_HOST`|
|SECRET_KEY|A secret value used to hash and sign tokens and other security-related stuffs.|Derived from `.env` with key `SECRET_KEY`|
|DEBUG|A value that evaluates to a boolean to determine whether the app is run in debug mode or production.|Derived from `.env` with key `DEBUG`|
|ALLOWED_PORT|Port the application will run on. If you change this from default, you will have to change the value in the [docker-compose.yml](./docker-compose.yml) file.|Derived from `.env` with key `PORT`|
|DB_USER|This is the default user for the PostgreSQL database. On first run, Docker will use this value to initialize a postgres user so you'll want to set it before your first execution.|Derived from `.env` with key `POSTGRES_USER`|
|DB_PASSWORD|This is the default password for the PostgreSQL database. On first run, Docker will use this value to initialize a postgres database so you'll want to set it before your first execution.|Derived from `.env` with key `POSTGRES_PASSWORD`|
|DB_DB|This is the default PostgreSQL database created. On first run, Docker will use this value to initialize a postgres database so you'll want to set it before your first execution|Derived from `.env` with key `POSTGRES_DB`|
|DB_PORT|The port Postgres will run on. Don't change it except you know what you're doing, and if you do, change the value in the [docker-compose.yml](./docker-compose.yml) file.|Derived from `.env` with key `POSTGRES_PORT`|
|DB_HOST|The host set in the docker container where the PostgreSQL instance will be running. Don't change it except you know what you're doing, and if you do, change the value in the [docker-compose.yml](./docker-compose.yml) file.|Derived from `.env` with key `POSTGRES_HOST`|
|DB_URL|URL leading to the application database|`postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DB}`|
|TEST_DB|This is the database created for test cases. It is flushed after every test case is run.|Derived from `.env` with key `POSTGRES_TEST_DB`
|TEST_DB_URL|URL leading to test database|`postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{TEST_DB}`|
|ACCESS_TOKEN_EXPIRY_TIME|Duration in seconds before access token expires| 60 * 30 (seconds)|
|REFRESH_TOKEN_EXPIRY_TIME|Duration in seconds before refresh token expires| 60 * 30 (seconds)|
|PASSWORD_HASHER|Hashing algorithm for passwords|`CryptContext(schemes=["bcrypt"], deprecated="auto")`|
|JWT_ALGORITHM|Algorithm used to generate JWT token|HS256|
|REDIS_HOST|The host set in the docker container where the Redis instance will be running. Don't change it except you know what you're doing, and if you do, change the value in the [docker-compose.yml](./docker-compose.yml) file.|Derived from `.env` with key `REDIS_HOST`|
|REDIS_PORT|The port the application will use to connect to Redis. Don't change it except you know what you're doing, and if you do, change the value in the [docker-compose.yml](./docker-compose.yml) file.|Derived from `.env` with key `REDIS_HOST`|
|PAGE_SIZE|[Not Implemented] default size of page for paginated items|50

## I don't want some things
There is the possibility that you may not want some features such as Redis. You can easily remove what you don't need and proceed as planned.
