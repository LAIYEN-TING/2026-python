import csv
import json
import io
import xml.etree.ElementTree as ET
import functools
import time

# ═══════════════════════════════════════════════════════════
# 1. 裝飾器實作 (使用 functools.wraps 保留原函式資訊)
# ═══════════════════════════════════════════════════════════

def timeit(func):
    """
    計時裝飾器。
    @functools.wraps(func) 的作用是讓被裝飾後的函式依然保有原來的 __name__ 和 __doc__。
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        # 印出函式名稱與耗時，方便觀察
        print(f"  執行 {func.__name__:<15} 耗時: {elapsed:.6f}s")
        return result
    return wrapper

# ═══════════════════════════════════════════════════════════
# 2. 資料解析函式
# ═══════════════════════════════════════════════════════════

@timeit
def parse_csv(data_str: str):
    """將 CSV 字串解析為 dict 清單"""
    f = io.StringIO(data_str)
    reader = csv.DictReader(f)
    return list(reader)

@timeit
def parse_json(data_str: str):
    """將 JSON 字串解析為 dict 清單"""
    return json.loads(data_str)

@timeit
def parse_xml(data_str: str):
    """將 XML 字串解析為 dict 清單"""
    root = ET.fromstring(data_str)
    # 這裡假設 XML 格式為 <data><row id="..." name="..." score="..."/></data>
    return [row.attrib for row in root.findall("row")]

# ═══════════════════════════════════════════════════════════
# 3. 測試資料生成與執行
# ═══════════════════════════════════════════════════════════

def generate_mock_data(n=1000):
    """生成三種格式的測試資料"""
    base_data = [{"id": i, "name": f"Student{i}", "score": 80} for i in range(n)]
    
    # CSV
    csv_buf = io.StringIO()
    writer = csv.DictWriter(csv_buf, fieldnames=["id", "name", "score"])
    writer.writeheader()
    writer.writerows(base_data)
    csv_str = csv_buf.getvalue()
    
    # JSON
    json_str = json.dumps(base_data)
    
    # XML
    xml_rows = "".join([f'<row id="{d["id"]}" name="{d["name"]}" score="{d["score"]}"/>' for d in base_data])
    xml_str = f"<data>{xml_rows}</data>"
    
    return csv_str, json_str, xml_str

def main():
    N = 1000
    print(f"--- 生成 {N} 筆資料中 ---")
    c_data, j_data, x_data = generate_mock_data(N)
    
    print("\n--- 開始測試解析速度 ---")
    parse_csv(c_data)
    parse_json(j_data)
    parse_xml(x_data)

if __name__ == "__main__":
    main()
