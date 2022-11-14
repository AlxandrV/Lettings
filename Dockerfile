FROM python:3.11

COPY . .

CMD python manage.py runserver