# AI 使用紀錄 - Week 03

## 1. 詢問 AI 的問題
- 如何將 (0,0) 底部的座標系轉換為 pygame 的頂部 (0,0) 座標系？
- 如何在 `unittest` 中模擬多個連續的輸入指令？
- `pygame` 如何在不重新繪製整個地圖的情況下移動機器人？（AI 建議還是每影格重繪，因為地圖小）

## 2. 採用的建議
- 採用了 `grid_to_screen` 的座標翻轉公式。
- 採用了 `execute_commands` 迴圈處理指令字串的寫法。

## 3. 拒絕的建議
- AI 建議使用 `sprite` 類別，但我認為這對簡單的 2D 格子模擬來說過於複雜，直接用 `draw.circle` 與 `draw.rect` 更直觀。

## 4. 自行修正的案例
- AI 提供的位移表沒考慮到 `scent` 的忽略邏輯，我手動在 `move_forward` 中加入了 `if world.has_scent(...)` 的判斷。
