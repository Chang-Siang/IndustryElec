# Data Description

## 用電資料

- [taiwan_industrial_electricity_20160101_20190930.csv](taiwan_industrial_electricity_20160101_20190930.csv) 為 BDRC 實驗室從[台灣電力公司官方網站](https://www.taipower.com.tw/tc/page.aspx?mid=96)撈取的原始用電資料，共 1,461 筆，欄位名稱為中文
- [taiwan_industrial_electricity_processed_20160101_20190930.csv](taiwan_industrial_electricity_processed_20160101_20190930.csv) 為 BDRC 實驗室對上述資料進行加工後的版本，追加部分日期相關屬性，共 1,461 筆，欄位名稱為英文

  | 欄位名稱              | 欄位說明                                                    |
  | --------------------- | ----------------------------------------------------------- |
  | date                  | 資料日期，單位：日                                          |
  | power_consumption     | 工業用電，單位：百萬度                                      |
  | peak_load             | 尖峰負載，單位：MW                                          |
  | peak_load_shift7      | 7 天後的尖峰負載，單位：MW                                  |
  | temp_taipei           | 氣溫，取自中央氣象局觀測資料站                              |
  | temp_taipei_shift7    | 7 天後的 Temp_Taipei                                        |
  | week                  | 星期幾                                                      |
  | week_update           | 星期幾，將國定假日調整為 6 ~ 7，將補班日調整為 1 ~ 5 的版本 |
  | week_update_shift7    | 7 天後的 week_update                                        |
  | is_holiday            | 是否為假日或國定假日                                        |
  | is_holiday_shift7     | 7 天後的 isHoliday                                          |
  | day_of_year           | 日期參數，表示一年中的第幾天                                |
  | transform_day_of_year | 日期參數，表示一年中的第幾天，頭尾連續版本                  |

## 氣象觀測資料

- [central_weather_bureau_observation_daily_by_region_20160101_20191031.csv](central_weather_bureau_observation_daily_by_region_20160101_20191031.csv) 為[中央氣象局觀測資料查詢系統](https://e-service.cwb.gov.tw/HistoryDataQuery/)保存的氣象觀測資料，包含氣溫、相對濕度、風速、風向、降水量等資訊
- 本次取用其中的氣溫資料，輔助用電預測
