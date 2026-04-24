# 題目 299

**題名**: UVA 299

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=e561)
- [Yui Huang 題解](https://yuihuang.com/zj-e561/)

## 題目敘述


在老舊的火車站，您也許會遇到少數僅存的"車箱置換員"。
"車箱置換員"是鐵路部門的員工，主要工作就是重新排列火車車廂。
一旦以最佳順序排列了車廂，所有火車司機要做的就是將車廂逐一卸下即可。
"車箱置換員"源自在鐵路橋附近的車站中執行此任務的第一人。
這座橋並不會垂直打開，而是繞著河中央的一根支柱旋轉。
將橋旋轉90度後，船隻就能向左或向右駛過。
第一位"車箱置換員"發現，這座橋最多可以在其上運行兩個車廂，通過將橋旋轉180度，車廂就能切換位置。
(缺點是車廂面向相反的方向，但是火車車廂可以以任何一種方式移動，所以沒差）。
現在幾乎所有的"車箱置換員"都已經淘汰了，鐵路公司希望將其操作自動化。
你的任務就是寫一個程式，該程式要計算最少需要交換幾次兩個相鄰車廂，才能將所有車廂依序排好。

## 輸入說明


輸入的第一行包含一個整數N，N代表測資數量。
每組測資的第一行包含一個整數L (0 ≤ L ≤ 50)，L代表火車的長度。
第二行包含數字1到L的排列，表示火車車廂的當前順序。
需要將火車車廂依照編號1到L的順序排好。

## 輸出說明

對於每組測資，請輸出："Optimal train swapping takes S swaps."，S代表最少交換次數。

---

## 解題思路

*請填入你的解題思路*

## 解題代碼

```python
# import sys

def solve():
    # [10] 從標準輸入讀取所有內容並切分成單字，方便處理不同格式的輸入
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    # 第一個數字是測資數量 N
    it = iter(input_data)
    num_test_cases = int(next(it))
    
    for _ in range(num_test_cases):
        # [8] 讀取車廂長度 L
        L = int(next(it))
        # 讀取接下來的 L 個數字作為車廂順序
        train = [int(next(it)) for _ in range(L)]
        
        # [9] 泡沫排序核心：計算交換次數
        swap_count = 0
        for i in range(L):
            # 每次掃描會將當前最大的數「浮」到正確位置
            for j in range(0, L - i - 1):
                # 如果左邊比右邊大，則必須交換
                if train[j] > train[j + 1]:
                    train[j], train[j + 1] = train[j + 1], train[j]
                    swap_count += 1
        
        # 依照題目要求格式輸出結果
        print(f"Optimal train swapping takes {swap_count} swaps.")

if __name__ == "__main__":
    solve()
    import sys

# 讀取所有輸入
data = sys.stdin.read().split()
if data:
    N = int(data[0])
    idx = 1
    for _ in range(N):
        L = int(data[idx])
        cars = [int(x) for x in data[idx+1 : idx+1+L]]
        idx += 1 + L
        
        swaps = 0
        # 簡易版泡沫排序
        for i in range(len(cars)):
            for j in range(len(cars) - 1):
                if cars[j] > cars[j+1]:
                    cars[j], cars[j+1] = cars[j+1], cars[j]
                    swaps += 1
                    
        print(f"Optimal train swapping takes {swaps} swaps.")
```

## 測試用例

*測試輸入與預期輸出*
