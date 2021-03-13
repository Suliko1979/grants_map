import folium
from folium import plugins
import pandas as pd
import os

m = folium.Map(location=[42, 74], zoom_start=4)

kyrgyzstanData = os.path.join('/Users/Admin/Desktop/Data Vis/kgz.geojson')
folium.GeoJson(kyrgyzstanData, name='kyrgyzstan').add_to(m)

mcg = folium.plugins.MarkerCluster(control=True)
m.add_child(mcg)

g1 = folium.plugins.FeatureGroupSubGroup(mcg, 'Chui')
m.add_child(g1)

g2 = folium.plugins.FeatureGroupSubGroup(mcg, 'Issyk Kul')
m.add_child(g2)

g3 = folium.plugins.FeatureGroupSubGroup(mcg, 'Osh')
m.add_child(g3)

g4 = folium.plugins.FeatureGroupSubGroup(mcg, 'JA')
m.add_child(g4)

g5 = folium.plugins.FeatureGroupSubGroup(mcg, 'Naryn')
m.add_child(g5)

g6 = folium.plugins.FeatureGroupSubGroup(mcg, 'Talas')
m.add_child(g6)

data = pd.read_excel('/Users/Admin/Desktop/Data Vis/chui.xlsx')
for row in data.itertuples():
    folium.Marker(location=[row.Lat, row.Long], popup=row.City).add_to(g1)

data = pd.read_excel('/Users/Admin/Desktop/Data Vis/ik.xlsx')
for row in data.itertuples():
    folium.Marker(location=[row.Lat, row.Long], popup=row.City).add_to(g2)

data = pd.read_excel('/Users/Admin/Desktop/Data Vis/osh.xlsx')
for row in data.itertuples():
    folium.Marker(location=[row.Lat, row.Long], popup=row.City).add_to(g3)

data = pd.read_excel('/Users/Admin/Desktop/Data Vis/ja.xlsx')
for row in data.itertuples():
    folium.Marker(location=[row.Lat, row.Long], popup=row.City).add_to(g4)

data = pd.read_excel('/Users/Admin/Desktop/Data Vis/jaa.xlsx')
for row in data.itertuples():
    folium.Marker(location=[row.Lat, row.Long], popup=row.City).add_to(g5)

data = pd.read_excel('/Users/Admin/Desktop/Data Vis/tal.xlsx')
for row in data.itertuples():
    folium.Marker(location=[row.Lat, row.Long], icon=folium.features.CustomIcon('/Users/Admin/Desktop/Data Vis/pc.png'),
                  popup=row.City).add_to(g6)

folium.LayerControl(collapsed=True).add_to(m)

m.save('/Users/Admin/Desktop/Data Vis/final1.html')
