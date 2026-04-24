# Week 01 先備知識 - 簡單好記版本
# 學生：1114405035 賴彥廷

# 1. 變數、型別與容器
name = "小明"
scores = [80, 90, 70]
data = {"姓名": name, "分數": scores}

# 2. 函式與迴圈 (計算平均)
def get_avg(lst):
    # 使用 sum() 和 len()
    return sum(lst) / len(lst)

# 3. 格式化輸出
avg = get_avg(scores)
print(f"{name} 的平均分數是: {avg:.1f}")

# 4. 推導式 (過濾出大於 75 的分數)
high_scores = [s for s in scores if s > 75]
print(f"高分項目: {high_scores}")

# 5. 排序 (由大到小)
sorted_scores = sorted(scores, reverse=True)
print(f"排序後: {sorted_scores}")

# 6. 例外處理
try:
    x = 10 / 0
except ZeroDivisionError:
    print("不能除以零！")
