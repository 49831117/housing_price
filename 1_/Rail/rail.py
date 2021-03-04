import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

gdf_Rail = gpd.read_file('Rail\\RAIL_1100104.shp',encoding='utf-8')
# print(gdf_Rail)
subset = gdf_Rail['RAILNAME']
sample = gdf_Rail.sort_values(by='MDATE')
sample.plot()
sample.plot(column='RAILNAME')
plt.show()