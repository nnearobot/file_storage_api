FROM python:3.8-alpine

RUN apk update
RUN pip3 install --no-cache-dir pipenv

WORKDIR /usr/src/app
COPY Pipfile Pipfile.lock ./
COPY api ./api
RUN mkdir -p /usr/src/app/files

RUN pipenv install --system --deploy

EXPOSE 5000


ENTRYPOINT ["python3"]

CMD ["filestorage.py"]
