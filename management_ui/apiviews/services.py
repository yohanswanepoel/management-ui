import requests
import random

URL_RELIANTPARTIES = "http://polyglot-demo-rp-myproject.192.168.99.104.nip.io/api/v1/reliantparties/"
URL_PROVIDER = "http://polyglot-demo-provider-myproject.192.168.99.104.nip.io/provider-api/api/v1/providers"
TIME_OUT = 2
#URL_RELIANTPARTIES = "http://0.0.0.0:7080/api/v1/reliantparties/"

def load_providers():
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

def get_count_reliant_parties(status):
    url = URL_RELIANTPARTIES + "count/"
    if status is not None:
        url = url + "?status=" + status
    try:
        result = requests.get(url, timeout = TIME_OUT)
        response = result.json()
    except:
        response = {}
    return response

def get_parties(status):
    url = URL_RELIANTPARTIES
    if status is not None:
        url = url + "?status=" + status
    #params = {'year': year, 'author': author}
    #r = requests.get(url, params=params)
    result = requests.get(url, timeout = TIME_OUT)
    response = result.json()
    return response

def get_party(key):
    url = URL_RELIANTPARTIES
    if key is not None:
        url = url + key
    #params = {'year': year, 'author': author}
    #r = requests.get(url, params=params)
    result = requests.get(url, timeout = TIME_OUT)
    response = result.json()
    return response

def update_create_party(object):
    if not 'id' in object:
        object["id"] = ""
    if object["id"] == "":
        #Create
        del object["id"]
        url = URL_RELIANTPARTIES
        result = requests.post(url, data=object, timeout = TIME_OUT)
    else:
        #Update
        url = URL_RELIANTPARTIES + object["id"] + "/"
        result = requests.put(url, data=object, timeout = TIME_OUT)
    return object
