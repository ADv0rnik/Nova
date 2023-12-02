![GitHub repo file count](https://img.shields.io/github/directory-file-count/ADv0rnik/Nova?style=flat-square) ![GitHub language count](https://img.shields.io/github/languages/count/ADv0rnik/Nova?style=flat-square) ![Tests](https://github.com/ADv0rnik/Nova/actions/workflows/django_ci.yml/badge.svg) [![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3100/)

### Scope
ASNOVA - is the web service for self education and education with tutor in one-to-one format. 
The project is written using Python v.3.11 and django framework. Frontend part was performed by using Bootsrap V5.
The history of changes might be found in `changes_log.md`

### Requirements
The application require Python version 3.11 or older. For Windows users the oldest version of python interpreter can be found
here [http://www.python.org](http://www.python.org.). Also, the docker must be preinstalled on your machine in order to run docker containers for
database and other services on your local machine.

### Usage
1. Clone the repository onto your local machine by following command:

`git clone https://github.com/ADv0rnik/Nova.git`
or
`git clone git@github.com:ADv0rnik/Nova.git` (if you have an appropriate SSH key)

2. Install dependencies from `requirements.txt`
```commandline
pip install -r requirements.txt
```
3. Setup your `.env` file according to `.env.example` schema
4. In root directory run 
```commandline
docker compose up --build -d
```
5. Run make migrations command as following
```commandline
python manage.py makemigrations
python manage.py migrate
```
6. Create superuser by running the following command:
```python
python manage.py createsuperuser
```
7. Run the application locally with
```python
python manage.py runserver
```
