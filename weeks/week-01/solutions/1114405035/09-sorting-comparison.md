# 9 比較、排序與 key 函式

你必須已經「不需要解釋」就能看懂：

```python
a < b
```

```python
sorted(data, key=lambda x: x.price)
min(data, key=itemgetter('uid'))
```
from operator import itemgetter
from itertools import groupby

# 原始資料：(任務類別, 優先級, 任務名稱)
# 優先級數字越小代表越緊急 (1 > 2 > 3)
tasks = [
    ('System', 2, 'Update OS'),
    ('User', 1, 'Fix Login'),
    ('System', 1, 'Reboot Server'),
    ('User', 2, 'Change Avatar'),
    ('System', 1, 'Security Patch'),
]

# --- 步驟 1: 多重排序 ---
# 我們希望先按「類別」排序，類別相同時再按「優先級」排序
# key 回傳一個 tuple (item[0], item[1])，Python 會自動套用 tuple 比較規則
tasks.sort(key=itemgetter(0, 1))

print("--- 排序後的任務 ---")
for t in tasks:
    print(t)

# --- 步驟 2: 分組 (groupby) ---
# 注意：因為已經按類別(索引0)排序過了，groupby 才能正確運作
print("\n--- 分組後的報告 ---")
for category, group in groupby(tasks, key=itemgetter(0)):
    print(f"[{category}]")
    for item in group:
        # 使用 tuple 解構獲取優先級與任務名
        _, priority, name = item
        print(f"  - 優先級 {priority}: {name}")

# --- 步驟 3: Top-N 應用 ---
# 找出全體任務中優先級數字最小(最緊急)的前 3 名
import heapq
urgent_top3 = heapq.nsmallest(3, tasks, key=itemgetter(1))

print("\n--- 最緊急前三名 ---")
print(urgent_top3)

用途（對應第一章範例）：

- tuple 比較順序
- 為何 `(priority, index, item)` 可排序
- Top-N
- dict / object 排序
- groupby 前置排序
