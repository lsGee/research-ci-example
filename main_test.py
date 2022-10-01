import unittest

import main  # internal module


class MainTest(unittest.TestCase):
    def test_helloworld(self):
        ret = main.helloworld("sj")
        self.assertEqual(ret, "Hello World! sj")


if __name__ == "__main__":
    unittest.main()  # 실행 시, 유닛테스트 통과
