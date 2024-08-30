from typing import List
import unittest
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        # Iterate through the range from 0 to len(nums) + 1 (which is n+1).
        # This loop calculates the sum of all numbers in the range [0, n].
        for value in range(0, len(nums) + 1):
            result += value
        
        # Subtract each number in the nums array from the result.
        # After this loop, result will hold the value of the missing number.
        for num in nums:
            result -= num
        
        # Return the missing number.
        return result

class TestSolution(unittest.TestCase):
    def test_missingNumber(self):
        # Table of test cases
        test_cases = [
            {"input": [3, 0, 1], "expected": 2},
            {"input": [0, 1], "expected": 2},
            {"input": [9, 6, 4, 2, 3, 5, 7, 0, 1], "expected": 8},
            {"input": [0], "expected": 1},
            {"input": [1, 2], "expected": 0},
            {"input": [2, 0, 3], "expected": 1},
            {"input": [1, 0], "expected": 2},
        ]
        
        solution = Solution()
        
        for case in test_cases:
            with self.subTest(case=case):
                self.assertEqual(solution.missingNumber(case["input"]), case["expected"])

if __name__ == '__main__':
    unittest.main()