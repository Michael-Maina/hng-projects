# Simple REST API
## Description
A simple REST API that demonstrates how to implement basic CRUD operations for a person.

Built using:
  - Python Flask web framework
  - MySQL database
  - SQLAlchemy ORM
## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)

## Installation
You'll need to have `Python v3.8.x` or higher and `MySQL v5.7.x` or higher to run the application.

Clone this repository.

For the Python libraries used in this application, run:
```bash
pip install -r requirements.txt
```

## Configuration
You will need to create a `.env` file that will contain the following environment variables of your own choosing:
```
API_PORT
API_HOST
DB_HOST
DB_USERNAME
DB_PWD
DB_DATABASE
```
These are loaded automatically by the `python-dotenv` library into the application.

For setting up your database, echo the contents of [db_setup.sql](https://github.com/Michael-Maina/hng-projects/blob/master/stage_2/db_setup.sql) file to the MySQL CLI:

**Open the file and edit username and password first**

```bash
echo db_setup.sql | mysql -u <username> -p <user_password>
```
## Usage
To start the api and attach it to a port, run the following command in your terminal:

```bash
gunicorn --bind 0.0.0.0:5000 api:app
```



## API Documentation
For all information on how to use the API, refer to the [DOCUMENTATION.md](https://github.com/Michael-Maina/hng-projects/blob/master/stage_2/DOCUMENTATION.md) file.