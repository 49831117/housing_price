# Housing Price

## 起源
- [內政部 實價登陸 Open Data](https://plvr.land.moi.gov.tw/DownloadOpenData)
- 觀察到某地區房價飆漲、薪水不漲的現象，思考是否各地皆如此。以此為出發點，期望可以透過此專案實踐將過去所學背景與程式語言結合，產出有用的數據分析資訊，提供未來多一個買房思考方向。

## 使用到的套件
1. ~~ArcGIS `pip install arcgis`~~
2. zipfile `pip install zipfile-deflate64` 
    > Released: Feb 25, 2021
3. matplotlib `pip install matplotlib`
4. pandas `pip install pandas`
5. seaborn `pip install seaborn`
6. plotly `pip install plotly` 
7. sklearn


## 步驟
1. 內政部實價登陸網站撈取資料
2. 資料整理與觀察
    1. 觀察資料：
       1. 檔案名稱


            |檔案名稱|交易類型|
            |:----:|:----:|
            |x_lvr_land_a|房屋買賣交易|
            |x_lvr_land_b|新成屋交易|
            |x_lvr_land_c|租房交易|


       2. 屬性名稱 
   
   
            ```python 
             # x_lvr_land_a 的屬性名稱
             city_a_column_name = ['鄉鎮市區', '交易標的', '土地區段位置建物區段門牌', '土地移轉總面積平方公尺', '都市土地使用分區', '非都市土地使用分區', '非都市土地使用編定', '交易年月日', '交易筆棟數', '移轉層次', '總樓層數', '建物型態', '主要用途', '主要建材', '建築完成年月', '建物移轉總面積平方公尺', '建物現況格局-房', '建物現況格局-廳', '建物現況格局-衛', '建物現況格局-隔間', '有無管理組織', '總價元', '單價元平方公尺', '車位類別', '車位移轉總面積(平方公尺)', '車位總價元', '備註', '編號', '主建物面積', '附屬建物面積', '陽台面積', '電梯']
        
             # x_lvr_land_b 的屬性名稱
             city_b_column_name = ['鄉鎮市區', '交易標的', '土地區段位置建物區段門牌', '土地移轉總面積平方公尺', '都市土地使用分區', '非都市土地使用分區', '非都市土地使用編定', '交易年月日', '交易筆棟數', '移轉層次', '總樓層數', '建物型態', '主要用途', '主要建材', '建築完成年月', '建物移轉總面積平方公尺', '建物現況格局-房', '建物現況格局-廳', '建物現況格局-衛', '建物現況格局-隔間', '有無管理組織', '總價元', '單價元平方公尺', '車位類別', '車位移轉總面積平方公尺', '車位總價元', '備註', '編號']

             # x_lvr_land_c 的屬性名稱
             city_c_column_name = ['鄉鎮市區', '交易標的', '土地區段位置建物區段門牌', '土地面積平方公尺', '都市土地使用分區', '非都市土地使用分區', '非都市土地使用編定', '租賃年月日', '租賃筆棟數', '租賃層次', '總樓層數', '建物型態', '主要用途', '主要建材', '建築完成年月', '建物總面積平方公尺', '建物現況格局-房', '建物現況格局-廳', '建物現況格局-衛', '建物現況格局-隔間', '有無管理組織', '有無附傢俱', '總額元', '單價元平方公尺', '車位類別', '車位面積平方公尺', '車位總額元', '備註', '編號']

            ```

    2. 縣市代碼：

        |縣市|代碼|縣市|代碼|縣市|代碼|縣市|代碼|縣市|代碼|
        |:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
        |臺北市|A|臺中市|B|基隆市|C|臺南市|D|高雄市|E|
        |新北市|F|宜蘭縣|G|桃園縣|H|嘉義市|I|新竹縣|J|
        |苗栗縣|K|~~臺中縣~~|~~L~~|南投縣|M|彰化縣|N|新竹市|O|
        |雲林縣|P|嘉義縣|Q|~~臺南縣~~|~~R~~|~~高雄縣~~|~~S~~|屏東縣|T|
        |花蓮縣|U|臺東縣|V|金門縣|W|澎湖縣|X|~~陽明山~~|~~Y~~|
        |連江縣|Z|


3. 資料分析
   1. 將 `1061` 至 `1094` 各縣市資料合併後得：
   ```python
    Int64Index: 1339590 entries, 1 to 33
    Data columns (total 34 columns):
    #   Column         Non-Null Count    Dtype      
    ---  ------         --------------    -----      
    0   鄉鎮市區           1339507 non-null  object 
    1   交易標的           1339590 non-null  object
    2   土地區段位置建物區段門牌   1339565 non-null  object
    3   土地移轉總面積平方公尺    1339590 non-null  object
    4   都市土地使用分區       1067866 non-null  object
    5   非都市土地使用分區      255378 non-null   object
    6   非都市土地使用編定      254410 non-null   object
    7   交易年月日          1339590 non-null  object
    8   交易筆棟數          1339590 non-null  object
    9   移轉層次           985894 non-null   object
    10  總樓層數           984834 non-null   object
    11  建物型態           1339590 non-null  object
    12  主要用途           964280 non-null   object
    13  主要建材           986102 non-null   object
    14  建築完成年月         965641 non-null   object
    15  建物移轉總面積平方公尺    1339590 non-null  object
    16  建物現況格局-房       1339590 non-null  object
    17  建物現況格局-廳       1339590 non-null  object
    18  建物現況格局-衛       1339590 non-null  object
    19  建物現況格局-隔間      1339590 non-null  object
    20  有無管理組織         1339590 non-null  object
    21  總價元            1339590 non-null  object
    22  單價元平方公尺        1313168 non-null  object
    23  車位類別           432942 non-null   object
    24  車位移轉總面積平方公尺    1112061 non-null  object
    25  車位總價元          1339590 non-null  object
    26  備註             418373 non-null   object
    27  編號             1339590 non-null  object
    28  Q              1339590 non-null  object
    29  車位移轉總面積(平方公尺)  227529 non-null   object
    30  主建物面積          227529 non-null   float64
    31  附屬建物面積         227529 non-null   float64
    32  陽台面積           227529 non-null   float64
    33  電梯             165045 non-null   object
    dtypes: float64(3), object(31)
    memory usage: 357.7+ MB
    None
   ```
   2. 內政部的實價登錄文件 `DataFrame` `concat` 後要 `encoding = utf-16` 才能讀取 `.csv`，但無法 `sep=","`。
      > try `utf-8-sig`
   3. 觀察到各縣市 raw data 中`鄉鎮市區`欄位有各種小問題，如新竹市的`鄉鎮市區`資料中只有`新竹市`、`台南市`及數個縣市的`鄉鎮市區`資料中有 `NaN`，故將資料丟入 Google，重新取得地理資訊。
      > [google-refine](https://code.google.com/archive/p/google-refine/)
   4. `TWD97` 的 `.shp` 範圍太大
      1. [MyGeodata Converter](https://mygeodata.cloud/conversion)：觀察 `.shp` 中描述的實際範圍
      2. 
      
         ![TWD97](https://github.com/49831117/housing_price/blob/master/image/geodataconv.jpg "TWD97")
    
4. 視覺化
