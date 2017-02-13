import json
from urllib.request import urlopen
def getCountry(ipAddress):
    response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    print(responseJson)
    return responseJson.get("country_code")
print(getCountry("121.97.110.145"))
