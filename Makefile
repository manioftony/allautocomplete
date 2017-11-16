init:
	pip install -r requirements.txt

clean:
	find . -name '*~' -delete
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete

server:
	python manage.py runserver

shell:
	python manage.py shell
