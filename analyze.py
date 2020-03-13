import math
import numpy as np


def calc_angle(eye_vec,stim_vec):
    dot_prod = np.dot(eye_vec,stim_vec)
    angle = np.arccos(dot_prod)
    return angle

def points_to_vec(points):
    diff = np.subtract(points[0],points[1])
    dist = distance(points[0],points[1])
    vec = [diff[0] / dist, diff[1] / dist]
    return vec

def vis_field_line(closer,further,magn):
    eye_vec = points_to_vec([closer,further])
    delta_x = eye_vec[0] * magn
    delta_y = eye_vec[1] * magn

    x1 = closer[0]
    y1 = closer[1]

    x2 = x1 + delta_x
    y2 = y1 + delta_y
    return [(x1,x2),(y1,y2)], eye_vec

def distance(c1,c2):
    subd = np.subtract(c1, c2)
    dist = math.sqrt(subd[0] ** 2 + subd[1] ** 2)
    return dist

def eye_to_stim(left,right,stim_point):
    l_diff = distance(left,stim_point)
    r_diff = distance(right,stim_point)
    if l_diff < r_diff:
        closer = left
        further = right
        diff = l_diff
    else:
        closer = right
        further = left
        diff = r_diff
    return ((closer[0],stim_point[0]),(closer[1],stim_point[1])), closer, further, diff



