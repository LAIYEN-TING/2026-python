import csv
import io
import platform
import zipfile
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# ── 系所 → 學院 對照表 ─────────────────
DEPT_TO_COLLEGE = {
    "應用外語系": "人文暨管理學院", "航運管理系": "人文暨管理學院",
    "行銷與物流管理系": "人文暨管理學院", "觀光休閒系": "人文暨管理學院",
    "資訊管理系": "人文暨管理學院", "餐旅管理系": "人文暨管理學院",
    "水產養殖系": "海洋資源暨工程學院", "海洋遊憩系": "海洋資源暨工程學院",
    "食品科學系": "海洋資源暨工程學院",
    "資訊工程系": "電資工程學院", "電信工程系": "電資工程學院",
    "電機工程系": "電資工程學院",
}

def apply_cjk_font():
    """設定中文字型，支援 Windows, macOS, Linux"""
    system = platform.system()
    if system == "Windows":
        font_list = ["Microsoft JhengHei", "Microsoft YaHei"]
    elif system == "Darwin": # macOS
        font_list = ["Heiti TC", "Arial Unicode MS"]
    else: # Linux
        font_list = ["Noto Sans CJK TC", "WenQuanYi Zen Hei"]
    
    plt.rcParams["font.sans-serif"] = font_list + plt.rcParams["font.sans-serif"]
    plt.rcParams["axes.unicode_minus"] = False

def load_student_data(zip_path: Path) -> pd.DataFrame:
    """
    從 ZIP 讀取多個 CSV，整合成一個 DataFrame。
    欄位包含：學年, 學院, 系所
    """
    records = []
    if not zip_path.exists():
        raise FileNotFoundError(f"找不到檔案: {zip_path}")

    with zipfile.ZipFile(zip_path) as z:
        for filename in z.namelist():
            if not filename.endswith(".csv"):
                continue
            
            # 取得年度
            year = int(filename[:3])
            
            # 讀取內容
            content = z.read(filename).decode("utf-8-sig")
            reader = csv.DictReader(io.StringIO(content))
            
            for row in reader:
                dept = row.get("系所名稱", "").strip()
                if not dept:
                    continue
                records.append({
                    "學年": year,
                    "學院": DEPT_TO_COLLEGE.get(dept, "其他"),
                    "系所": dept
                })
    
    return pd.DataFrame.from_records(records)

def plot_college_trends(df: pd.DataFrame, output_path: Path = None):
    """繪製學院生源分析圖並存檔"""
    # 準備統計數據
    pivot = df.groupby(["學年", "學院"]).size().reset_index(name="人數")
    
    # 設定 Seaborn 主題
    sns.set_theme(style="whitegrid", font_scale=1.2)
    apply_cjk_font()
    
    fig, axes = plt.subplots(1, 2, figsize=(16, 8))
    
    # 圖 A：折線圖 (趨勢)
    sns.lineplot(data=pivot, x="學年", y="人數", hue="學院", marker="o", markersize=8, ax=axes[0])
    axes[0].set_title("109-114 學年各學院人數趨勢")
    
    # 為折線圖標上數字
    for _, row in pivot.iterrows():
        axes[0].annotate(f'{int(row["人數"])}', 
                         (row["學年"], row["人數"]),
                         textcoords="offset points", 
                         xytext=(0, 10), 
                         ha='center', 
                         fontsize=10)
    
    # 圖 B：堆疊長條圖 (結構)
    pivot_wide = pivot.pivot(index="學年", columns="學院", values="人數").fillna(0)
    pivot_wide.plot(kind="bar", stacked=True, ax=axes[1], alpha=0.8, edgecolor="white")
    axes[1].set_title("各學年學院結構占比")
    axes[1].set_ylabel("人數")
    axes[1].tick_params(axis='x', rotation=0)
    
    # 為堆疊長條圖標上數字
    for container in axes[1].containers:
        # 只在高度大於 0 的時候標註，避免數字重疊
        labels = [f'{int(v):d}' if v > 0 else '' for v in container.datavalues]
        axes[1].bar_label(container, labels=labels, label_type='center', fontsize=10, color='white', fontweight='bold')
    
    plt.tight_layout()
    
    if output_path:
        fig.savefig(output_path, dpi=150, bbox_inches="tight")
        print(f"圖表已儲存至: {output_path}")
    
    return fig

def main():
    HERE = Path(__file__).resolve().parent
    ZIP_PATH = HERE.parents[3] / "assets" / "npu-stu-109-114-anon.zip"
    OUTPUT_IMG = HERE / "college_trend_result.png"

    print("正在讀取資料...")
    df = load_student_data(ZIP_PATH)
    
    print("正在繪製圖表...")
    plot_college_trends(df, OUTPUT_IMG)
    # plt.show() # 在 CLI 環境通常不直接 show

if __name__ == "__main__":
    main()
