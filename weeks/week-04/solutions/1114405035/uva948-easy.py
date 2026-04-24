#!/usr/bin/env python3
import sys

# 題目：UVA 948 (實際上是 False Coin)
# 目的：根據秤重結果找出唯一的假幣

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    it = iter(input_data)
    try:
        m = int(next(it))
        for case in range(m):
            n = int(next(it))
            k = int(next(it))
            
            # 可能為「輕」或「重」的硬幣集合
            # 初始時所有硬幣都有可能
            maybe_light = [True] * (n + 1)
            maybe_heavy = [True] * (n + 1)
            
            for _ in range(k):
                pi = int(next(it))
                left = [int(next(it)) for _ in range(pi)]
                right = [int(next(it)) for _ in range(pi)]
                result = next(it)
                
                left_set = set(left)
                right_set = set(right)
                involved = left_set | right_set
                
                if result == '=':
                    # 這些硬幣一定是真的
                    for coin in involved:
                        maybe_light[coin] = False
                        maybe_heavy[coin] = False
                elif result == '<':
                    # 左邊輕，右邊重
                    # 不在秤上的硬幣一定是真的
                    for coin in range(1, n + 1):
                        if coin not in involved:
                            maybe_light[coin] = False
                            maybe_heavy[coin] = False
                        elif coin in left_set:
                            maybe_heavy[coin] = False # 左邊只可能輕
                        elif coin in right_set:
                            maybe_light[coin] = False # 右邊只可能重
                elif result == '>':
                    # 左邊重，右邊輕
                    for coin in range(1, n + 1):
                        if coin not in involved:
                            maybe_light[coin] = False
                            maybe_heavy[coin] = False
                        elif coin in left_set:
                            maybe_light[coin] = False # 左邊只可能重
                        elif coin in right_set:
                            maybe_heavy[coin] = False # 右邊只可能輕
            
            # 統計還有可能的假幣
            candidates = []
            for coin in range(1, n + 1):
                if maybe_light[coin] or maybe_heavy[coin]:
                    candidates.append(coin)
            
            # 如果只有一個候選者，輸出編號，否則輸出 0
            if len(candidates) == 1:
                print(candidates[0])
            else:
                print(0)
                
            # 測試資料間輸出一空白列
            if case < m - 1:
                print()
                
    except StopIteration:
        pass

if __name__ == '__main__':
    solve()
