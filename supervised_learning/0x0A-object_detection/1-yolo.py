#!/usr/bin/env python3
"""
Initialize Yolo
"""
import tensorflow.keras as K
import numpy as np


class Yolo():
    """
    Yolo that uses the Yolo v3 algorithm to perform object detection
    """

    def __init__(self, model_path, classes_path, class_t, nms_t, anchors):
        """
        model: the Darknet Keras model
        class_names: a list of the class names for the model
        class_t: the box score threshold for the initial filtering step
        nms_t: the IOU threshold for non-max suppression
        anchors: the anchor boxes
        """
        self.model = K.models.load_model(model_path)
        with open(classes_path, 'r') as r:
            data = r.read()
        self.class_names = data.split()
        self.class_t = class_t
        self.nms_t = nms_t
        self.anchors = anchors

    def sig(self, x):
        """
        Sigmoid
        """
        return (1 / (1 + np.exp(-x)))

    def process_outputs(self, outputs, image_size):
        """
        image_size is a numpy.ndarray containing the image’s original size
        [image_height, image_width].
        Returns a tuple of (boxes, box_confidences, box_class_probs)
        boxes: a list of numpy.ndarrays of shape (grid_height, grid_width,
        anchor_boxes, 4) containing the processed boundary boxes for each
        output, respectively.
        box_confidences: a list of numpy.ndarrays of shape (grid_height,
        grid_width, anchor_boxes, 1) containing the box confidences for each
        output, respectively.
        """
        boxes = []
        box_confidences = []
        box_class_probs = []
        for i, box in enumerate(boxes):
