# -*- coding: utf-8 -*-
from app import app
import os
from app import Detector, Imager
from flask import json, render_template, url_for, request, redirect, send_from_directory, jsonify

detector = None
imager = None

@app.route('/')
def index():
    return render_template('index.html', engine=(not detector is None))

@app.route('/init', methods=['POST'])
def init():
    global detector, imager
    if not detector:
        detector = Detector()
    if not imager:
        imager = Imager()
    return jsonify(status = "ok")

@app.route('/', methods=['POST'])
def upload_file():
    file = request.files['file']
    issues = imager.validate(file)
    if issues:
        # TODO: вывести варнинг на страничку и отменить аплоад
        pass
    image_path = imager.upload(file)
    detector.detect(image_path)
    return jsonify(imageUrl = detector.last_result())
