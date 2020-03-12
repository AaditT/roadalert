from flask import Flask
from flask_googlemaps import GoogleMaps
from flask import Flask, render_template
from flask_googlemaps import Map
import csv
app = Flask(__name__)

api_key = ""
# you can set key as config
app.config['GOOGLEMAPS_KEY'] = api_key

# Initialize the extension
GoogleMaps(app)

pothole_list=[]

with open('pothole_coordinates.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
        if row[0] != "lat":
            pothole_list.append(tuple([float(row[0]),float(row[1])]))



@app.route("/")
def mapview():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        style = "height:500px;width:500px;margin:0;",
        markers=[]
        )
    for (lat1, lon1) in pothole_list:
        mymap.markers.append(
              {
              'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
              'lat': lat1,
              'lng': lon1,
              'infobox': "<strong>Added on:</strong> 1/2/13 </br> <strong>Accelerometer Data-Based</strong>"
              },
              )
    return render_template('example.html', mymap=mymap)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
