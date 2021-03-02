import requests
import os
import zipfile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import geoplot as gplt



# 爬取資料
def real_estate_crawler(year, season):
    """要下載檔案的民國年+季，下載 zip 後解壓縮並存入指定資料夾"""
    if year > 1000:
        year -= 1911
    # download real estate zip content (eg.https://plvr.land.moi.gov.tw/DownloadSeason?season=109S4&type=zip&fileName=lvr_landcsv.zip)
    res = requests.get("https://plvr.land.moi.gov.tw//DownloadSeason?season="+str(year)+"S"+str(season)+"&type=zip&fileName=lvr_landcsv.zip")
    
    # save content to file
    fname = 'data/'+str(year)+str(season)+'.zip'
    open(fname, 'wb').write(res.content)

    # make additional folder for files to extract
    folder = 'data/real_estate' + str(year) + str(season)
    if not os.path.isdir(folder):
        os.mkdir(folder)

    # extract files to the folder
    with zipfile.ZipFile(fname, 'r') as zip_ref:
        zip_ref.extractall(folder)

'''
單季下載
real_estate_crawler(101, 3)
'''

# 批次下載
start_y = int(input("輸入查詢起始年份：民國 "))
end_y = int(input("輸入查詢結束年份：民國 ") + 1
for year in range(start_y, end_y ):
    for season in range(1,5):
        print(year, season)
        real_estate_crawler(year, season)




# 歷年資料夾
# 指定路徑
path = "data" 
# 解壓縮後的資料夾列表



# dirs = [資料夾名稱前四個字為 real 且 109 年的資料] 
# 可改 for 迴圈批次處理個年分
dirs = [d for d in os.listdir(path) if d[:4] == 'real' and 1100>int(d[-4:])> 1090 ]

# print(len(dirs)) # 對照用

dfs = []
alphs = "a b c d e f g h i j k m n o p q t u v w x z".upper().split()
for d in dirs:
    # print("前四個字為 real 的資料夾名稱:", d) # 檢查用
    # 依序將各資料夾代入路徑，讀取 csv 檔
    for alph in alphs:
        df = pd.read_csv(os.path.join('data', d,f'{alph}_lvr_land_a.csv'))
        df['Q'] = d[-1] # 新增「季」欄位，辨識查找用
        dfs.append(df.iloc[1:])

'''
path = "data" 
dirs = [d for d in os.listdir(path) if d[:4] == 'real' and int(d[-4:])>100] # dirs = [資料夾名稱前四個字為 real 且 10601 之後的資料] 
dfs = []
for d in dirs:
    df = pd.read_csv(os.path.join('data', d,'a_lvr_land_a.csv'))
    df['Q'] = d[-1] # 新增「季」欄位
    dfs.append(df.iloc[1:])
'''

df = pd.concat(dfs)
print(df.iloc[1])
df1 = df.duplicated()
print(df1.index(True))

# 觀察資料
# want_know_list = df[["編號", "鄉鎮市區", "土地區段位置建物區段門牌"]]
# print(want_know_list.info()) 

df.to_csv("all_109.csv", encoding="utf-8-sig")
