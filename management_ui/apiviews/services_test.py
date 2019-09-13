from .services import *

import requests
import random
import json

def load_parties():
    print("..........Populate parties..........")
    states = ['ACT','NSW','NT','QLD','TAS','VIC','WA']
    status = ['New','Alpha','Beta','Active','Down','Retired']
    party = {}
    party['name'] = 'name'
    party['status'] = 'New'
    party['email'] = 'name@email.com'
    party['abn'] = '1233421243'
    party['address_street_1'] = '11 Some Avenue'
    party['address_street_2'] = 'Suburb'
    party['address_state'] = 'ACT'
    party['address_post_code'] = '2022'
    party['contact_phone'] = '024837832'
    party['name'] = 'name'
    for x in range(100):
        party['status'] = random.choice(status)
        party['address_state'] = random.choice(states)
        party['name'] = "name" + str(x)
        update_create_party(party)
    return "Done"

def load_providers():
    states = ['ACT','NSW','NT','QLD','TAS','VIC','WA']
    status = ['New','Alpha','Beta','Active','Down','Retired']
    party = {}
    party['businessNumber'] = '1233421243'
    party['contact'] = 'name'
    party['email'] = 'name@email.com'
    party['name'] = 'person name'
    party['status'] = 'New'
    for x in range(20):
        party['status'] = random.choice(status)
        party['name'] = "name" + str(x)
        party['contact'] = "contact" + str(x)
        update_create_provider(party)
    return "Done"

def delete_all_parties():
    url = URL_RELIANTPARTIES + "clear/"
    print(url)
    try:
        result = requests.get(url, timeout = TIME_OUT)
        response = result.json()
        response = "Done"
    except:  # This is the correct syntax
        response = result
    return response

def delete_all_providers():

    providers = get_providers()
    # Not code that I am going to love (but this is what the API has) - iterate and remove
    for p in providers:
        url = URL_PROVIDER +str(p["id"])
        try:
            result = requests.delete(url, timeout = TIME_OUT)
        except:  # This is the correct syntax
            response = result
    return "Done"