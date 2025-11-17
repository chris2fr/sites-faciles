tailwind-compile:
	npx @tailwindcss/cli -i ./include/tailwind.css -o ./static/assets/css/gdvoisins-tailwind.css 

.PHONY: messages
messages:
	../venv/bin/django-admin makemessages -l fr -l en --ignore=manage.py --ignore=medias --ignore=setup.py --ignore=staticfiles --ignore=workshop

.PHONY: compilemessages
compilemessages:
	../venv/bin/django-admin compilemessages -l fr -l en --ignore=manage.py --ignore=medias --ignore=setup.py --ignore=staticfiles --ignore=workshop