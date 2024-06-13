FROM python:3.10-bookworm

RUN mkdir -p /backend
WORKDIR /backend

COPY ./Pipfile /backend/
COPY ./Pipfile.lock /backend/
RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --deploy --system

COPY . /backend/

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]