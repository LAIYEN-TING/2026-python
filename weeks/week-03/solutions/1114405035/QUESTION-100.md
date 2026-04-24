# 題目 100

**題名**: UVA 100

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=c039)
- [Yui Huang 題解](https://yuihuang.com/zj-c039/)

## 題目敘述

考慮以下的演算法：

1. 輸入 n
2. 印出 n
3. 如果 n = 1，結束
4. 如果 n 是奇數，則 n = 3 * n + 1
5. 否則 n = n / 2
6. GOTO 2

例如輸入 22，得到的數列：22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

據推測此演算法對任何整數而言會終止（當列印出 1 的時候）。
雖然此演算法很簡單，但以上的推測是否真實卻無法知道。
然而對所有的 n（0 < n < 1,000,000）來說，以上的推測已經被驗證是正確的。

給一個輸入 n，透過以上的演算法我們可以得到一個數列（以 1 作為結尾）。
此數列的長度稱為 n 的 cycle-length。
上面提到的例子，22 的 cycle-length 為 16。

問題：對任意兩個整數 i、j，我們想要知道介於 i、j（包含 i、j）之間的數所產生的數列中，最大的 cycle-length 是多少。

## 輸入說明


輸入可能包含了好幾列測試資料，每一列有一對整數資料 i，j 。
0< i，j < 1,000,000

## 輸出說明


對每一對輸入 i , j 你應該要輸出 i, j 和介於 i, j 之間的數所產生的數列中最大的 cycle length。

---

## 解題思路

核心是計算 Collatz 序列的 cycle-length，並在區間內取最大值。

做法：

- 對每個 n 計算 cycle-length：n 到 1 的步數（含 n 與 1）。
- 對輸入 i, j 先取區間 [min(i, j), max(i, j)]。
- 用記憶化（memoization）存已算過的 n，避免重複計算。

時間複雜度：

- 單次計算在平均情況下很快，搭配快取後能通過 0 < n < 1,000,000 的測資。

## 解題代碼

```python
```

## 測試用例

測試輸入：

```
1 10
100 200
201 210
900 1000
```

預期輸出：

```
1 10 20
100 200 125
201 210 89
900 1000 174
```
import sys

# [10] 使用字典作為快取 (Cache)，這就是 Memoization 技巧
# 初始條件：1 的循環長度是 1
memo = {1: 1}

def get_cycle_length(n):
    """計算 n 的 3n+1 循環長度"""
    # [10] 如果已經算過，直接回傳結果 (O(1) 查詢)
    if n in memo:
        return memo[n]
    
    # [8] 根據 3n+1 規則計算下一個數
    if n % 2 == 0:
        next_n = n // 2
    else:
        next_n = 3 * n + 1
    
    # 遞迴計算並存入快取
    # 這裡隱含了遞迴深度限制，但 3n+1 在 10^6 內通常不會超過限制
    res = 1 + get_cycle_length(next_n)
    memo[n] = res
    return res

def solve():
    # [10] 使用 sys.stdin 處理大量輸入，對應 EOF 狀況
    for line in sys.stdin:
        if not line.strip():
            continue
            
        try:
            # [8] 解析輸入 i, j
            parts = list(map(int, line.split()))
            if len(parts) < 2: continue
            i, j = parts[0], parts[1]
            
            # [9] 處理區間：i 可能大於 j，必須取正確的 range
            start, end = min(i, j), max(i, j)
            
            # [8] 生成器表達式 + max()
            # 這裡不會產生中間 List，記憶體效率最高 O(1)
            max_len = max(get_cycle_length(n) for n in range(start, end + 1))
            
            # 按格式要求輸出原始的 i, j
            print(f"{i} {j} {max_len}")
            
        except EOFError:
            break

if __name__ == "__main__":
    solve()
    #簡單
    import sys

# 快取：存儲數字與對應的循環長度
cache = {1: 1}

def get_len(n):
    # 如果快取沒有，就遞迴計算
    if n not in cache:
        # 奇數 3n+1, 偶數 n/2
        nxt = n * 3 + 1 if n % 2 else n // 2
        cache[n] = 1 + get_len(nxt)
    return cache[n]

# 持續讀取直到輸入結束
for line in sys.stdin:
    nums = [int(x) for x in line.split()]
    if not nums: break
    
    i, j = nums[0], nums[1]
    # 注意：範圍必須從小到大，但輸出要保持原始順序
    low, high = (i, j) if i < j else (j, i)
    
    # 使用推導式計算範圍內最大值
    ans = max(get_len(n) for n in range(low, high + 1))
    print(f"{i} {j} {ans}")