FROM python:3.10-bookworm

RUN mkdir -p /app
WORKDIR /app

COPY ./Pipfile /app/
COPY ./Pipfile.lock /app/
RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --deploy --system

COPY . /app/

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]