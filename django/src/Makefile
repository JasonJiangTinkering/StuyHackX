SHELL := /bin/bash

.PHONY: clean
clean:
	rm *~

.PHONY: superuser
superuser:
	echo "from users.models import CustomUser; CustomUser.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python3 manage.py shell

.PHONY: migration
migration:
	python3 manage.py makemigrations

.PHONY: migrate
migrate:
	python3 manage.py migrate

.PHONY: shell
shell:
	python3 manage.py shell

.PHONY: runserver
runserver:
	python3 manage.py runserver