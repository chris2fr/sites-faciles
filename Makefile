# Loading environment variables
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

ifeq ($(USE_DOCKER),1)
	EXEC_CMD := docker-compose exec -ti web
else
	EXEC_CMD :=
endif

.PHONY: web-prompt
web-prompt:
	$(EXEC_CMD) bash

.PHONY: test-unit
test-unit:
	$(EXEC_CMD) poetry run python manage.py test --settings wagtail_village.config.settings_test

.PHONY: collectstatic
collectstatic:
	$(EXEC_CMD) poetry run python manage.py collectstatic --noinput --ignore=*.sass


.PHONY: messages
messages:
	$(EXEC_CMD) poetry run django-admin makemessages -l fr --ignore=manage.py --ignore=medias --ignore=setup.py --ignore=staticfiles --ignore=templates

.PHONY: sass
sass:
	$(EXEC_CMD) poetry run python manage.py compilescss
	make collectstatic

.PHONY: quality
quality:
	$(EXEC_CMD) poetry run black --check --exclude=venv .
	$(EXEC_CMD) poetry run isort --check --skip-glob="**/migrations" --extend-skip-glob="venv" .
	$(EXEC_CMD) poetry run flake8 --count --show-source --statistics --exclude="venv,**/migrations" .

.PHONY: fix
fix:
	$(EXEC_CMD) poetry run black --exclude=venv .
	$(EXEC_CMD) poetry run isort --skip-glob="**/migrations" --extend-skip-glob="venv" .


.PHONY: init
init:
	$(EXEC_CMD) poetry install
	$(EXEC_CMD) poetry run pre-commit install
	$(EXEC_CMD) poetry run python manage.py migrate
	make collectstatic
	$(EXEC_CMD) poetry run python manage.py set_config
	$(EXEC_CMD) poetry run python manage.py create_starter_pages

.PHONY: demo
demo:
	make init
	$(EXEC_CMD) poetry run python manage.py create_demo_pages

.PHONY: runserver
runserver:
	$(EXEC_CMD) poetry run python manage.py runserver 
	# $(EXEC_CMD) poetry run python manage.py runserver $(HOST_URL):$(HOST_PORT)


.PHONY: test
test:
	$(EXEC_CMD) poetry run python manage.py test

.PHONY: test
# From https://tailwindcss.com/docs/installation/tailwind-cli
tailwind-install-bin-linux:
	wget https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64 
	mv tailwindcss-linux-x64 venv/bin/tailwindcss
	chmod +x venv/bin/tailwindcss

.PHONY: test
# From https://tailwindcss.com/docs/installation/tailwind-cli
tailwind-install:
	npm install tailwindcss @tailwindcss/cli

.PHONY: test
# From https://tailwindcss.com/docs/installation/tailwind-cli
tailwind-compile:
	npx @tailwindcss/cli -i ./lesgv/src/tailwind/input.css -o ./lesgv/static/css/lesgv/tailwind.css -m

.PHONY: test
tailwind-compilemax:
	npx @tailwindcss/cli -i ./lesgv/src/tailwind/input.css -o ./lesgv/static/css/lesgv/tailwind.css 

.PHONY: test
tailwind-watch:
	npx @tailwindcss/cli -i ./lesgv/src/tailwind/input.css -o ./lesgv/static/css/lesgv/tailwind.css --watch

fixtures-dump-test-initial:
	mkdir -p fixtures
	touch fixtures/not.json
	rm fixtures/*.json
	./venv/bin/python manage.py dumpdata --natural-foreign auth.group > fixtures-1-auth-group.json
	./venv/bin/python manage.py dumpdata --natural-foreign auth.user > fixtures-2-auth-user.json
	./venv/bin/python manage.py dumpdata --natural-foreign wagtailcore.collection > fixtures-3-wagtailcore-collection.json
	./venv/bin/python manage.py dumpdata --natural-foreign taggit > fixtures-4-taggit.json
	./venv/bin/python manage.py dumpdata --natural-foreign wagtailcore.Locale wagtailcore.Revision wagtailcore.Page wagtailcore.Site wagtailimages.Image  wagtaildocs.Document django_village lesgv wagtail_village_blog wagtail_village_forms wagtail_village_lesgrandsvoisins wagtail_village wagtailmenus wagtailsnippets wagtailusers socialaccount > fixtures-initial.json 
	mkdir -p fixtures/media/{original_,}images
	mkdir -p media/{original_,}images
	touch fixtures/media/{original_,}images/not.txt
	cp -a fixtures/media/images/* medias/images
	cp -a fixtures/media/original_images/* medias/original_images

fixtures-load-test-initial:
	./venv/bin/python manage.py loaddata fixtures/test-initial.json
	cp -a fixtures/media/* medias

fixtures-building-dump:
	rm fixtures-initial.json
	./venv/bin/python manage.py dumpdata --natural-foreign wagtailcore.Locale wagtailcore.Revision wagtailcore.Page wagtailcore.Collection wagtailcore.Site wagtailimages.Image  wagtaildocs.Document django_village lesgv wagtail_village_blog wagtail_village_forms wagtail_village_lesgrandsvoisins wagtail_village wagtailmenus  wagtailsnippets allauth auth wagtailusers socialaccount > fixtures-initial.json 
	ls -la fixtures-initial.json
	mv fixtures-initial.json /tmp

fixtures-building-load:
	./venv/bin/python manage.py loaddata -e auth.Permission /tmp/fixtures-initial.json 

help:
	find . -type f -name Makefile
	grep -e "^[-A-Za-z0-9_]*:" Makefile | sed 's/:.*//g'

fixtures-dump:
	./venv/bin/python manage.py dumpdata \
  --natural-foreign \
	--natural-primary \
	--indent=2 \
	-e auth.Permission \
	-e contenttypes \
	-e sessions \
	-e wagtailimages.rendition \
	auth.group \
	auth.user \
	wagtailcore.collection \
	taggit \
	wagtailcore.Locale \
	wagtailcore.Page \
	wagtailcore.Collection \
	wagtailcore.Site \
	wagtailimages.Image \
	wagtaildocs.Document \
	django_village \
	lesgv \
	wagtail_village_blog \
	wagtail_village_forms \
	wagtail_village_lesgrandsvoisins \
	wagtail_village \
	wagtailmenus \
	wagtailsnippets \
	allauth \
	auth \
	wagtailusers \
	socialaccount \
	wagtailcore.revision > dump.json
#	grep 'revision":' dump.json | sed 's/[^0-9]//g' | uniq | sort -h - | awk '/^[0-9]+$/' ORS=',' | sed 's/,$//' > dump-revisions.txt 
#	./venv/bin/python manage.py dumpdata --pks `cat dump-revisions.txt` wagtailcore.Revision > dump-revisions.json

fixtures-dump-context:
	./venv/bin/python manage.py dumpdata \
  --natural-foreign \
	--natural-primary \
	--indent=2 \
	-e auth.Permission \
	-e contenttypes \
	-e sessions \
	-e wagtailimages.rendition \
	auth.group \
	auth.user \
	wagtailcore.collection \
	taggit \
	wagtailcore.Locale \
	wagtailimages.Image \
	wagtaildocs.Document \
	allauth \
	auth \
	wagtailusers \
	socialaccount > dump-context.json
# 	-e postgres_search.indexentry \
# 	-e wagtailcore.Revision \

fixtures-dump-content:
	./venv/bin/python manage.py dumpdata \
  --natural-foreign \
	--natural-primary \
	--indent=2 \
	-e auth.Permission \
	-e contenttypes \
	-e sessions \
	-e wagtailimages.rendition \
	wagtailcore.Page \
	wagtailcore.Site \
	django_village \
	lesgv \
	wagtail_village_blog \
	wagtail_village_forms \
	wagtail_village_lesgrandsvoisins \
	wagtail_village \
	wagtailmenus \
	wagtailsnippets \
	socialaccount \
	wagtailcore.revision > dump-content.json

requirements:
	./venv/bin/pip install -r requirements.txt 