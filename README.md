# DjangoBlog

------------------------------------------------------------------------------------------------------------------------

## Table of contents
* [General info](#General-info)
* [Setup](#Setup)

------------------------------------------------------------------------------------------------------------------------

## General info:

This Blogging web application project is purely made with Django as the backend.

This web application creates a very basic blog site using Django. The site allows blog authors to create text-only blogs using the Admin site, and any logged-in user to add comments via a form.

------------------------------------------------------------------------------------------------------------------------

## Setup

To run this app, you will need to follow these 5 steps:

1. Clone This Project (Make Sure You Have Git Installed)
```
https://github.com/aviz92/DjangoBlog.git
```

2. Install Dependencies
```
pip install -r requirements.txt
```

3. Set Database (Make Sure you are in directory same as manage.py)
```
python manage.py makemigrations
python manage.py migrate
```

4. Create Superuser 
```
python manage.py createsuperuser
```

5. After all these steps , you can start testing and developing this project. 
```
python manage.py runserver
```

#### That's it! Happy Coding!
------------------------------------------------------------------------------------------------------------------------
