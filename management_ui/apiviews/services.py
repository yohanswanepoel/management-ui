import requests

URL_RELIANTPARTIES = "http://polyglot-example-rp-myproject.192.168.99.103.nip.io/api/v1/reliantparties/"
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
    r = requests.get(url)
    response = r.json()
    print (response)
    return response