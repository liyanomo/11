import unittest
from bubble import merge_sort

class TestListElements(unittest.TestCase):

    def test_list_eq(self):
        actual_res = merge_sort([10,6,35,2,12,24,25,16])
        expected_res =[2, 6, 10, 12, 16, 24, 25, 35]
        self.assertListEqual(actual_res, expected_res)

    def test_list_eq2(self):
        expected_res =[3,10,24,36,45]
        a = [10,45,36,24,3]
        actual_res = merge_sort(a)
        self.assertEqual(actual_res, expected_res)

if __name__ == "__main__":
    unittest.main()