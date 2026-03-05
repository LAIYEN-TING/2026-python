# 8 容器操作與推導式

你必須已經「不需要解釋」就能看懂：

```python
[x for x in data if x > 0]
{k: v for k, v in d.items()}
```

```python
(x * x for x in nums)
```
nums = [1, 2, 3, 4, 5]

# 場景 A：計算平方和
# 注意：直接在 sum() 裡面寫推導式，不需要多一對括號
total_sum = sum(x * x for x in nums) 

# 場景 B：過濾後尋找最小值
# 如果資料很大，生成器能節省大量記憶體
min_val = min(x for x in nums if x > 2)

# 場景 C：字串連接 (join)
# 適合將非字串序列轉換後合併
labels = ["ID", "Name", "Score"]
csv_line = ",".join(str(item).upper() for item in labels)

print(f"平方和: {total_sum}") # 55
print(f"大於2的最小值: {min_val}") # 3
print(f"CSV 格式: {csv_line}") # ID,NAME,SCORE

用途（對應第一章範例）：

- 過濾序列（1.16）
- 字典子集（1.17）
- `sum(...)` / `min(...)` / `join(...)`
