
'''
1. 指定查詢年分
2. real_estate_crawler(year, season) 爬取資料並儲存、解壓縮
3. 合併成一份 df
4. 將 df 存成 .csv，檔名為 f"all_{start_y}_to_{end_y}.csv"
'''

import requests
import os
import zipfile
import pandas as pd


# 爬取資料
def real_estate_crawler(year, season):
    """要下載檔案的民國年+季，下載 zip 後解壓縮並存入指定資料夾"""
    if year > 1000:
        year -= 1911
    # download real estate zip content (eg.https://plvr.land.moi.gov.tw/DownloadSeason?season=109S4&type=zip&fileName=lvr_landcsv.zip)
    res = requests.get("https://plvr.land.moi.gov.tw//DownloadSeason?season="+str(year)+"S"+str(season)+"&type=zip&fileName=lvr_landcsv.zip")
    
    # save content to file
    fname = 'raw_data/'+str(year)+str(season)+'.zip'
    open(fname, 'wb').write(res.content)

    # make additional folder for files to extract
    folder = 'raw_data/real_estate' + str(year) + str(season)
    if not os.path.isdir(folder):
        os.mkdir(folder)

    # extract files to the folder
    with zipfile.ZipFile(fname, 'r') as zip_ref:
        zip_ref.extractall(folder)

# 批次下載
start_y = int(input("輸入查詢起始年份：民國 "))
end_y = int(input("輸入查詢結束年份：民國 "))

for year in range(start_y, end_y+1):
    for season in range(1,5):
        print(year, season)
        real_estate_crawler(year, season)


# 歷年資料夾
# 指定路徑
path = "raw_data" 

# 可改 for 迴圈批次處理個年分
start_yq = int(str(start_y)+"0")
end_yq = int(str(end_y+1)+"0")
dirs = [d for d in os.listdir(path) if d[:4] == 'real' and end_yq>int(d[-4:])> start_yq ]


dfs = []

alphs = "a b c d e f g h i j k m n o p q t u v w x z".upper().split()
for d in dirs:
    for alph in alphs:
        path = os.path.join('raw_data', d,f'{alph}_lvr_land_a.csv')
        print("Reading:", path)
        df = pd.read_csv(path)
        df['local'] = alph # 新增「城市代碼」欄位
        dfs.append(df.iloc[1:])


df = pd.concat(dfs)
print("\n第一列資料：\n", df.iloc[1])
print(df.info())

df.to_csv("raw_data\\all_109_to_109.csv", encoding="utf-8-sig")
