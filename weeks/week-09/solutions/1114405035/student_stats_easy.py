import zipfile
import csv
from collections import Counter
from pathlib import Path

# 這個版本使用了更直觀、容易記憶的方法來處理資料
# 適合初學者理解 zip 與 csv 的基本組合應用

def main():
    # 1. 設定檔案路徑 (使用 Path 處理路徑，既現代又方便)
    HERE = Path(__file__).resolve().parent
    # 找到專案中的 zip 檔案
    ZIP_PATH = HERE.parents[3] / "assets" / "npu-stu-109-114-anon.zip"

    if not ZIP_PATH.exists():
        print(f"找不到檔案: {ZIP_PATH}")
        return

    # 2. 用來存放統計結果的字典
    # 格式：{ "109": Counter({...}), "110": ... }
    stats_by_year = {}

    # 3. 開啟並讀取 ZIP 檔案
    with zipfile.ZipFile(ZIP_PATH) as z:
        # 列出 zip 裡所有的檔名
        for filename in z.namelist():
            # 我們只處理 csv 檔案
            if not filename.endswith(".csv"):
                continue
            
            # 取得年度 (檔名前三個字，例如 '109')
            year = filename[:3]
            
            # 讀取檔案內容 (bytes) 並轉換成字串 (utf-8-sig 可以自動去掉 Excel 的 BOM)
            content = z.read(filename).decode("utf-8-sig")
            
            # 將字串依照換行符號切開
            lines = content.splitlines()
            
            # 使用 csv.reader 讀取切開後的每一行
            # 這是最簡單的記憶方式：reader(清單)
            reader = csv.reader(lines)
            all_rows = list(reader)
            
            if not all_rows:
                continue
                
            header = all_rows[0]  # 第一行是標題
            rows = all_rows[1:]   # 剩下的才是資料
            
            # 找到「系所名稱」是在第幾個欄位
            try:
                dept_idx = header.index("系所名稱")
            except ValueError:
                continue
            
            # 統計該年度每個系所的人數
            # 這裡用列表推導式配合 Counter，非常簡潔
            dept_counts = Counter(row[dept_idx] for row in rows if len(row) > dept_idx)
            
            # 把統計結果存入字典
            stats_by_year[year] = {
                "total": len(rows),
                "counts": dept_counts
            }

    # 4. 印出結果報告
    print("# 學生資料統計簡報")
    print("-" * 30)
    
    # 依照年度排序後印出
    for year in sorted(stats_by_year):
        total = stats_by_year[year]["total"]
        # 取得人數最多的系所
        top_dept, top_num = stats_by_year[year]["counts"].most_common(1)[0]
        
        print(f"【{year} 學年度】")
        print(f"  總人數：{total} 人")
        print(f"  人數最多系所：{top_dept} ({top_num} 人)")
        print("-" * 30)

if __name__ == "__main__":
    main()
