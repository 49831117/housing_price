'''
觀察 TWD97/TOWN_MOI_1091016.shp 的資料
'''
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# 讀取檔案
gdftwd = gpd.read_file('TWD97\\TOWN_MOI_1091016.shp')
gdftwd["city_country"] = gdftwd["COUNTYNAME"]+gdftwd["TOWNNAME"]
check_city_country = gdftwd.city_country
check_city_country.to_csv("TWD97\\check_name_list.csv", encoding = 'utf-8-sig')


# subset = gdftwd['TOWNNAME'].to_list()

# print("\n各鄉鎮市區名稱：\n", subset, f"\n鄉鎮市區總數：{len(subset)}", "\n")
# print(subset)
# check = "東沙鄉"
# print(check in subset)




# sample = gdf_twd.sort_values(by='COUNTYID')
# print(sample.COUNTYID)

# sample.plot()
# sample.plot(column='RAILNAME' )
