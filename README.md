## django-assess

Assessment on Django

## Description

The **django-asess** is a simple application that uses an API endpoint that accepts a string of comma separated points for example “(2,3), (1,1), (5, 4), ... and calculates the closest points. It then stores them in a table in the database.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://www.getpostman.com/collections/0ffc8f406491236c06cb)


## Development set up


-   Check that python 3.8.x is installed:

    ```
    python --version
    >> Python 3.8.x
    ```

-   Install pipenv:

    ```
    pip3 install pipenv
    ```

-   Check pipenv is installed:
    ```
    pipenv --version
    >> pipenv, version 2018.11.26
    ```
-   Check that postgres is installed:

    ```
    postgres --version
    >> postgres (PostgreSQL) 10.1
    ```
-  Database
    * Switch to postgres account (in terminal)
        ```
        sudo su - postgres
        ```
    * Run PostgreSQL command line client.
        ```
        psql
        ```
    * Create a database user with a password.
        ```
        CREATE USER django_assess_owner with password 'password12345';
        ```
    * Create a database instance.
        ```
        CREATE DATABASE djando_assess owner django_assess_owner encoding 'utf-8';
        ```  

- Clone the django-assessment repo and cd into it
    ```
    git clone https://github.com/EKibet/django-assessment
    ```
- Create  virtual environment
    ```
    pipenv --python 3.8

    ```
- Turn off a virtual environment  
    ```
    exit
    ```

- Spawn a shell in a virtual environment
    ```
    pipenv shell
    ```
- Install dependencies
    ```
   pipenv sync 
    ```
- Create Application environment variables and save them in .env file 
    ```
    DJANGO_READ_DOT_ENV_FILE=True
    DJANGO_DEBUG=True
    DATABASE_URL='postgresql://localhost/django_assess?user=django_assess_owner&password=password12345'
    SECRET_KEY='super_secret'
    ```

- Add the variables in the .env file to path
    ```
    source .env
    ```
- Running migrations

    - Initial migration commands
        ```
        make migrations
        
        make migrate
        ```



- Run application.
    ```
    make serve
    ```

- Running tests and generating report

    On command line run:

    ```
    pytest
    ```

    To further view the lines not tested or covered if there is any,

    A `htmlcov` directory will be created, get the `index.html` file by entering the directory and view it in your browser.
### Available endpoints
``` 
    */api/get-pairs*   [Post method]  
    Input parameters: 
        
        media type= application/json  
        {  
            "points_submitted": "(2,3), (1,1), (5, 4)",  
            "relative_point": "(2,3)"  
        }  
        relative_point - the app will use this position as the comparison point.
                        It will compare the submitted points against the relative then return one that is closest.

    N/B: If you're sending the payload via multipart/form then ensure you eliminate the quotation marks since form values are submitted as strings by default.  


    */api/get-pairs*   [Get method]  
    Returns a response with the closest pair and it's distance from the supplied relative point.

```
#### Sample Format for using *application/json* 

![alt text](https://github.com/EKibet/django-assessment/blob/master/assets/post.png?raw=true)  
#### Sample Format for using *application/json* 

*/api/get-pairs*    [Get method]
![alt text](https://github.com/EKibet/django-assessment/blob/master/assets/djangoa.png?raw=true)  
#### Sample Format for using *multipart/form* 
![alt text](https://github.com/EKibet/django-assessment/blob/master/assets/form.png?raw=true)  
### Code Quality Conventions

This projects follows the PEP8 Style Guide 



## Built with
- Python version  3
- Django (DRF)
- Postgres
 ```

