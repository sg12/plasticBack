FROM python:3.11

WORKDIR /app

COPY ./src /app

COPY ./requirements.txt /app

EXPOSE 8050

RUN pip3 install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8050"]