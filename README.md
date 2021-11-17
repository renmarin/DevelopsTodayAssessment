# DevelopsTodayAssessment
A simple news board API

Heroku deployment link: [News Board API](https://news-board-api-786.herokuapp.com/).

Postman collection link: https://www.getpostman.com/collections/e4799db5c7f8a0e012d5

# Prerequisites
On your machine should be installed Docker and  to create application's work environment. You can use Docker Desktop on Mac and Windows, for Linux you need to install Docker Engine and Docker Compose. Guide how to install it:
https://docs.docker.com/get-started/#download-and-install-docker .

# API list

    http://127.0.0.1:8000/api/read                                                   - all news data
    http://127.0.0.1:8000/api/read/<id>                                              - detail about news
    http://127.0.0.1:8000/api/update/<id>                                            - update news
    http://127.0.0.1:8000/api/delete/<id>                                            - delete news
    http://127.0.0.1:8000/api/create                                                 - create new news
    http://127.0.0.1:8000/api/read/<id>/comments                                     - read comments
    http://127.0.0.1:8000/api/read/<id>/comments/create                              - create comment
    http://127.0.0.1:8000/api/read/<id>/comments/<comment_id>                        - read one comment
    http://127.0.0.1:8000/api/read/<id>/comments/<comment_id>/update                 - update comment
    http://127.0.0.1:8000/api/read/<id>/comments/<comment_id>/delete                 - delete comment
    http://127.0.0.1:8000/api/read/<id>/upvote                                       - upvote news

# How to run it

## Create a Django project

1. Change to the root of your project directory.

2. Create the Django project by running the **docker-compose run** command as follows.

    `sudo docker-compose run web django-admin startproject assessment .`      

3. After the docker-compose command completes, list the contents of your project. If you are running Docker on Linux, the files **django-admin** created are owned by root. This happens because the container runs as the root user. Change the ownership of the new files.

      `sudo chown -R $USER:$USER .`

## Connect the database

1. In your project directory, edit the **assessment/settings.py** file.
2. Replace the DATABASES = ... with the following:

      ```# settings.py 
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'postgres',
                'USER': 'postgres',
                'PASSWORD': 'postgres',
                'HOST': 'db',
                'PORT': 5432,
            }
        }
These settings are determined by the postgres Docker image specified in **docker-compose.yml**.

4. Run the `sudo docker-compose up` command from the top level directory for your project.

At this point, your Django app should be running at port 8000 on your Docker host. On Docker Desktop for Mac and Docker Desktop for Windows, go to http://localhost:8000

5. Use `sudo docker exec -ti [your_container] bash` to connect to container's terminal.

## Set up Django app

1. Configure django setting **assessment/settings.py** like this::

    ```
    INSTALLED_APPS = [
        ...
        'rest_framework',
        'news_board.apps.NewsBoardConfig',
    ]
    
2. Include the News Board API URLconf in your project urls.py like this::

    from django.urls import include

    path('', include('news_board.urls')),

3. Run "python manage.py migrate" to create the News Board API models.

4. Visit http://127.0.0.1:8000 **before accessing API**.

## Data
This API uses JSON data format. Below are shown some examples of data.

News:

``
{
        "id": 1,
        "title": "Test News 1",
        "link": "news-board-api-786.herokuapp.com",
        "creation_date": "2021-11-17T03:16:00+02:00",
        "amount_of_upvotes": 0,
        "author_name": "Admin"
    }
``

Comments:

``
{
        "id": 1,
        "author_name": "Admin",
        "content": "Some comment",
        "creation_date": "2021-11-17T03:24:32+02:00",
        "news_f": 3
    }
``

news_f - the ID of a specific news
