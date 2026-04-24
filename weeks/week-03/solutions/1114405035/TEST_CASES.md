# TEST CASES - Week 03

| 編號 | 輸入 (初始位置, 指令) | 預期結果 | 實際結果 | 狀態 | 對應測試函式 |
|:---:|:---|:---|:---|:---:|:---|
| 1 | (1, 1, E), RFRFRFRF | (1, 1, E) | (1, 1, E) | PASS | test_complex_commands |
| 2 | (1, 1, N), L | (1, 1, W) | (1, 1, W) | PASS | test_turn_left |
| 3 | (1, 1, N), R | (1, 1, E) | (1, 1, E) | PASS | test_turn_right |
| 4 | (1, 1, N), FFF | (1, 3, N) | (1, 3, N) | PASS | test_move_forward |
| 5 | (1, 1, N), FFFF | (1, 3, N) LOST | (1, 3, N) LOST | PASS | test_move_out_of_bounds |
| 6 | (1, 3, N) + Scent, F | (1, 3, N) | (1, 3, N) | PASS | test_scent_ignores_danger |
| 7 | (1, 3, E) + N-Scent, F | (2, 3, E) | (2, 3, E) | PASS | test_different_scent_directions |
| 8 | (1, 1, N), FXF | (1, 3, N) | (1, 3, N) | PASS | test_invalid_command |

## 測資設計說明
- **案例 5**: 測試邊界掉落並觸發 LOST。
- **案例 6**: 測試當同一格已有相同方向的 Scent 時，機器人是否會忽略危險指令。
- **案例 7**: 測試不同方向的 Scent 不應互相干擾。
- **案例 8**: 測試程式對於非 L/R/F 指令的容錯性。
