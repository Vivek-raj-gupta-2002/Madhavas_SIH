# Project Setup Guide
This documentation provides instructions on how to set up and run the project.

## Create a Virtual Environment with its file name .env.

### Create an API of data with the help of "AISHE" and "UDISE"
1. [Aishe link](https://aishe.gov.in/aishe/instituteDirectoryIndex?hasReportLink=index)

2. [Udise link](https://src.udiseplus.gov.in/)

### The following steps should be followed in a sequenced manner
1. Set up an environment file using Dockerfile and Docker-Compose file.
   Command: 
   ```
   docker-compose build
   ```
2. Make a migrations.
   Command:
   ```
   docker-compose run web python3 project/manage.py makemigrations
   ```
3. With the help of Migration, we create a Database.
   Command: 
   ```
   docker-compose run web python3 project/manage.py migrate
   ```
4. Collectstatic.
   Command:
   ```
   docker-compose run web python3 project/manage.py collect static
   ```
5. Create a superuser.
   Command: 
   ```
   docker-compose run web python3 project/manage.py createsuperuser
   ```
6. Run the server on Django Developer.
   Command: 
   ```
   docker-compose run web python3 project/manage.py run server
   ```

### Additional notes
The project is now running on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
