# Project Setup Guide
This document provides instructions on how to set up and run the project.

## Prerequisites
1. Python 3.8 or later
2. virtualenv
3. Installation

### Create a virtual environment:
at location `./backend`

```
python -m venv env
```

### Activate the virtual environment:
at location `./backend`
```
source env/bin/activate
```

### Install the required dependencies:
at location `./backend`
``` 
pip install -r requriments.txt 
```

### Create a .env file in the project directory with the following configuration:
at location `./backend/project`
`.env`

```
# Django setup
DEBUG=True/False
SECRET_KEY='<Your Key>'

# database setup
DATABASE='' # Database URL
DATABASE_USER='' # Database username
DATABASE_PASSWORD='' # Database password
DATABASE_HOST='' # Database host
DATABASE_PORT='' # Database port

# Email Setup
EMAIL_USER='bharitigupta123@gmail.com'
EMAIL_PASSWORD='rvod gshs royb xunn'

```
at location `./backend/project`

### Run the following commands:
```
$ python manage.py migrate

$ python manage.py collectstatic

$ python manage.py createsuperuser

$ python manage.py runserver

```


### Additional Notes
1. Replace <Your Key> with a strong secret key.
2. You cannot use direct password in `EMAIL_PASSWORD` in case of gmail use: [APP Password guide](https://support.google.com/accounts/answer/185833?visit_id=638378288407547944-1516551644&p=InvalidSecondFactor&rd=1
).
3. Update the database configuration with your own database details.
4. The project is now running on http://localhost:8000.
