import unittest
import functools
import time
from timeit_benchmark import parse_csv, parse_json, parse_xml, timeit

class TestTimeitBenchmark(unittest.TestCase):

    def test_parsers_data_integrity(self):
        """測試三種解析器是否能正確還原原始數據"""
        # 準備小型測試資料
        csv_data = "id,name,score\n1,Alice,90\n2,Bob,85"
        json_data = '[{"id": "1", "name": "Alice", "score": "90"}, {"id": "2", "name": "Bob", "score": "85"}]'
        xml_data = '<data><row id="1" name="Alice" score="90"/><row id="2" name="Bob" score="85"/></data>'
        
        expected = [
            {"id": "1", "name": "Alice", "score": "90"},
            {"id": "2", "name": "Bob", "score": "85"}
        ]
        
        # 這裡會觸發裝飾器的 print，但在測試中我們主要檢查回傳值
        self.assertEqual(parse_csv(csv_data), expected)
        self.assertEqual(parse_json(json_data), expected)
        self.assertEqual(parse_xml(xml_data), expected)

    def test_decorator_metadata(self):
        """測試裝飾器是否正確保留了被裝飾函式的元數據 (__name__)"""
        @timeit
        def my_test_function():
            """這是一個測試說明"""
            return True
        
        self.assertEqual(my_test_function.__name__, "my_test_function")
        self.assertEqual(my_test_function.__doc__, "這是一個測試說明")
        self.assertTrue(my_test_function())

    def test_decorator_execution(self):
        """測試裝飾器是否確實執行了函式"""
        state = {"called": False}
        
        @timeit
        def mark_called():
            state["called"] = True
            
        mark_called()
        self.assertTrue(state["called"])

if __name__ == "__main__":
    unittest.main()
