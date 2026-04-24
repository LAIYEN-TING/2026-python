# Week 05 作業：1114405035

本目錄包含 Week 05 的五題 UVA 解題程式、簡單版本、測試與紀錄。

## 目錄結構

- `uva10041.py` - UVA 10041：Vito 的親戚距離最小化
- `uva10041_easy.py` - UVA 10041 簡易版本
- `uva10050.py` - UVA 10050：Hartals 罷會天數計算
- `uva10050_easy.py` - UVA 10050 簡易版本
- `uva10055.py` - UVA 10055：函數複合增減性查詢
- `uva10055_easy.py` - UVA 10055 簡易版本
- `uva10056.py` - UVA 10056：輪流擲骰子勝率計算
- `uva10056_easy.py` - UVA 10056 簡易版本
- `uva10057.py` - UVA 10057：密碼 A 的最小距離總和
- `uva10057_easy.py` - UVA 10057 簡易版本
- `tests/test_week05.py` - 週次測試檔
- `TEST_CASES.md` - 測試案例說明
- `TEST_LOG.md` - 測試執行日誌
- `AI_USAGE.md` - AI 使用紀錄
- `assets/` - 補充資料或截圖（可空）

## 執行方式

### UVA 程式
```bash
python uva10041.py < input.txt
python uva10050.py < input.txt
python uva10055.py < input.txt
python uva10056.py < input.txt
python uva10057.py < input.txt
```

### 單元測試
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## 注意事項

- 本週作業放在 `weeks/week-05/solutions/1114405035/`
- 已實作五題 UVA 讀入/輸出處理與測試
- 同時包含簡單版本 `*_easy.py`
