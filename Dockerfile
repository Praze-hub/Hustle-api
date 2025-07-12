FROM python:3.8-slim
ENV PYTHONUNBUFFERED=1

WORKDIR /Hustle


# RUN apk update && apk add postgresql-dev libffi-dev gcc python3-dev musl-dev
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libffi-dev \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN mkdir -p /Hustle/staticfiles


RUN python manage.py collectstatic --noinput

EXPOSE 8000

# CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
CMD ["sh", "-c", "python manage.py collectstatic --noinput && gunicorn core.wsgi:application --bind 0.0.0.0:8000"]
