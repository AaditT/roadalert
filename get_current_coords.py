from pigps import GPS
gps = GPS()

def get_current_coords():
    return([float(gps.lat),float(gps.lon)])
