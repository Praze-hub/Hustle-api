FROM python:3.8-alpine
ENV PYTHONUNBUFFERED=1
RUN apk update && apk add postgresql-dev libffi-dev gcc python3-dev musl-dev
WORKDIR /Hustle
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN python manage.py collectstatic --noinput

CMD gunicorn your_project.wsgi:application --bind 0.0.0.0:$PORT
