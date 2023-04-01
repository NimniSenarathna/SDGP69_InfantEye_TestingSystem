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

    # Calculate the mean of the reference points
    mean_reference_point = np.mean(reference_points, axis=0, dtype=np.int32)

    # Calculate the width and height of the eye region
    width = euclidean_distance(face_points[eye_points[0]], face_points[eye_points[1]])
    height = euclidean_distance(face_points[eye_points[2]], face_points[eye_points[3]])

    # Calculate the horizontal and vertical distances between the center of the eye and its corners
    center_to_left_corner_horizontal_width = euclidean_distance(mean_reference_point[:2],
                                                                face_points[eye_points[0]]) / width + 1e-6
    center_to_up_vertical_height = euclidean_distance(mean_reference_point[:2],
                                                      face_points[eye_points[2]]) / height + 1e-6

    return mean_reference_point, center_to_left_corner_horizontal_width, center_to_up_vertical_height


def current_position_details(face_points):
    # "minEnclosingCircle" opencv for finding the smallest circle
    (x, y), radius = cv.minEnclosingCircle(face_points)
    return [int(x), int(y), int(radius)]

