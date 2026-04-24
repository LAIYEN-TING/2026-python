# Robot Lost - 1114405035 賴彥廷

## 功能清單
- [x] 2D 格子地圖顯示 (0,0) 到 (5,3)
- [x] 機器人位置與朝向顯示（綠色：生存，紅色：LOST）
- [x] Scent 留痕跡功能（橘色圓圈標示）
- [x] 鍵盤互動操作 (L/R/F)
- [x] 新增機器人 (N) 與 清除 Scent (C)
- [x] 狀態顯示 HUD（座標、方向、狀態）

## 執行方式
1. 安裝依賴：`pip install pygame`
2. 啟動遊戲：`python robot_game.py`
3. 執行測試：`python -m unittest tests/test_robot_core.py`

## 測試方式
使用 Python 內建 `unittest` 模組，覆蓋了轉向、越界、Scent 生效等 10 個案例。

## 資料結構選擇理由
1. **set[tuple]**: 用於儲存 `scents`，因為 `scent` 的查詢頻率很高，使用 `set` 的查詢複雜度為 O(1)，且能自動處理重複位置。
2. **list[tuple]**: 用於儲存機器人的 `history`（路徑紀錄），方便未來擴充回放功能。
3. **位移表 (dict)**: 使用 `MOVE_MAP` 將方向字元映射到 `(dx, dy)`，避免大量的 `if-else` 判斷，程式更簡潔。

## 踩到的 Bug 與修正
- **Bug**: 在 pygame 繪圖時，座標 (0,0) 出現在左上角，但題目要求 (0,0) 在左下角。
- **修正**: 撰寫 `grid_to_screen` 轉換函式，使用 `screen_y = MARGIN + (world.height - y) * CELL_SIZE` 進行垂直翻轉。

## 遊玩截圖
![gameplay](assets/gameplay.png)
*(請記得自行放入截圖檔案)*
