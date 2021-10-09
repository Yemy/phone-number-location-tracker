import geocoder
import folium


g = geocoder.ip('me')

myaddr = g.latlng

my_map1 = folium.Map(location=myaddr, zoom_start=12)

my_map1.save('my_map.html')
