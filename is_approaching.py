from math import sin, cos, sqrt, atan2, radians
import csv

# approximate radius of earth in km
R = 6373.0

def distance_between(lat1, lon1, lat2, lon2):
	lat1 = radians(lat1)
	lon1 = radians(lon1)
	lat2 = radians(lat2)
	lon2 = radians(lon2)
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))
	distance_in_km = R * c
	distance_in_ft = distance_in_km * 3280.84
	return(distance_in_ft)

def is_approaching():
	with open('pothole_coordinates.csv', newline='') as csvfile:
	    data = list(csv.reader(csvfile))
	for coordinate in data:
		if distance_between(float(coordinate[0]),float(coordinate[1]),current_lat, current_lon) <= 50:
			return True
