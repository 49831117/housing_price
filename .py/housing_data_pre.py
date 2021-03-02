import os
import pandas as pd
import numpy as np



df = pd.read_csv(".py\\all_109.csv")
df_zip = pd.read_csv(".py\\housing_zipcode.csv")

data_zip = []
data_set = df_zip.city_country
for i in df["土地區段位置建物區段門牌"]:
    if i[:6] in data_set:
        index = df_zip.city_country.index(i[:6])
        data_zip.append(df_zip.zip_code[index])
    else:
        data_zip.append("")

df["zip_code"] = data_zip

df['單價元平方公尺'] = df['單價元平方公尺'].astype(float)
df['單價元坪'] = df['單價元平方公尺'] * 3.30579

df = df[df['備註'].isnull()]

# print(df.columns) # 觀察屬性

'''
將郵遞區號(zip_code)、單位坪數價錢(per_price)抽出建立 price.csv

price = pd.read_csv(".py\\price.csv")

df_p_median = price.groupby(price.zip_code)[['per_price']].median()
df_p_median.to_csv("price_median.csv")

再匯入 housing_zipcode，對照縣市、鄉鎮市區。
'''

df.to_csv("h_109_zip.csv", encoding = "utf-8-sig")


