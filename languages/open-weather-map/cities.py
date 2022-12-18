"""
Cities
"""

import requests
import unidecode

CITIES_URL = "https://raw.githubusercontent.com/hieudoanm/tablebase/master/json/world/cities.json"

response = requests.get(CITIES_URL, timeout= 10)
response_json = response.json()
names = list(map(lambda city: city.get("name"), response_json))
unidecoded_names = list(map(unidecode.unidecode, names))
unique_unidecoded_names = list(set(unidecoded_names))
unique_unidecoded_names.sort()

print(len(unique_unidecoded_names), unique_unidecoded_names)
