FROM python:3.11

COPY . .

RUN pip install --upgrade pip \
&& pip install -r requirements.txt

ENV PORT=8000

CMD python manage.py runserver 0.0.0.0:$PORT