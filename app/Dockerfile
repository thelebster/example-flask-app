FROM python:3.7-alpine
LABEL maintainer="Anton Lebedev <mailbox@lebster.me>"
WORKDIR /app
RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . /app
ENV FLASK_APP=app.py
CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "5000" ]
