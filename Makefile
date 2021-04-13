serve:
	python manage.py runserver

migrations:
	python manage.py makemigrations
	python manage.py migrate

shell:
	python manage.py shell

test:
	python manage.py test