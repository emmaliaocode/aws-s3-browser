FROM python:3.8-alpine
ENV PYTHONUNBUFFERED=1

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput

ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
