# TEST LOG - Week 03

## 1. Red Cycle (Initial Failure)
- **執行指令**: `python -m unittest tests/test_robot_core.py`
- **測試總數**: 10
- **通過數**: 0
- **失敗數**: 10
- **修改內容**: 剛建立測試檔案，尚未實作 `Robot` 與 `World` 類別，因此所有匯入與初始化皆失敗。

## 2. Green Cycle (Success)
- **執行指令**: `python -m unittest tests/test_robot_core.py`
- **測試總數**: 10
- **通過數**: 10
- **失敗數**: 0
- **修改內容**: 完成了 `robot_core.py` 中的 `turn_left`, `turn_right`, `move_forward` 與 `scent` 判定邏輯。修正了邊界判定從 `>` 改為 `>=` 的錯誤。
