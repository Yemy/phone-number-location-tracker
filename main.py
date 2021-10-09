import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from opencage.geocoder import OpenCageGeocode
import folium


number = input("Enter Phone Number:")
key = 'c25c2569149e4393a9f5741da4cace1a'

country = phonenumbers.parse(number, "CH")
print("Country: " + str(geocoder.description_for_number(country, "en")))

your_location = geocoder.description_for_number(country, "en")

service_provider = phonenumbers.parse(number, "RO")
print("Service Provider: " + str(carrier.name_for_number(service_provider, "en")))

gb_number = phonenumbers.parse(number, "GB")
print("Continent/Capital City: " + str(timezone.time_zones_for_number(gb_number)))

# extract phone numbers from text
# text = "Call me at 510-748-8230 if it's before 9:30, or on 703-4800500 after 10am. or 0919575929"
# for match in phonenumbers.PhoneNumberMatcher(text, "US"):
# 	print(match)

# for match in phonenumbers.PhoneNumberMatcher(text, "US"):
#     print(phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164))


geocoder = OpenCageGeocode(key)
query = str(your_location)
results = geocoder.geocode(query)

# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)


myMap = folium.Map(location=[lat, lng], zoom_start = 9)
folium.Marker([lat, lng], popup=your_location).add_to((myMap))

myMap.save("mylocation.html")
