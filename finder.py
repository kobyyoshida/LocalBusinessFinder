import requests
import json
import csv
 
api_key = 'fiyrU_gFRWeYqSbT66zWEGmKoY7_MAO_t4zkUPMaiHbD6_i4n4cN7_0h16ihNg-07yJUR7_toMqhmJib_KeNQCvMtgLKpcdAmHtbu0NclwxDgU06eAxdXsTtuIadYHYx'
headers = {'Authorization': 'Bearer %s' % api_key}
 
url = 'https://api.yelp.com/v3/businesses/search'
params = {'term':'veterinarian','location':'Orange County'}
 
req = requests.get(url, params=params, headers=headers)
 
parsed = json.loads(req.text)
 
businesses = parsed["businesses"]
 
for business in businesses:
    print("Name:", business["name"])
    print("Rating:", business["rating"])
    print("Address:", " ".join(business["location"]["display_address"]))
    print("Phone:", business["phone"])
    print("\n")
 
    id = business["id"]
 
    url="https://api.yelp.com/v3/businesses/" + id + "/reviews"
 
    req = requests.get(url, headers=headers)
 
    parsed = json.loads(req.text)
 
    reviews = parsed["reviews"]
 
    print("--- Reviews ---")
 
    #for review in reviews:
    #    print("User:", review["user"]["name"], "Rating:", review["rating"], "Review:", review["text"], "\n")
 
 