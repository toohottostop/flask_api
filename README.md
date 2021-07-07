# Flask API
Flask RESTful API

## For what?
- Learn what REST architecture is
- Learn to Build RESTful API with Flask
- Go through the full cycle of application development from task decomposition to deployment

## What used?
Pytnon:
[pytnon 3.8.5](https://www.python.org/downloads/release/python-385/)  

Libs:  
- Flask
- Flask-RESTful
- ORM SQLAlchemy
- Alembic migrations
- Marshmallow validation
- PyJWT. User authorization with JWT tokens  

## Installation
1. Make dir and jump into it  
`$mkdir flask_api && cd flask_api`
2. Clone repository  
`git clone https://github.com/toohottostop/flask_api.git`
3. Install virtual environment package  
`$sudo apt install python3-virtualenv`    
Set your virtual environment package  
`$python3 -m virtualenv <name_of_virtualenv>`  
Activate virtual environment  
`$source <name_of_virtualenv>/bin/activate`
4. Install requirements  
`pip install -r requirements.txt`
5. Make directory for your sqlite database
`$mkdir data`
Apply migrations
`flask db upgrade`
*You can populate your db with script `inserts_values_in_db.py` from folder "/src/database/"
   
## How to use  
`$python3 wsgi.py`
