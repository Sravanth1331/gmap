import folium
import pandas

data=pandas.read_csv("Volcanoes.txt")

lst=list(data["LAT"])
lst1=list(data["LON"])
elev=list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation < 2000:
        return 'orange'
    else:
        return 'red'



map=folium.Map(location=[38.58,-92.36],titles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt,ln,ele in zip(lst,lst1,elev):
    fgv.add_child(folium.Marker(location=[lt,ln], popup=str(ele)+"m",icon=folium.Icon(color=color_producer(ele))))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json",'r', encoding='utf-8-sig'). read() , 
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] <10000000
else 'orange' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")