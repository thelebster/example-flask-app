FROM python:3.7-alpine
LABEL maintainer="Anton Lebedev <mailbox@lebster.me>"
WORKDIR /app
RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . /app
ENV FLASK_APP=${FLASK_APP}
ENV FLASK_ENV=${FLASK_ENV}
CMD flask run --host ${FLASK_HOST} --port ${FLASK_PORT}
