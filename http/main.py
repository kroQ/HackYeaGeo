import googlemaps
import ast
import requests
import queue


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
        print("Geting gelocation google")
        r = requests.get(
            "https://maps.googleapis.com/maps/api/geocode/json?address={0}&key=AIzaSyA07o97XCzHbUCPxN0DeCXezL2Dwdv0-f4".format(
                str(street)), verify=False)
        # geocode_results = self.gmaps.geocode(str(street))
        # return ast.literal_eval(str(geocode_results))[0]['geometry']['location']
        return r.json()['results'][0]['geometry']['location']

    def get_cord_arcgis(self, street):
        print("Geting gelocation esri")
        r = requests.get(
            "https://utility.arcgis.com/usrsvcs/appservices/GK9LgG0PlpZvIHP8/rest/services/World/GeocodeServer/findAddressCandidates?SingleLine={0}&f=pjson".format(
                str(street)), verify=False)
        if r.status_code == 200:
            return r.json()['candidates'][0]['location']
        else:
            raise Exception("Error")

        pass


if __name__ == "__main__":
    s = Street("Pruska", "24")
    a = HttpRequest()
    print(str(a.get_cord_google(s)))
    print(str(a.get_cord_arcgis(s)))


    # wgs84 = osr.SpatialReference()
    # pl65 = osr.SpatialReference()
    # wgs84.ImportFromEPSG(4326)
    # pl65.ImportFromEPSG(2178) # pl-2000
    # ct = osr.CoordinateTransformation(wgs84, pl65)
    # pl65pt = ct.TransformPoint(50.0847602, 19.9966874)
    # print(pl65pt)
