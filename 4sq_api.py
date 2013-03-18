import time
import urllib2
import json

def get_restaurant_entries(restaurant):
    url = "https://api.foursquare.com/v2/venues/search?"
    version = "v=" + time.strftime("%Y%m%d")
    API_KEY= "&client_id=JSM3WVVM1OTXSHTUALUK1VADIKD5TGS3IQT2H5CX40TC4M1V&client_secret=KZ1Q4UGUJZD21TLPMK3SJY1YBUCBHGQN2X5MLRKVXYV5YVVA"
    intent = "&intent=browse"
    ll_hacker_school = "&ll=40.726576,-74.000645"
    radius = "&radius=800"
    query = "&query=" + restaurant

    query_link = ""
    query_link += url
    query_link += version
    query_link += API_KEY
    query_link += intent
    query_link += ll_hacker_school
    query_link += radius
    query_link += query
    #print query_link

    response = urllib2.urlopen(query_link)
    json_obj = json.load(response)
    venues = json_obj['response']['venues']
    closest_addresses = []
    #return_string = "The closest restaurants to " + restaurant + " are: "
    for restaurant in venues:
        #print restaurant
        location = restaurant['location']
        address = location ['address']
        btwn = location ['crossStreet']
        closest_addresses.append(address + " " + btwn)
    return closest_addresses

print get_restaurant_entries("chipotle")

