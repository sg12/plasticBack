FROM python:3.11

WORKDIR /app

COPY ./src /app

COPY ./requirements.txt /app

EXPOSE 8000

RUN pip3 install -r requirements.txt

RUN python manage.py makemigrations

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]