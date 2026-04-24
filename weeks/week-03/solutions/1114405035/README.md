# Week 03 作業範本：1114405035

本範本展示 `weeks/week-03/solutions/<student-id>/` 內的推薦檔案結構與執行方式。

## 目錄內容

### UVA 解題程式
- `uva100.py` - UVA 100：Collatz 序列最大 cycle-length
- `uva118.py` - UVA 118：機器人模擬
- `uva272.py` - UVA 272：TeX 引號替換
- `uva299.py` - UVA 299：火車排序交換次數
- `uva490.py` - UVA 490：文字旋轉 90 度

### pygame 遊戲
- `robot_game.py` - pygame 主程式（互動畫面）⚠️ 需要 pygame 套件
- `robot_game_text.py` - **文字版遊戲**（推薦替代方案，無需額外套件）
- `robot_core.py` - 核心邏輯（不依賴 pygame，便於測試）

### 測試與文件
- `tests/test_robot_core.py` - 核心邏輯測試
- `tests/test_robot_scent.py` - scent 規則測試
- `TEST_CASES.md` - 測試案例
- `TEST_LOG.md` - 測試執行日誌
- `AI_USAGE.md` - AI 使用紀錄

### 遊戲資源
- `assets/gameplay.png` - 遊戲截圖（請手動截圖）
- `assets/replay.gif` - 重播動畫（選做）

## 執行方式

### UVA 程式測試
```bash
python uva100.py < input.txt
python uva118.py < input.txt
# ...以此類推
```

### pygame 遊戲
```bash
python robot_game.py
```

控制：
- `L/R/F`：執行指令
- `空白鍵`：重置機器人
- 滑鼠點擊按鈕：重置機器人 / 清除 scents / 重播

⚠️ **pygame 安裝問題**：如果 pygame 安裝失敗，請使用文字版：

### 文字版遊戲（推薦）
```bash
python robot_game_text.py
```

控制：
- `L`：左轉
- `R`：右轉  
- `F`：前進
- `Q`：離開
- `C`：清除 scents
- `N`：新機器人

### 測試執行
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## 注意事項

- pygame 遊戲需要安裝 `pygame` 套件：`pip install pygame`
- **如果 pygame 安裝失敗**，請使用 `robot_game_text.py` 文字版遊戲
- 請手動截圖遊戲畫面並儲存為 `assets/gameplay.png`（可使用文字版遊戲的輸出）
- 所有程式都有繁體中文註解
- 測試涵蓋正常、邊界、錯誤案例