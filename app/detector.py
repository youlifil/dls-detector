from flask import current_app
import os
from flask.helpers import url_for
import torch
import cv2

class Detector:
    def __init__(self):
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', force_reload=False)
        self._last_result = None

    def _save_path(self):
        return os.path.join(current_app.root_path, current_app.config['RESULT_PATH'])

    def _save_filename(self):
        return os.path.join(self._save_path(), 'image0.jpg')

    def last_result(self):
        return self._last_result
    
    def detect(self, path):
        self.img = cv2.imread(path)[:, :, ::-1]
        self.model.conf = 0.5
        results = self.model(self.img)
        results.save(self._save_path())
        self._last_result = os.path.join(current_app.config["RESULT_PATH"], 'image0.jpg')
        return results.pred
