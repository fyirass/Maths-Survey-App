NB: Run redis-server.exe if you have a port 6379 error.

1- Download and Install Python from Here: https://www.python.org/downloads/

2- Install virtualenviroment:

	python -m pip install --user virtualenv

3- Create virtualenviroment:

	python -m venv env
  
4- Activate virtualenviroment:

	env\Scripts\activate

5- Install django

	pip install django
	django-admin startproject {project-name}
	python manage.py startapp app_name

6- Copy the project on the env document, open it and install all the libraries
	
	cd env
	cd Face-Analytics-App-main
	pip install -r requirements.txt	

7- Make migrations database

	python manage.py makemigrations
	python manage.py migrate
	python manage.py createsuperuser

8- Run the Project

	python manage.py runserver

9- Run this link on your browser

	http://127.0.0.1:8000/deepface/

10-generate requirements.txt python

	pip list --format=freeze > requirements.txt
	pip install -r requirements.txt

11- 
	
	whitenoise.storage.CompressedManifestStaticFilesStorage

	STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
	STATIC_ROOT = BASE_DIR / 'staticfiles'


12- Creat superuser

	python manage.py createsuperuser


13

	apt-get install libglu1
	apt-get install libglib2.0-0
	
	apt-get update
	apt-get install redis-server
	
	redis-server
















django


regester class into database
admin: admin.site.register(Question)