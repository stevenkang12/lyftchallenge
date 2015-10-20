# Steven Kang
# Lyft Programming Challenge
# Oct. 20, 2015
# Description: This finds the minimum distance between opposing paths according to their latitude and longitude on Earth. Values are returned in miles and distance is calculated using the Haversine formula.

import math # Needed for invsin

class Point(object):
    def __init__(self, lat, lon):
        self.latitude = float(lat)
        self.longitude = float(lon)
   
    def set_latitude(self, val):
        self.latitude = val
    
    def set_longitude(self, val):
        self.longitude = val

    def __repr__(self):
        return "<Point, latitude:%f, longitude:%f>" % (self.latitude, self.longitude)

# use the Haversine formula
# Inputs: P1 & P2 are two point objects.
def distanceBetweenPoints(P1, P2):
    # Radius of the earth = 3,959 mi.
    r = 3959
    lat1, lon1 = P1.latitude, P1.longitude
    lat2, lon2 = P2.latitude, P2.longitude
    # Use haversine formula to find distance.
    h = ((math.sin((lat2-lat1)/2))**2)+math.cos(lat1)*math.cos(lat2)*(math.sin((lon2-lon1)/2)**2)
    dist = 2*r*(math.asin(h**(.5)))
    return dist

# pointsArr stores all of the points. 
# The distance of a path is the summed distance of each sequential pair of points. 
def distanceInPath(self, pointsArr):
    num = len(pointsArr)
    pairs = [distanceBetweenPoints(i,j) for i,j in zip(pointsArr[:num-1],pointsArr[1:num])]
    return sum(pairs)

def example():
    # Define 4 example points.
    A, B, C, D = Point(25, 75), Point(35, 55), Point(15, 100), Point(35, 100)
    # Define 2 paths.
    paths = [[A, C, D, B], [C, A, B, D]]
    # Calculate the points for both.
    distance = [[i, distanceInPath(p)] for i, p in enumerate([path1, path2])]
    sorteddist = sorted(distance, key=lambda x:x[1])
    minidx = sorteddist[0][0] # Grabs the idx.
    # Print out an appropriate response.
    print "The shorter path involves the following points in order:"
    for p in paths[minidx]:
        print "\t(%f, %f)" % (p.latitude, p.longitude)
    
if __name__ == "__main__":
    example()
