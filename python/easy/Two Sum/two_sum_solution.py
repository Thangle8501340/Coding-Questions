from typing import List
import unittest
class Solution:
    # twoSum - returns 2 numbers from list  (nums) that matches int (target)
    # input - nums: List[int] = the list of integers , target:int = the target to match
    # output - List[int] = a list containing 2 numbers that matches target
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hashmap = {}
        for index,value in enumerate(nums):
            if value in nums_hashmap:
                return [nums_hashmap[value], index]
            else:
                nums_hashmap[target - value] = index


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_two_sum(self):
        test_cases = [
            {"input": ([2, 7, 11, 15], 9), "expected": [0, 1]},
            {"input": ([3, 2, 4], 6), "expected": [1, 2]},
            {"input": ([3, 3], 6), "expected": [0, 1]},
            {"input": ([1000000000, -1000000000, 0], 0), "expected": [0, 1]},
            {"input": ([-1, -2, -3, -4, -5], -8), "expected": [2, 4]},
            {"input": ([1, 2, 3], 7), "expected": None},  
            {"input": ([1], 2), "expected": None}, 
            {"input": ([], 0), "expected": None},  
        ]

        for case in test_cases:
            with self.subTest(case=case):
                nums, target = case["input"]
                expected = case["expected"]
                result = self.solution.twoSum(nums, target)
                self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()