from flask import Flask, render_template, request, redirect, url_for, flash, session, make_response, Response, jsonify #pip install flask
import cv2 #pip install opencv-python-headless or pip install opencv-python
import numpy as np  
from pyzbar.pyzbar import decode #pip install pyzbar or pip install pyzbar[scripts]
from werkzeug.security import generate_password_hash, check_password_hash #pip install -U Werkzeug
from datetime import datetime, date #pip install datetime pip install pytz
import pytz 
import csv
# from appaditional.connect import connectBD
import pymysql #pip install pymysql #pip install mysql-connector-python-rf
import os
  
# UTC = pytz.utc 


# settings
application = Flask(__name__)
# UPLOAD_FOLDER = 'static/file/'

# Function for passwords 
def _create_password(password):
   return generate_password_hash(password,'pbkdf2:sha256:30',30)

# index page (user form)
@application.route('/')
def Index():
  try:
    return render_template('index.html')
    
  except Exception:
    return 'Hola en python'

# # home page 
# @application.route('/home',methods=['POST','GET'])
# def home():
#   try:
#     if 'FullName' in session:
#       return render_template('home.html',Datos = session)
#     else:
#       flash("Inicia Sesion")
#       return render_template('index.html')

#   except Exception as error:
#     flash(str(error))
#     return redirect('/') 
