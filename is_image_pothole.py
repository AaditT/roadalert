import os
import time
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def classify():

    delete_cmd = "rm output.txt"
    classify_cmd = "python3 -m scripts.label_image --graph=tf_files/retrained_graph.pb --image=road.jpeg > output.txt"

    os.system(delete_cmd)
    os.system(classify_cmd)


    data_file = open("output.txt", "r")
    content_by_line = data_file.readlines()
    for line in content_by_line:
    	if line == '\n':
    		content_by_line.remove(line)

    if 'pothole' in str(content_by_line[1]):
        pothole_score = str(content_by_line[1]).replace('pothole ','')
        pothole_score = pothole_score.replace('(score=','')
        pothole_score = pothole_score.replace(')','')
        print("Pothole: " + str(pothole_score))

        not_pothole = 1 - float(pothole_score)

    elif 'road' in str(content_by_line[1]):
        not_pothole = str(content_by_line[1]).replace('road ','')
        not_pothole = not_pothole.replace('(score=','')
        not_pothole = not_pothole.replace(')','')
        print("Road: " + str(not_pothole))

        pothole_score = 1 - float(not_pothole)
    return([pothole_score, not_pothole])

def is_image_pothole():
    if float(classify()[0]) >= 0.8:
        return True
    elif float(classify()[1]) < 0.8:
        return False
is_image_pothole()
