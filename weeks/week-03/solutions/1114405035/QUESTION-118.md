# 題目 118

**題名**: UVA 118

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=c082)
- [Yui Huang 題解](https://yuihuang.com/zj-c082/)

## 題目敘述


給你一塊矩形土地的長寬，再依序給定每個機器人的初始位置狀況及一連串的指令集，你必須用你的程式求出每個機器人最後的位置狀況。
一個機器人的位置狀況包括了其坐標（ x 坐標， y 坐標），和它面向的方向（用 N , S , E , W 來分別代表北、南、東、西）。
至於一個機器人所收到的指令集，是一個由字母 ' L ' ， ' R ' ， 和 ' F ' 所構成的字串，其分別代表：左轉（Left）：機器人在原地往左轉 90 度。
右轉（Right）: 機器人在原地往右轉 90 度。
前進（Forward）: 機器人往其面向的方向向前走一格，且不改變其面向之方向。
從坐標 (x,y) 走至 (x,y+1) 的這個方向我們定義為北方。
因為此矩形土地是有邊界的，所以一旦一個機器人走出邊界掉落下去，就相當於永遠消失了。
不過這個掉下去的機器人會留下「標記 ( scent ) 」，提醒以後的機器人，避免他們從同一個地方掉下去。
掉下去的機器人會把標記，留在他掉落之前所在的最後一個坐標點。
所以對於以後的機器人，當他正位在有標記的地方時，這個機器人就會忽略會讓他掉下去的指令。

## 輸入說明


輸入裡的第一列有2個正整數，代表這個矩形世界右上角頂點的坐標，其中假設這個世界的左下角頂點坐標為 ( 0 , 0 )。
接下來是若干組有關機器人的初始位置狀況和指令集，每個機器人2列。
第一列為位置狀況，包括了兩個整數和一個字元（ N , S , E 或 W ），代表機器人初始的位置坐標以及機器人最初所面對的方向。
第二列則是指令集，是一個由 ' L ' ， ' R ' 和 ' F ' 所組成的字串。
輸入以 end-of-file 作為結束。
各機器人是依序動作的，也就是說，直到一個機器人作完他全部的動作，下一個機器人才會開始動作。
所有機器人的初始位置皆會在矩形土地上，不會落在外面。
任何坐標的最大值皆不會超過 50 。
每個指令集的長度皆不會超過 100 個字元長。

## 輸出說明


對於每一個機器人，你都必須輸出其最後所在的坐標和面對的方向。
如果一個機器人會掉落出此世界外，你必須先輸出他在掉落前，最後的所在位置和面對的方向，再多加一個字： LOST 。

---

## 解題思路

*請填入你的解題思路*

## 解題代碼

```python
# import sys

def solve():
    # [10] 讀取地圖邊界 (處理第一列)
    first_line = sys.stdin.readline().split()
    if not first_line: return
    max_x, max_y = map(int, first_line)
    
    # [8] 使用 Set 存儲掉落標記座標，保證查詢速度為 O(1)
    scents = set()
    
    # 定義順時針方向，方便利用索引處理旋轉
    directions = ['N', 'E', 'S', 'W']
    # [8] 字典映射：方向對應的座標位移 (dx, dy)
    move_map = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }

    # [10] 持續讀取直到 EOF
    while True:
        pos_line = sys.stdin.readline().split()
        if not pos_line: break # EOF 結束
        
        x, y = int(pos_line[0]), int(pos_line[1])
        facing = pos_line[2]
        
        # 讀取指令字串
        commands = sys.stdin.readline().strip()
        
        lost = False
        for cmd in commands:
            if cmd == 'R':
                # 右轉：順時針移動索引
                idx = (directions.index(facing) + 1) % 4
                facing = directions[idx]
            elif cmd == 'L':
                # 左轉：逆時針移動索引
                idx = (directions.index(facing) - 1) % 4
                facing = directions[idx]
            elif cmd == 'F':
                dx, dy = move_map[facing]
                nx, ny = x + dx, y + dy
                
                # 檢查是否超出地圖邊界
                if nx < 0 or nx > max_x or ny < 0 or ny > max_y:
                    # [9] 如果當前位置沒有被標記過，才會掉下去
                    if (x, y) not in scents:
                        scents.add((x, y)) # 留下標記
                        lost = True
                        break # 機器人消失，停止指令
                    # 如果有標記，則忽略此 Forward 指令，留在 (x, y)
                else:
                    x, y = nx, ny
        
        # 輸出最終位置，若掉落則加上 LOST
        output = f"{x} {y} {facing}"
        if lost:
            output += " LOST"
        print(output)

if __name__ == "__main__":
    solve()
    import sys

# 一次性取得所有輸入行，過濾掉空行
lines = [l.strip() for l in sys.stdin.readlines() if l.strip()]
if not lines: exit()

mx, my = map(int, lines[0].split())
scents = set()
dirs = "NESW" # 字串也可以當清單用

i = 1
while i < len(lines):
    # 解析位置與指令
    x, y, f = lines[i].split(); x, y = int(x), int(y)
    cmds = lines[i+1]
    lost = False
    
    for c in cmds:
        if c == 'F':
            # 根據方向計算位移
            dx, dy = {"N":(0,1), "E":(1,0), "S":(0,-1), "W":(-1,0)}[f]
            if 0 <= x+dx <= mx and 0 <= y+dy <= my:
                x, y = x+dx, y+dy
            elif (x, y) not in scents:
                scents.add((x, y))
                lost = True
                break
        else:
            # 處理旋轉：利用字串索引
            curr_i = dirs.find(f)
            f = dirs[(curr_i + (1 if c == 'R' else -1)) % 4]
            
    print(f"{x} {y} {f}{' LOST' if lost else ''}")
    i += 2
```

## 測試用例

*測試輸入與預期輸出*
