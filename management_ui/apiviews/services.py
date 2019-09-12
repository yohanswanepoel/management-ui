import requests

#URL_RELIANTPARTIES = "http://polyglot-example-rp-myproject.192.168.99.103.nip.io/api/v1/reliantparties/"
URL_RELIANTPARTIES = "http://0.0.0.0:7080/api/v1/reliantparties/"
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
    result = requests.get(url)
    response = result.json()
    return response

def get_parties(status):
    url = URL_RELIANTPARTIES
    if status is not None:
        url = url + "?status=" + status
    #params = {'year': year, 'author': author}
    #r = requests.get(url, params=params)
    result = requests.get(url)
    response = result.json()
    return response

def get_party(key):
    url = URL_RELIANTPARTIES
    if key is not None:
        url = url + key
    #params = {'year': year, 'author': author}
    #r = requests.get(url, params=params)
    result = requests.get(url)
    response = result.json()
    return response