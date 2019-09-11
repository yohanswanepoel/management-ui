import requests

def get_count_reliant_parties():
    url = 'http://127.0.0.1:8000/api/v1/reliantparties/count' 
    #params = {'year': year, 'author': author}
    r = requests.get(url, params=params)
    parties = r.json()
    parties_list = {'reliant_parties':parties['results']}
    return parties_list