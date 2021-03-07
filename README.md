- [Housing Price](#housing-price)
  - [參考資料](#參考資料)
  - [起源](#起源)
  - [使用到的套件 & 軟體](#使用到的套件--軟體)
  - [步驟](#步驟)
  - [Test](#test)
    - [篩選資料前提](#篩選資料前提)
    - [Test - 各鄉鎮市區房價中位數](#test---各鄉鎮市區房價中位數)
    - [遇到的問題](#遇到的問題)
  - [統計結果](#統計結果)
    - [問題修正](#問題修正)
    - [表格與視覺化](#表格與視覺化)

# Housing Price
## 參考資料
- [地籍圖資網路便民服務系統](https://easymap.land.moi.gov.tw/Index)
- [不動產成交案件實際資訊資料供應系統](https://plvr.land.moi.gov.tw/DownloadOpenData)
- [Lin-Sheng Lee (2014) 房屋價格決定因素之探討：空間與多層次分析之應用](https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/login?o=dnclcdr&s=id=%22102NTU05389031%22.&searchmode=basic)

## 起源
- 觀察到某地區房價飆漲、薪水不漲的現象，思考是否各地皆如此。以此為出發點，期望可以透過此專案實踐將過去所學背景與程式語言結合，產出有用的數據分析資訊，提供未來多一個買房思考方向。

## 使用到的套件 & 軟體
1. zipfile `pip install zipfile-deflate64` 
    > Released: Feb 25, 2021
2. matplotlib `pip install matplotlib`
3. pandas `pip install pandas`
4. geopandas `pip install geopandas`
5. Excel
6. Power BI



## 步驟
1. [內政部實價登錄網站](https://plvr.land.moi.gov.tw/DownloadOpenData)撈取資料
2. 資料整理與觀察
    1. 觀察資料：
         - 檔案名稱


            |檔案名稱|交易類型|
            |:----:|:----:|
            |x_lvr_land_a|房屋買賣交易|
            |x_lvr_land_b|新成屋交易|
            |x_lvr_land_c|租房交易|


         - [raw data - 屬性名稱](https://github.com/49831117/housing_price/blob/master/raw_data.md)


    1. 縣市代碼：

        |縣市|代碼|縣市|代碼|縣市|代碼|縣市|代碼|縣市|代碼|
        |:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
        |臺北市|A|臺中市|B|基隆市|C|臺南市|D|高雄市|E|
        |新北市|F|宜蘭縣|G|桃園縣|H|嘉義市|I|新竹縣|J|
        |苗栗縣|K|~~臺中縣~~|~~L~~|南投縣|M|彰化縣|N|新竹市|O|
        |雲林縣|P|嘉義縣|Q|~~臺南縣~~|~~R~~|~~高雄縣~~|~~S~~|屏東縣|T|
        |花蓮縣|U|臺東縣|V|金門縣|W|澎湖縣|X|~~陽明山~~|~~Y~~|
        |連江縣|Z|


3. 資料分析
   1. 將 `1061` 至 `1094` 各縣市資料合併後得 1,339,590 過於龐大，如下，故決定先按年處理。
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
   1. 內政部的實價登錄文件以 `DataFrame` 形式 `concat` 後，必須要 `encoding = 'utf-16'` 才能讀取 `.csv`，但同時卻無法有效地 `sep=','`。
      > 解決方法：try `encoding = 'utf-8-sig'`
   2. 觀察到各縣市 raw data 中`鄉鎮市區`欄位有各種小問題，如新竹市的`鄉鎮市區`資料中只有`新竹市`，又如`台南市`及數個縣市的`鄉鎮市區`資料中有 `NaN`，故將資料丟入 Google，重新取得地理資訊。
      > [google-refine](https://code.google.com/archive/p/google-refine/)
      >
      > [中華郵政 - 3+3郵遞區號應用系統](https://www.post.gov.tw/post/internet/Download/index.jsp?ID=220306)
         > 轉完得到 `dbf` 檔
         >
         > 特別注意`鄉鎮市區`名重複：南區、信義區、東區、北區、中正區、中山區、大安區
   
   3. [政府資料開放平臺](https://data.gov.tw/dataset/7442)中 `TWD97` 的 `.shp` 對於此討論主題而言範圍太大。
      > 原因：太平島（位於南沙群島，隸屬於高雄市旗津區中興里）
      - 透過 [MyGeodata Converter](https://mygeodata.cloud/conversion)：觀察 `.shp` 中描述的實際範圍
           > ![TWD97](https://github.com/49831117/housing_price/blob/master/image/geodataconv.jpg "TWD97")
   4. [中華郵政](https://www.post.gov.tw/post/download/1050812_%E8%A1%8C%E6%94%BF%E5%8D%80%E7%B6%93%E7%B7%AF%E5%BA%A6%28toPost%29.xml)各鄉鎮市區郵遞區號所列舉的鄉鎮市區與 `TWD97` 中的鄉鎮市區差異：
      - `TWD97` 的鄉鎮市區中尚少了以下三筆鄉鎮市區：
        - 宜蘭縣釣魚臺列嶼  290
        - 海南東沙	817
        - 海南南沙  819

    
4. 視覺化處理
   - 目前主要透過 `geopandas` 結合 `matplotlib` 呈現。
   - 未來會透過 Power BI / Tableau 呈現。

----

## Test

### 篩選資料前提
  - 資料只考慮「**含有建物**的交易」且「交易日期確實為**民國 109 年**」的資料。
  - 因為此次試跑數據統整是取中位數，考慮到民國 109 年交易熱度，將單位地區交易筆數 < 3 筆的鄉鎮市區資料刪除，以免受極值影響。

### Test - 各鄉鎮市區房價中位數
[Test - 各鄉鎮市區房價中位數](https://github.com/49831117/housing_price/blob/master/.py/first.md)

![2020median](https://github.com/49831117/housing_price/blob/master/image/2020median.jpg "2020median")

### 遇到的問題
   1. 統計資料與圖資 `merge` 時是根據郵遞區號，但 `.shp` 中資料單位為鄉鎮市區，其中有些鄉鎮市區共用相同的郵遞區號（如：嘉義市東區、嘉義市西區皆為 600），故匯出的圖檔與資料會有錯誤。
      > 解決方式：重新做資料清洗，改以擷取地址，而非以郵遞區號連結地理資訊與數據資料。
   2. 地址無詳細含有縣市與鄉鎮市區（即僅有路名，或是鄉鎮市區名稱錯誤）者直接剃除，共剃除約一萬筆左右（大約佔符合前提資料量的 6 %），可能會造成小地區統計資訊偏差。

----

## 統計結果

### 問題修正
- 解決鄉鎮市區同名的問題：
  - 撈取資料存取同時即新增縣市代碼欄位做為辨識。
- 數個鄉鎮市區共用相同郵遞區號，raw data 的欄位亦無區分。
  > 如：嘉義市不論東區或西區，raw data 的資料皆為「嘉義市」，若未將其區分，繪得的圖會如第一次測試一樣，嘉義市部分沒有資料。
    - 地址與地段前處理：
       - 考量大多縣市 raw data 有準確率很高的鄉鎮市區資料，故需特別花時間處理的資料為「新竹市」、「嘉義市」。
       - 建立路名、路段對照表。
          - 新竹市要細分成：北區、東區、香山區
          - 嘉義市要細分成：東區、西區
    - 大多數可透過鄉鎮市區 + 縣市代碼對照完成，但有少數型態需要特別注意：
       - 「新竹市新竹市」、「新竹市新竹市新竹市」、「xx里oo鄰」等等，需先去掉
       - 地段名部分也要注意，尤其像是「中山段一小段」與「中山一小段」名稱細微的差異。
> 按照上述步驟，可以將實際交易日為民國 109 年共 `392,237` 筆資料前處理至僅有 `79` 筆資料無鄉鎮市區。
- 資料分析：
   - 因聚焦在各鄉鎮市區建物相關交易中每坪單價數據統計，故在有效的 `392,158` 筆資料中，篩選出「建物」、「房地(土地+建物)」、「房地(土地+建物)+車位」三種交易標的，共計 `188,325` 筆。
### 表格與視覺化

[各鄉鎮市區中位數統計](https://github.com/49831117/housing_price/blob/master/.py/%E5%90%84%E9%84%89%E9%8E%AE%E5%B8%82%E5%8D%80%E4%B8%AD%E4%BD%8D%E6%95%B8%E7%B5%B1%E8%A8%88.md)

民國 109 年各鄉鎮市區單價（元/坪）分布圖
![2020median_1](https://github.com/49831117/housing_price/blob/master/image/2020median_1.jpg "2020median_1")

民國 109 年各縣市單價（元/坪）長條圖
![109年各縣市單價中位數(建物相關)](https://github.com/49831117/housing_price/blob/master/image/109年各縣市單價中位數(建物相關).jpg "109年各縣市單價中位數(建物相關)")

民國 109 年各縣市單價（元/坪）長條圖
![109年各縣市單價平均數(建物相關)](https://github.com/49831117/housing_price/blob/master/image/109年各縣市單價平均數(建物相關).jpg "109年各縣市單價平均數(建物相關)")

民國 109 年各縣市單價（元/坪）長條圖
![109年各縣市單價標準差(建物相關)](https://github.com/49831117/housing_price/blob/master/image/109年各縣市單價標準差(建物相關).jpg "109年各縣市單價標準差(建物相關)")