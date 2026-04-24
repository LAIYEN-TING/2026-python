# Week 07 作業：1114405035

本目錄包含 Week 07 的五題 UVA 解題程式與測試。

## 目錄結構

- `uva10062.py` - UVA 10062：乳牛排序
- `uva10062_easy.py` - UVA 10062 簡易版本
- `uva10071.py` - UVA 10071：六元組求和
- `uva10071_easy.py` - UVA 10071 簡易版本
- `uva10093.py` - UVA 10093：炮兵部署最大數量
- `uva10093_easy.py` - UVA 10093 簡易版本
- `uva10101.py` - UVA 10101：木棒等式修正
- `uva10101_easy.py` - UVA 10101 簡易版本
- `uva10170.py` - UVA 10170：無限旅館房間
- `uva10170_easy.py` - UVA 10170 簡易版本
- `tests/test_week07.py` - 週次測試檔
- `TEST_CASES.md` - 測試案例說明
- `TEST_LOG.md` - 測試執行紀錄
- `AI_USAGE.md` - AI 使用紀錄
- `assets/` - 補充資料或截圖

## 執行方式

```bash
python uva10062.py < input.txt
python uva10071.py < input.txt
python uva10093.py < input.txt
python uva10101.py < input.txt
python uva10170.py < input.txt
```

## 單元測試

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## 注意事項

- 本週作業已放在 `weeks/week-07/solutions/1114405035/`
- 每題都有原始版本與 `*_easy.py` 簡易版本
- `10101` 只允許移動木棒，不改變 `+`、`-`、`=` 的位置
