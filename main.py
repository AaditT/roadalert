from is_approaching import is_approaching
from get_current_coords import get_current_coords
from alert import alert
from is_image_pothole import is_image_pothole
import csv


def add_new_pothole():
    with open('pothole_coordinates.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([get_current_coords()[0],get_current_coords()[1]])

def loop():
    if is_approaching():
        alert()
        add_new_pothole()
        time.sleep(1)
        break
    elif not is_approaching():
        if is_image_pothole():
            alert()
            add_new_pothole()
            time.sleep(1)
            break
        elif not is_image_pothole():
            if is_accel_pothole():
                add_new_pothole()
                time.sleep(1)
            elif not_accel_pothole():
                break

while True:
    loop()
