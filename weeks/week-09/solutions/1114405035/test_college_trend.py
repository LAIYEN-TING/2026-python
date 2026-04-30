import unittest
import zipfile
import tempfile
import pandas as pd
from pathlib import Path
from college_trend import load_student_data, DEPT_TO_COLLEGE

class TestCollegeTrend(unittest.TestCase):
    def setUp(self):
        # 建立臨時測試環境
        self.test_dir = tempfile.TemporaryDirectory()
        self.zip_path = Path(self.test_dir.name) / "test_students.zip"
        
        # 模擬兩年的 CSV 資料
        # 109年：資工(電資)、養殖(海資)、不存在系所(其他)
        csv_109 = "系所名稱,性別\n資訊工程系,1\n水產養殖系,2\n未知系所,1\n"
        # 110年：應外(人管)
        csv_110 = "系所名稱,性別\n應用外語系,1\n"
        
        with zipfile.ZipFile(self.zip_path, 'w') as z:
            z.writestr("109_stu.csv", "\ufeff" + csv_109)
            z.writestr("110_stu.csv", "\ufeff" + csv_110)

    def tearDown(self):
        self.test_dir.cleanup()

    def test_load_student_data(self):
        """測試資料讀取與學院對照邏輯"""
        df = load_student_data(self.zip_path)
        
        # 1. 檢查 DataFrame 基本屬性
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 4) # 109(3人) + 110(1人)
        
        # 2. 檢查學院對照是否正確
        # 資訊工程系 -> 電資工程學院
        self.assertTrue((df[df["系所"] == "資訊工程系"]["學院"] == "電資工程學院").all())
        # 未知系所 -> 其他
        self.assertTrue((df[df["系所"] == "未知系所"]["學院"] == "其他").all())
        # 應用外語系 -> 人文暨管理學院
        self.assertTrue((df[df["系所"] == "應用外語系"]["學院"] == "人文暨管理學院").all())
        
        # 3. 檢查年度是否正確抓取 (前三碼)
        self.assertEqual(df["學年"].unique().tolist(), [109, 110])

    def test_dept_to_college_mapping(self):
        """測試核心字典內容"""
        self.assertEqual(DEPT_TO_COLLEGE["資訊工程系"], "電資工程學院")
        self.assertEqual(DEPT_TO_COLLEGE["水產養殖系"], "海洋資源暨工程學院")

if __name__ == "__main__":
    unittest.main()
