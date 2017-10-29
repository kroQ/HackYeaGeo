import googlemaps
import ast
from gdal import osr
from arcgis.geocoding import geocode
import requests

class Street:
    def __init__(self, street, number):
        self.city = "Kraków"
        self.street = street
        self.number = number

    def __str__(self):
        return "{0} {1} {2}".format(self.city, self.street, self.number)

class HttpRequest():

    def __init__(self):
        self.gmaps = googlemaps.Client(key="AIzaSyDaKujEXD4mtbDj0DLCPZ8j4G3-OtT-TUU")
        self.gmaps.timeout = 200


    def get_cord_google(self, street):
        print("Geting gelocation google for :{0}".format(str(street)))
        geocode_results = self.gmaps.geocode(str(street))
        return str(geocode_results)

    def get_cord_arcgis(self):
        arcgis = geocode(address="Skarżynskiego 3", )

        # data = self.arcgis.FindAddressCandidates("Skarżynskiego 3")
        return arcgis

    def get_cord(self, street):
        return ast.literal_eval(str(self.get_cord_google(street)))

        pass

if __name__ == "__main__":
    s = Street("Pruska", "24")
    a = HttpRequest()
    # res = a.get_cord(s)
    # print(res[0]['geometry']['location'])
    print(a.get_cord_arcgis())

    # wgs84 = osr.SpatialReference()
    # pl65 = osr.SpatialReference()
    # wgs84.ImportFromEPSG(4326)
    # pl65.ImportFromEPSG(2178) # pl-2000
    # ct = osr.CoordinateTransformation(wgs84, pl65)
    # pl65pt = ct.TransformPoint(50.0847602, 19.9966874)
    # print(pl65pt)



