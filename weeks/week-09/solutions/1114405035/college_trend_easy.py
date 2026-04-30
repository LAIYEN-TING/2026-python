import zipfile
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 這個版本採用最直觀的 Pandas 寫法，適合初學者快速上手數據視覺化
# 記憶重點：pd.read_csv 搭配 zipfile，以及 df.plot() 直接出圖

# 1. 準備對照表
MAPPING = {
    "資訊工程系": "電資學院", "電信工程系": "電資學院", "電機工程系": "電資學院",
    "水產養殖系": "海資學院", "海洋遊憩系": "海資學院", "食品科學系": "海資學院",
    "應用外語系": "人管學院", "航運管理系": "人管學院", "行銷與物流管理系": "人管學院",
    "觀光休閒系": "人管學院", "資訊管理系": "人管學院", "餐旅管理系": "人管學院",
}

def main():
    # 2. 設定路徑
    HERE = Path(__file__).resolve().parent
    ZIP_PATH = HERE.parents[3] / "assets" / "npu-stu-109-114-anon.zip"
    
    if not ZIP_PATH.exists():
        print("找不到資料檔")
        return

    # 3. 讀取資料並整合
    all_data = []
    with zipfile.ZipFile(ZIP_PATH) as z:
        for name in z.namelist():
            if name.endswith(".csv"):
                # 直接用 pandas 讀取 zip 裡的檔案
                with z.open(name) as f:
                    # encoding 使用 utf-8-sig 處理 BOM
                    temp_df = pd.read_csv(f, encoding="utf-8-sig")
                    # 加上學年欄位 (檔名開頭三碼)
                    temp_df["學年"] = name[:3]
                    all_data.append(temp_df)
    
    # 合併所有年度資料
    df = pd.concat(all_data, ignore_index=True)
    
    # 4. 資料轉換：將系所轉成學院
    df["學院"] = df["系所名稱"].map(MAPPING).fillna("其他")
    
    # 5. 製作樞紐分析表 (學年為橫軸，學院為欄，計算人數)
    # 這是最簡單的出圖準備方式
    report = df.groupby(["學年", "學院"]).size().unstack(fill_value=0)
    
    print("--- 統計簡表 ---")
    print(report)

    # 6. 繪圖 (設定字型以支援中文)
    plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei", "Heiti TC", "sans-serif"]
    plt.rcParams["axes.unicode_minus"] = False
    
    # 直接用 pandas 的 plot 功能畫出堆疊長條圖，簡單好記
    ax = report.plot(kind="bar", stacked=True, figsize=(10, 6), title="109-114 學年各學院生源結構")
    ax.set_ylabel("人數")
    plt.xticks(rotation=0) # 讓年份橫著放
    
    # 7. 存檔
    output_path = HERE / "college_trend_easy.png"
    plt.savefig(output_path, dpi=120)
    print(f"\n視覺化圖表已完成並存檔：{output_path.name}")

if __name__ == "__main__":
    main()
