from flask import Flask
from .detector import *
from .imager import *

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif', '.bmp']
app.config['UPLOAD_PATH'] = 'static/uploaded'
app.config['RESULT_PATH'] = 'static/result'

from app import routes
