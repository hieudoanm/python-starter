"""
GeoText
"""

from geotext import GeoText

MESSAGE_1 = "Ho Chi Minh"
places = GeoText(MESSAGE_1)
print(places.cities)

MESSAGE_2 = "Frankfurt am Main"
places = GeoText(MESSAGE_2)
print(places.cities)

MESSAGE_3 = "Paris"
places = GeoText(MESSAGE_3)
print(places.cities)

MESSAGE_3 = "Hanoi"
places = GeoText(MESSAGE_3)
print(places.cities)

MESSAGE_3 = "Hanoi"
places = GeoText(MESSAGE_3)
print(places.cities)
