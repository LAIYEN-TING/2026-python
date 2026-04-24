# Week 06 作業：1114405035

本週為自習週，主要任務是整理常用的 Python I/O 模板與字串處理模板，並記錄學習心得。

## 目錄

- `io_template.py`：常用輸入輸出與快速讀取模板
- `string_template.py`：常見字串分割、格式化、合併模板
- `AI_USAGE.md`：AI 使用紀錄
- `TEST_LOG.md`：本週作業執行紀錄
- `assets/`：補充資料或截圖（目前可空）

## 本週學習重點

1. 常見輸入讀取方式：
   - `sys.stdin.readline()` 讀行
   - `sys.stdin.read().split()` 讀取所有 token
   - `map(int, input().split())` 轉換數字列表
2. 字串處理技巧：
   - `split()` 和 `join()`
   - `strip()` 清除前後空白
   - `format()` 與 f-string 格式化輸出
3. 迭代器與生成器應用：
   - 使用 `yield` 建立生成器
   - 用 `for` 迭代器處理大型輸入資料
4. 程式撰寫模板：
   - 分離輸入處理與問題邏輯
   - 先寫 `process_input()` 再寫 `main()`

## 使用方式

```bash
python io_template.py
python string_template.py
```

## 注意事項

- 本週作業檔案已放在 `weeks/week-06/solutions/1114405035/`
- 作業內容為個人模板整理與學習心得，不含特定 `QUESTION-*.md`
