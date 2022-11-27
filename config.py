import os 

class Config(object):
    FLASK_SECRET = os.environ.get('FLASK_SECRET') or 'you-will-never-guess-this-one'


