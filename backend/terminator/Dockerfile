# pull official base image
FROM python:3.8.3-alpine
# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# copy project
COPY . /backend
ENTRYPOINT ["python", "/backend/manage.py", "runserver", "0.0.0.0:8000"]
