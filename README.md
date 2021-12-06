#  File upload API

The goal of this project is to implement a web application that 
provides an API with the following functionality:
- the API should be protected by authorisation with a token 
or username/password pair
- upload and process an excel file
- retrieve the date and time the file was uploaded
- retrieve the processing status (uploaded, processing, finished)
- retrieve the processing result
- retrieve the date and time of the end of processing, 
if the processing is completed


The following technologies are used to implement the service:
- Python 3.9.7
- Django 3.2.9
- djangorestframework 3.12.4
- djangorestframework_simplejwt 5.0.0
- openpyxl 3.0.9
- xlrd 2.0.1
- Celery 5.2.1
- Redis 3.5.3
- drf-yasg 1.20.0
- Docker 4.2.0


### Usage

#### Using docker-compose

- $ git clone https://github.com/JackCX777/file_upload_api
- $ docker-compose -f docker-compose-dev.yml up --build -d
- Please wait about few minutes
- The API endpoints and documentation are available on http://0.0.0.0:8000/swagger/


#### Note: 

For unauthorised users, only the registration subpoint is available.

To obtain a token, you need to first register with a custom username and password. 
You can also use the built-in superuser account with:

username: admin

password: testpass

This API uses a Bearer JSON Web Token. Access token valid for 30 minutes, 
refresh token valid for 1 day.

To auth by token please find the Authorize button in the top right corner,
fill in the Value field using the following format:

Bearer your_new_access_token

Then click Authorize.

The file uploading endpoint accepts only *.xls or *.xlsx files.

A 30 seconds delay is used to emulate long file processing operations.