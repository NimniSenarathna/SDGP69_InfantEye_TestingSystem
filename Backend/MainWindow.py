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


# normalize distance of points
def normalized_distance(distance, total_distance):
    return round((distance / total_distance), 2)


def polar_coordinates(point1, point2):
    x1 = point1[0] - point2[0]
    y1 = point1[1] - point2[1]
    rho = math.sqrt(math.pow(x1, 2) + math.pow(y1, 2)) / (point2[2] + 1e-6)
    theta = abs(math.degrees(math.atan(y1 / (x1 + 1e-6))))

    if x1 > 0 and y1 > 0:
        theta = 360 - theta

    if x1 > 0 and y1 < 0:
        theta = theta

    if x1 < 0 and y1 < 0:
        theta = 180 - theta

    if x1 < 0 and y1 > 0:
        theta = 180 + theta

    return rho, theta

# get the initial details of the iris point
def get_initial_details_of_center_of_the_eye(face_points, iris_points, eye_points, delay_time):
    # Initialize an array to store reference points for a certain period of time
    reference_points = np.zeros((1, 3))
    start_time = time()

    # Collect reference points for a specified delay time
    while time() - start_time < delay_time:
        points = face_points[iris_points]
        (x, y), radius = cv.minEnclosingCircle(points)
        reference_points = np.append(reference_points, [[x, y, radius]], axis=0)
