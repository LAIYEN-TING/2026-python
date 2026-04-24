# TEST_LOG

## Red run

- command: `python -m unittest discover -s tests -p "test_*.py" -v`
- result: 7 tests run, 2 failures
- failure reason: `robot_core` 的 `scent` 邏輯錯誤，LOST 後沒有正確留下 scent
- 修改說明：修正 `RobotWorld.execute_instruction` 中 LOST 時的 scent 添加邏輯

## Green run

- command: `python -m unittest discover -s tests -p "test_*.py" -v`
- result: 7 tests run, 7 OK
- 修正說明：全部測試通過，包含 Robot 核心邏輯與 scent 規則驗證
