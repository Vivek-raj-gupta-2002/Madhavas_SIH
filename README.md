# Project Setup Guide
This document provides instructions on how to set up and run the project.

## Prerequisites
1. Python 3.8 or later
2. virtualenv
3. Installation

### Create a virtual environment:
```
python -m venv env
```

### Activate the virtual environment:
```
source env/bin/activate
```

### Install the required dependencies:
``` 
pip install -r requirements.txt 
```

### Create a .env file in the project directory with the following configuration:
`.env`

```
DEBUG=True

SECRET_KEY='<Your Key>'

DATABASE='' # Database URL
DATABASE_USER='' # Database username
DATABASE_PASSWORD='' # Database password
DATABASE_HOST='' # Database host
DATABASE_PORT='' # Database port

```

### Run the following commands:
```
$ python manage.py migrate

$ python manage.py collectstatic

$ python manage.py createsuperuser

$ python manage.py runserver

```


### Additional Notes
1. Replace <Your Key> with a strong secret key.

2. Update the database configuration with your own database details.
3. The project is now running on http://localhost:8000.