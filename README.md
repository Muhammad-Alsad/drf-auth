# Lab-33

## project: Authentication & Production Server

## Author: Muhammad AL-Sad

### How to initialize/run your application:
    - python manage.py runserver




### URL:  http://127.0.0.1:8000/api/v1/movies/

   - bearer:

    ```
        {
            "username": "muhammad",
            "password": "1234",
            "owner": 1
        }

    ```



### URL :   http://127.0.0.1:8000/api/token/refresh/   
      -  inside body 
        body:
        '''

        {
            {
                "refresh:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkwODMyNjc1LCJpYXQiOjE2OTA4MzIzNzUsImp0aSI6IjE0Y2YzMmNjZTg2MDQzZTNhZjhhN2I4ZWZmNWMwMjQ1IiwidXNlcl9pZCI6MX0.ddodmBVzCZVwpWPh5WEyFZIKbBbgdGy5lnLWGWuQhnc "
            }
        }
        '''