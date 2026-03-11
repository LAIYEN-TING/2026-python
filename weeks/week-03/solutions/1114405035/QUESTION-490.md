# 題目 490

**題名**: UVA 490

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=c045)
- [Yui Huang 題解](https://yuihuang.com/zj-c045/)

## 題目敘述


在這個問題中你必須將數列文字往順時針方向旋轉90度。
也就是說將原本由左到右，由上到下的句子輸出成由上到下，由右到左。
例如輸入是 HELLO（一行）和 WORLD（一行），輸出應該重新排列成為一個矩陣，使得最後一行變成最左列，第一行變成最右列。

## 輸入說明


輸入最多不會超過100列，每列最多不會超過100個字元。
合法的字元包括：換行，空白，所有的標點符號，數字，以及大小寫字母。
（注意：Tabs並不算是合法字元。
）輸入直到EOF（檔案結束）。

## 輸出說明


最後一列輸入必須垂直輸出在最左邊一行，輸入的第一列必須垂直輸出在最右邊一行。
每行輸出應該使用與輸入中最寬的行等長的空格填充，以形成正確的矩形。
輸入和輸出之間有90度的順時針旋轉關係。

## 解題思路

*請填入你的解題思路*

## 解題代碼

```python
# 你的代import sys

def solve():
    # [10] 讀取所有輸入列並存入 list
    # 使用 .rstrip('\n\r') 是為了保留每列末尾可能的空格，只去掉換行符
    lines = []
    for line in sys.stdin:
        lines.append(line.replace('\n', '').replace('\r', ''))
    
    if not lines:
        return

    # [8] 找出所有輸入中最長的一列長度 L
    max_len = max(len(l) for l in lines)
    
    # 旋轉邏輯：
    # 輸出共有 max_len 列
    # 每一列要從最後一個原始輸入掃描回第一個原始輸入
    for char_idx in range(max_len):
        output_row = []
        # [9] 從最後一列 (len-1) 遍歷回第一列 (0)
        for line_idx in range(len(lines) - 1, -1, -1):
            current_line = lines[line_idx]
            
            # 如果目前字串長度足夠，就放入該字元
            if char_idx < len(current_line):
                output_row.append(current_line[char_idx])
            else:
                # [8] 長度不足則補空白，確保輸出維持矩形形狀
                output_row.append(" ")
        
        # 將該列字元結合並印出
        print("".join(output_row))

if __name__ == "__main__":
    solve()碼這裡
    import sys

# 一次性讀取所有行並存入清單
lines = [line.strip('\n\r') for line in sys.stdin]
if not lines: exit()

# 取得最長寬度
max_w = max(len(s) for s in lines)

# 外層跑字元索引 (0 ~ max_w-1)
for i in range(max_w):
    # 內層由最後一列往第一列跑
    for j in range(len(lines) - 1, -1, -1):
        # 判斷當前行 j 的長度是否超過索引 i
        if i < len(lines[j]):
            print(lines[j][i], end='')
        else:
            print(' ', end='')
    print() # 換行
```

## 測試用例

*測試輸入與預期輸出*
