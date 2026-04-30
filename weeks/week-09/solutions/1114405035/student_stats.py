import csv
import io
import pickle
import tempfile
import zipfile
from collections import Counter
from pathlib import Path

def process_student_zip(zip_path: Path):
    """
    讀取壓縮檔中的 CSV 資料並進行統計。
    回傳 summary 格式: {年度: {'total': 總數, 'by_dept': 系所統計, 'by_entry': 入學方式統計}}
    """
    summary = {}
    
    if not zip_path.exists():
        raise FileNotFoundError(f"找不到檔案: {zip_path}")

    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            if not info.filename.endswith(".csv"):
                continue
            
            # 取得年度 (例如 '109')
            year = info.filename[:3]
            
            # 讀取內容並處理 BOM
            raw = z.read(info)
            text = raw.decode("utf-8-sig")
            
            # 使用 StringIO 將字串模擬成檔案供 csv.reader 讀取
            reader = csv.reader(io.StringIO(text))
            rows = list(reader)
            
            if not rows:
                continue
                
            header = rows[0]
            data = rows[1:]
            
            # 找出欄位索引
            try:
                dept_idx = header.index("系所名稱")
                entry_idx = header.index("入學方式")
            except ValueError:
                continue # 忽略格式不符的檔案

            # 統計
            by_dept = Counter(r[dept_idx] for r in data if len(r) > dept_idx)
            by_entry = Counter(r[entry_idx] for r in data if len(r) > entry_idx)

            summary[year] = {
                "total": len(data),
                "by_dept": by_dept,
                "by_entry": by_entry,
            }
            
    return summary

def generate_markdown_report(summary):
    """
    根據統計資料生成 Markdown 格式報告字串。
    """
    lines = ["# 6 屆新生概況報告\n"]
    lines.append("| 學年 | 人數 | 第一大系所 |")
    lines.append("|------|------|------------|")
    
    for year in sorted(summary):
        top_dept, top_n = summary[year]["by_dept"].most_common(1)[0]
        lines.append(f"| {year} | {summary[year]['total']} | {top_dept} ({top_n}) |")
        
    return "\n".join(lines)

def main():
    # 設定路徑
    HERE = Path(__file__).resolve().parent
    # 假設資產目錄在專案根目錄下
    ZIP_PATH = HERE.parents[3] / "assets" / "npu-stu-109-114-anon.zip"
    
    try:
        print(f"正在處理: {ZIP_PATH.name}")
        summary = process_student_zip(ZIP_PATH)
        
        # 輸出部分統計到終端機
        print("\n=== 6 屆新生人數 ===")
        for year in sorted(summary):
            print(f"  {year} 學年：{summary[year]['total']:>4} 人")

        # 生成報告
        report_content = generate_markdown_report(summary)
        print("\n=== Markdown 報告預覽 ===")
        print(report_content)
        
    except Exception as e:
        print(f"發生錯誤: {e}")

if __name__ == "__main__":
    main()
