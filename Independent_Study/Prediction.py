__author__ = 'aliHitawala'

class Prediction(object):
    def __init__(self, prediction, confidence=1.0):
        self.prediction = prediction
        self.confidence = confidence

    def get_prediction(self):
        return self.prediction

    def get_confidence(self):
        return self.confidence