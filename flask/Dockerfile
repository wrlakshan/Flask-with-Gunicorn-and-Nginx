FROM python:3.8

# Define a build-time argument
ARG APP_NAME_ARG

# You can set it as an environment variable if needed at runtime too
ENV APP_NAME_ARG=${APP_NAME_ARG}

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]
