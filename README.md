# Example Flask Application

Prepare the enviroment:

```
cp .env.sample .env
```

Run application:

```
docker-compose up --build
```

Go to http://127.0.0.1:3000/hello.

Run application with [pipenv](https://github.com/pypa/pipenv):

```
brew install python3
brew install pipenv
cd app
pipenv install
pipenv shell
FLASK_APP=app.py flask run
```
