'''
觀察 TWD97/TOWN_MOI_1091016.shp 的資料
'''
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# 讀取檔案
gdftwd = gpd.read_file('TWD97\\TOWN_MOI_1091016.shp')
# gdftwd["city_country"] = gdftwd["COUNTYNAME"]+gdftwd["TOWNNAME"]
# print("\n各欄位名稱：\n", gdftwd.columns.to_list(), f"\n欄位個數：{len(gdftwd.columns.to_list())}", "\n")
# print(gdftwd.iloc[1])



subset = gdftwd['TOWNNAME'].to_list()

print("\n各鄉鎮市區名稱：\n", subset, f"\n鄉鎮市區總數：{len(subset)}", "\n")
# print(subset)
# check = "東沙鄉"
# print(check in subset)

# subset1 = gdftwd["COUNTYNAME"]
# sub1_list = subset1.to_list()
# list = []
# for i in sub1_list:
#     if i not in list:
#         list.append(i)
# print(list, len(list))


# sample = gdf_twd.sort_values(by='COUNTYID')
# print(sample.COUNTYID)

# sample.plot()
# sample.plot(column='RAILNAME' )
