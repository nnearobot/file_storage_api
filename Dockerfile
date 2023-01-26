FROM python:3.8-alpine

RUN apk update
RUN apk add nginx

RUN pip3 install --no-cache-dir pipenv
RUN pip3 install uwsgi

WORKDIR /usr/src/app
COPY Pipfile Pipfile.lock uwsgi.ini start.sh ./
COPY api ./api
COPY nginx.conf /etc/nginx/

RUN pipenv install --system --deploy

EXPOSE 80

ENTRYPOINT ["/usr/src/app/start.sh"]
