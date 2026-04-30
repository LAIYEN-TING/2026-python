import unittest
import zipfile
import tempfile
import io
from pathlib import Path
from student_stats import process_student_zip, generate_markdown_report

class TestStudentStats(unittest.TestCase):
    def setUp(self):
        # 建立一個暫時的 ZIP 檔供測試使用
        self.test_dir = tempfile.TemporaryDirectory()
        self.zip_path = Path(self.test_dir.name) / "test_data.zip"
        
        # 準備模擬資料
        csv_content_109 = "系所名稱,入學方式\n資訊工程系,甄選入學\n資訊工程系,聯合登記分發\n電子工程系,甄選入學\n"
        csv_content_110 = "系所名稱,入學方式\n資訊工程系,甄選入學\n機械工程系,技優甄審\n"
        
        with zipfile.ZipFile(self.zip_path, 'w') as z:
            # 加入 BOM 以模擬真實情況
            z.writestr("109_data.csv", "\ufeff" + csv_content_109)
            z.writestr("110_data.csv", "\ufeff" + csv_content_110)

    def tearDown(self):
        self.test_dir.cleanup()

    def test_process_student_zip(self):
        """測試是否能正確解析 ZIP 並統計人數"""
        summary = process_student_zip(self.zip_path)
        
        # 檢查年度是否正確
        self.assertIn("109", summary)
        self.assertIn("110", summary)
        
        # 檢查 109 年統計
        self.assertEqual(summary["109"]["total"], 3)
        self.assertEqual(summary["109"]["by_dept"]["資訊工程系"], 2)
        self.assertEqual(summary["109"]["by_dept"]["電子工程系"], 1)
        
        # 檢查 110 年統計
        self.assertEqual(summary["110"]["total"], 2)

    def test_generate_markdown_report(self):
        """測試 Markdown 報告生成格式"""
        summary = process_student_zip(self.zip_path)
        report = generate_markdown_report(summary)
        
        self.assertIn("# 6 屆新生概況報告", report)
        self.assertIn("| 109 | 3 | 資訊工程系 (2) |", report)
        self.assertIn("| 110 | 2 | 資訊工程系 (1) |", report)

if __name__ == "__main__":
    unittest.main()
