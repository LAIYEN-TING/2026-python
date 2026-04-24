import sys

def solve():
    # 讀取所有的標準輸入並依行分割
    input_data = sys.stdin.read().splitlines()
    idx = 0
    field_num = 1
    
    while idx < len(input_data):
        line = input_data[idx].strip()
        if not line:
            idx += 1
            continue
        
        # 解析 n, m (行與列)
        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break
            
        grid = []
        for _ in range(n):
            idx += 1
            grid.append(list(input_data[idx]))
            
        if field_num > 1:
            print()
        print(f"Field #{field_num}:")
        field_num += 1
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '*':
                    print('*', end='')
                else:
                    count = sum(1 for di in [-1, 0, 1] for dj in [-1, 0, 1] 
                                if 0 <= i+di < n and 0 <= j+dj < m and grid[i+di][j+dj] == '*')
                    print(count, end='')
            print()
        idx += 1

if __name__ == '__main__':
    solve()