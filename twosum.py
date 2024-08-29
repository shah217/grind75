from typing import List

# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []

def main():
    # Test cases for the two_sum function
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1])
    ]
    
    sol = Solution()
    for nums, target, expected in test_cases:
        result = sol.twoSum(nums, target)
        print(f"Test case: nums={nums}, target={target}")
        print(f"Expected: {expected}, Got: {result}")
        assert result == expected, f"Expected {expected} but got {result}"
    print("All test cases passed successfully.")

if __name__ == "__main__":
    main()
    

if __name__ == "__main__":
    main()