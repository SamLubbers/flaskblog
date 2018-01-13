# flaskblog
personal blog developed with Flask and SQlite3. Learned from the [official flask docummentation tutorial](http://flask.pocoo.org/docs/0.12/tutorial/)

## prerequisites

Python 3.6

PostgreSQL. If you are on MacOS you can install it with [Homebrew](https://brew.sh/)


´´´bash
brew update
brew install postgresql
´´´ 

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

## Running

Run the application (development mode, debug on by default)

```bash
./run.sh
```
