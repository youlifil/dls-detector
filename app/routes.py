# -*- coding: utf-8 -*-
from app import app
import os
from app import Detector, Imager
from flask import json, render_template, url_for, request, redirect, send_from_directory, jsonify, g

@app.route('/')
def index():
    # return render_template('index.html', engine=('detector' in g))
    return render_template('index.html')

# @app.route('/init', methods=['POST'])
# def init():
#     if 'detector' not in g:
#         g.detector = Detector()
#     if 'imager' not in g:
#         g.imager = Imager()
#     print(g.imager)
#     return jsonify(status = "ok")

@app.route('/', methods=['POST'])
def upload_file():
    file = request.files['file']
    imager = Imager()
    detector = Detector()
    issues = imager.validate(file)
    if issues:
        # TODO: вывести варнинг на страничку и отменить аплоад
        pass
    image_path = imager.upload(file)
    detector.detect(image_path)
    return jsonify(imageUrl = detector.last_result())
