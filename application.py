from email.mime import application
from flask import Flask

application = Flask(__name__)

# index page (user form)
@application.route('/')
def Index():
    return 'Hola Mundo'