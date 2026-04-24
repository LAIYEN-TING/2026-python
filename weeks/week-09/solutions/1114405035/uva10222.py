import sys

def solve():
    # 建立對應的標準鍵盤字元集 (向左位移2格)
    keyboard = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
    decode_map = {}
    for i in range(2, len(keyboard)):
        decode_map[keyboard[i]] = keyboard[i-2]
        
    for line in sys.stdin:
        result = []
        for char in line.lower():
            # 如果字元在我們建立好的 map 中，就替換
            if char in decode_map:
                result.append(decode_map[char])
            else:
                result.append(char)
        print("".join(result), end="")

if __name__ == '__main__':
    solve()