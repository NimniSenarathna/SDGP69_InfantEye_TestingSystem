import numpy as np
import sys
import mediapipe as mp
import cv2 as cv
import json
import math
from time import time, sleep

with open("parameters.json", "r") as read_file:
    param = json.load(read_file)


# give euclidean distance of two points
def euclidean_distance(point1, point2):
    return math.dist(point1, point2)


# get center and the radius of iris
def iris_details(points):
    (r_x, r_y), r_radius = cv.minEnclosingCircle(points)
    return (r_x, r_y), r_radius