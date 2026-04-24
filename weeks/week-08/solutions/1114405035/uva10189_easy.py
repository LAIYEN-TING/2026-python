import sys

lines = sys.stdin.read().splitlines()
idx = 0
case_num = 1
first = True

while idx < len(lines):
    if not lines[idx].strip():
        idx += 1; continue
    n, m = map(int, lines[idx].split())
    if n == 0 and m == 0: break
    
    if not first: print()
    first = False
    print(f"Field #{case_num}:")
    case_num += 1
    
    grid = [lines[idx+1+i] for i in range(n)]
    idx += n + 1
    
    for i in range(n):
        row = ""
        for j in range(m):
            if grid[i][j] == '*':
                row += '*'
            else:
                mines = sum(1 for dx in [-1, 0, 1] for dy in [-1, 0, 1]
                            if 0 <= i+dx < n and 0 <= j+dy < m and grid[i+dx][j+dy] == '*')
                row += str(mines)
        print(row)