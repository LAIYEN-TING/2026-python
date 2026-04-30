import time
import json

# ═══════════════════════════════════════════════════════════
# 1. 簡易版計時裝飾器 (拿掉 wraps 讓結構最簡化)
# ═══════════════════════════════════════════════════════════

def simple_timer(func):
    """
    這是一個最基礎的裝飾器模板：
    1. 接收一個函式 (func)
    2. 定義一個內層函式 (wrapper)，用來接收所有參數 (*args, **kwargs)
    3. 在內層函式中執行原函式，並加上我們想要的邏輯 (計時)
    """
    def wrapper(*args, **kwargs):
        # 紀錄開始時間
        t1 = time.time() 
        
        # 執行原本的函式
        result = func(*args, **kwargs)
        
        # 紀錄結束時間並印出
        t2 = time.time()
        print(f"函式 [{func.__name__}] 執行完畢，花了 {t2 - t1:.5f} 秒")
        
        # 把原函式的結果回傳回去，不能吃掉人家的結果！
        return result
    
    return wrapper

# ═══════════════════════════════════════════════════════════
# 2. 使用裝飾器
# ═══════════════════════════════════════════════════════════

@simple_timer
def easy_json_parse(data):
    """簡單的 JSON 解析測試"""
    return json.loads(data)

@simple_timer
def sleep_test(seconds):
    """測試睡眠時間"""
    time.sleep(seconds)
    return "醒來了"

def main():
    print("--- 簡易裝飾器測試 ---")
    
    # 測試解析 JSON
    test_data = '[{"name": "小明", "age": 20}]' * 1000
    # 修正：重複字串會變成無效 JSON (如 [...] [...] )，改用 list 重複
    json_str = json.dumps([{"name": "小明", "age": 20}] * 1000)
    
    easy_json_parse(json_str)
    
    # 測試睡覺
    print(sleep_test(0.5))

if __name__ == "__main__":
    main()
