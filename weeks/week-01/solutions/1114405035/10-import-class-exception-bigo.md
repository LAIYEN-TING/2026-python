# 10 模組、類別、例外與 Big-O（最低門檻）

## import 基礎

你必須已經「不需要解釋」就能看懂：

```python
import heapq
from collections import deque
```

用途（對應第一章範例）：

- 幾乎所有進階工具

---

## class 與物件（看得懂即可）

```python
class User:
    def __init__(self, user_id):
        self.user_id = user_id
```

```python
user.user_id
```

用途（對應第一章範例）：

- PriorityQueue Item
- attrgetter
- namedtuple 對照 class

---

## 例外處理（try / except）

```python
try:
    int(val)
except ValueError:
    pass
```

用途（對應第一章範例）：

- `filter(is_int, values)`

---

## 基本 Big-O 觀念（聽得懂即可）

你需要知道：

- O(1), O(N), O(log N)

用途（對應第一章範例）：

- deque vs list
- heap push/pop
- sorted vs nlargest
import heapq
from operator import attrgetter

# --- 1. 定義類別 ---
class Job:
    def __init__(self, name, priority_str):
        self.name = name
        # 這裡有個潛在風險：priority_str 可能是亂碼
        self.priority = self._parse_priority(priority_str)

    def _parse_priority(self, val):
        """內部方法：嘗試將輸入轉為整數，失敗則設為最低優先級 (99)"""
        try:
            return int(val)
        except (ValueError, TypeError):
            return 99

    def __repr__(self):
        return f"Job(name='{self.name}', p={self.priority})"

# --- 2. 原始資料 (包含髒資料) ---
raw_data = [
    ("Server Fix", "1"),
    ("Email Reply", "5"),
    ("Coffee Break", "invalid"), # 測試例外處理
    ("Security Patch", "1"),
    ("UI Update", "3")
]

# --- 3. 建立物件清單 (推導式運用) ---
jobs = [Job(name, p) for name, p in raw_data]

# --- 4. 效能權衡 (Big-O 應用) ---

# 如果我們只需要「最緊急」的前 2 名：
# 使用 heapq.nsmallest 的複雜度約為 O(N log K)，比全排序 O(N log N) 快
top_urgent = heapq.nsmallest(2, jobs, key=attrgetter('priority'))

# 如果我們需要「完整排序」清單：
# 使用 sorted()，時間複雜度 O(N log N)
sorted_jobs = sorted(jobs, key=attrgetter('priority'))

# --- 5. 輸出結果 ---
print("--- 最緊急任務 (Top 2) ---")
for job in top_urgent:
    print(job)

print("\n--- 所有任務排序 (由重到輕) ---")
for job in sorted_jobs:
    print(job)