import pandas as pd
import numpy as np
import geopandas as gp
import matplotlib.pyplot as plt



data = pd.read_csv('.py\\price_median.csv')
twd97_geod = gp.GeoDataFrame.from_file('TWD97\TOWN_MOI_1091016.shp')
# print(data.info())
# print(twd97_geod.info())
twd97_geod["city_town"] = twd97_geod["COUNTYNAME"]+twd97_geod["TOWNNAME"]
# twd97_geod.plot()

data_geod = gp.GeoDataFrame(data)
da_merge = twd97_geod.merge(data_geod, on = 'city_town', how = 'left')
da_merge.plot('per_price', k = 100 , cmap = "hot", scheme = 'percentiles', alpha= 1, figsize = (15, 15), legend = True)

plt.title('2020 Median', fontsize=15)

plt.show()

