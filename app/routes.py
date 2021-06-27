# -*- coding: utf-8 -*-
from app import app
from app.detection.Detector import Detector
from flask import render_template, url_for

detector = None

def init():
    global detector
    if not detector:
        detector = Detector()

@app.route('/')
@app.route('/index')
def index():
    init()
    result = detector.detect()
    file = url_for('static', filename='image0.jpg')
    return render_template('index.html', image=file)
