version := $(shell cat include/VERSION)

tailwind-compile:
	date +"%Y-%m-%d-%Hh%Mm%Ss" > include/VERSION
	../venv/bin/python ./include/replace-tailwind-version.py
	-rm ./static/assets/css/gdvoisins-tailwind-*.css
	npx @tailwindcss/cli -i ./include/gdvoisins-tailwind-input.css -o ./static/assets/css/gdvoisins-tailwind-${version}.css 

.PHONY: messages
messages:
	../venv/bin/django-admin makemessages -l fr -l en --ignore=manage.py --ignore=medias --ignore=setup.py --ignore=staticfiles --ignore=workshop

.PHONY: compilemessages
compilemessages:
	../venv/bin/django-admin compilemessages -l fr -l en --ignore=manage.py --ignore=medias --ignore=setup.py --ignore=staticfiles --ignore=workshop