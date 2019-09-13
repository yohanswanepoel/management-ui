import requests

URL_RELIANTPARTIES = "http://polyglot-demo-rp-myproject.192.168.99.104.nip.io/api/v1/reliantparties/"
TIME_OUT = 2
#URL_RELIANTPARTIES = "http://0.0.0.0:7080/api/v1/reliantparties/"
def get_count_reliant_parties(status):
    # Registered
    # Test
    # Active
    # Down
    # Retired
    # Need one for active / not - active
    url = URL_RELIANTPARTIES + "count/"
    if status is not None:
        url = url + "?status=" + status
    #params = {'year': year, 'author': author}
    #r = requests.get(url, params=params)
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
    if object["id"] is None:
        #Create
        url = URL_RELIANTPARTIES
        result = requests.post(url, data=object, timeout = TIME_OUT)
    else:
        #Update
        url = URL_RELIANTPARTIES + object["id"] + "/"
        result = requests.put(url, data=object, timeout = TIME_OUT)
    return object
