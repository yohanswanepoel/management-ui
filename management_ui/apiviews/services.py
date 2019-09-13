import requests
import random
import json
import os

URL_RELIANTPARTIES = "http://" os.getenv('URL_RELIANTPARTIES', '') + ":8080/api/v1/reliantparties/"
URL_PROVIDER = "http://" os.getenv('URL_PROVIDER', '') + ":8080/provider-api/api/v1/providers/"

#URL_RELIANTPARTIES = "http://polyglot-demo-rp-myproject.192.168.99.104.nip.io/api/v1/reliantparties/"
#URL_PROVIDER = "http://polyglot-demo-provider-myproject.192.168.99.104.nip.io/provider-api/api/v1/providers/"
TIME_OUT = 2
#URL_RELIANTPARTIES = "http://0.0.0.0:7080/api/v1/reliantparties/"

def get_count_providers():
    url = URL_PROVIDER + "count/"
    try:
        result = requests.get(url, timeout = TIME_OUT)
        response = result.content.decode("utf-8").replace("'", '"')
    except:
        response = {}
    json_response = json.loads(response)
    return json_response

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

def get_providers():
    url = URL_PROVIDER
    result = requests.get(url, timeout = TIME_OUT)
    response = json.loads(result.content.decode("utf-8").replace("'", '"'))
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

def get_provider(key):
    url = URL_PROVIDER
    if key is not None:
        url = url + key
    #params = {'year': year, 'author': author}
    #r = requests.get(url, params=params)
    result = requests.get(url, timeout = TIME_OUT)
    response = json.loads(result.content.decode("utf-8").replace("'", '"'))
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
    return result.json()

def update_create_provider(object):
    if not 'id' in object:
        object["id"] = ""
    if object["id"] == "":
        #Create
        del object["id"]
    headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    url = URL_PROVIDER
    result = requests.post(url, data=json.dumps(object), timeout = TIME_OUT, headers = headers )
    return json.loads(result.content.decode("utf-8"))
