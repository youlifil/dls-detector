import torch
import cv2

class Detector:
    def __init__(self):
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', force_reload=False)

    def detect(self):
        self.img = cv2.imread('./image.jpg')[:, :, ::-1]
        self.model.conf = 0.5
        results = self.model(self.img)
        results.save('./app/static')
        return str(results.pred)
