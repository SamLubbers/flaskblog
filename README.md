# flaskblog
personal blog developed with Flask and SQlite3. Learned from the [official flask docummentation tutorial](http://flask.pocoo.org/docs/0.12/tutorial/)

## installation

Clone or download repository onto local computer

```bash
git clone https://github.com/SamLubbers/flaskblog.git
```

install application with necessary dependecies (preferably in a virtualenv, to avoid conflicts with existing packages in your computer)

```bash
cd flaskblog
pip install -e .
```

## usage

export an environment variable that tells Flask where to find the application instance. Make sure to be inside the project directory and run the following

```bash
export FLASK_APP=flaskblog
```
Initialize the database

```bash
flask initdb
```

Run the application

```bash
flask run
```

## debug

turn on debug mode with the following environment variable

```bash
export FLASK_DEBUG=true
```
run the application just like before

```bash
flask run
```
