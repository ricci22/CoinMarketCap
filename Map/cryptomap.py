#This example uses Python 2.7 and the python-request library.
#Response is single-quoted

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '5c52d8ee-6eb1-4b9b-bccd-cf796d1141fd',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url)
    data = json.loads(response.text)

    #write output into cryptomap.json file
    with open("cryptomap.txt", "w") as external_file:
        #print(data, file=external_file)
        external_file.write(json.dumps(data, indent=4, sort_keys=True))
        external_file.close()
    
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)