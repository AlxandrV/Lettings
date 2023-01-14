# Lettings

Orange County Lettings web app

## Summary

- [Local development](#local-development)
- [Local development from Docker](#local-development-from-docker)
- [Deploy](#deploy)
    - [CircleCI](#circleci)
    - [Heroku](#heroku)
    - [Sentry](#sentry)

## Local development 

### Prerequisites

- A CircleCI and Heroku account
- Git CLI
- SQLite3 CLI
- A Python runtime environment, version 3.6 or higher

In the rest of the local development documentation, it is assumed that the `python` command in your shell OS runs the above Python interpreter (unless a virtual environment is enabled).

### macOS / Linux

#### Clone the repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/AlxandrV/Lettings.git`

#### Create the virtual environment

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (If the previous step has errors with a package not found on Ubuntu)
- Activate the environment `source venv/bin/activate`
- Confirm that the `python` command runs the Python interpreter in the virtual environment
`which python`
- Confirm that the version of the Python interpreter is 3.6 or higher `python --version`
- Confirm that the `pip` command runs the pip executable in the virtual environment, `which pip`
- To disable the environment, `deactivate`

#### Run the site

- `cd /path/to/app`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Go to `http://localhost:8000` in a browser.
- Confirm that the site is working and that it is possible to navigate (you should see several profiles and locations).

#### Linting

- `cd /path/to/app`
- `source venv/bin/activate`
- `flake8`

#### Units tests

- `cd /path/to/app`
- `source venv/bin/activate`
- `pytest --no-migrations`

#### Database

- `cd /path/to/app`
- Open a `sqlite3` shell session
- Connect to the database `.open oc-lettings-site.sqlite3`
- Display the tables in the database `.tables`
- Show columns in the profile table, `pragma table_info(profiles_profile);`
- Run a query on the profile table, `select user_id, favorite_city from profiles_profile where favorite_city like 'B%';`
- `.quit` to leave

#### Panel d'administration

- Go to `http://localhost:8000/admin`
- Login with user `admin`, password `Abc1234!`

### Windows

Using PowerShell, as above except :

- To activate the virtual environment, `.\venv\Scripts\Activate.ps1` 
- Replace `which <my-command>` with `(Get-Command <my-command>).Path`

## Local development from Docker

Install [Docker](https://www.docker.com/get-started/) on your desk

### Build from the Dokerfile or Docker compose

With Dockerfile :

- Build the image `docker build -t <my-image-name> .`
- Run `docker run -p 8000:8000 -it <my-image-name>`

The application will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

With Docker Compose :

If you are install [Docker Compose](https://docs.docker.com/compose/install/)

- Run `docker-compose up`

The application will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Build from my DokerHub

Public access to my depot [alxandrv/lettings](https://hub.docker.com/r/alxandrv/lettings)

Run the latest version 

- Run `docker run -p 8000:8000 -it alxandrv/lettings`

The application will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Deploy

### CircleCI

Pipelines [Lettings](https://app.circleci.com/pipelines/github/AlxandrV/Lettings) on CircleCI

Steps :

- Create a project CirleCI
- Set the environment variables :

| key | Value |
|-----|-------|
| DOCKER_LOGIN | `Your login Docker Hub` |
| DOCKER_PASSWORD | `Your password Docker hub` |
| HEROKU_API_KEY | `Your secret API key Heroku` |
| HEROKU_APP_NAME | `Name of your Heroku project` |

### Heroku

Project [Lettings](https://letting.herokuapp.com/) deployed on Heroku

| key | Value |
|-----|-------|
| DEBUG_COLLECTSTATIC | 1 |
| SECRET_KEY | `Your secret key Django` |
| SENTRY_DSN | `Your sentry DSN` |

By default Heroku create in your app an Add-ons `DATABASE` remove that

### Sentry

Create Sentry account to access the project [Lettings](https://sentry.io/organizations/openclassrooms-0q/projects/lettings/)