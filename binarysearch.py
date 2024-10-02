from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bottom = 0
        top = len(nums) -1
        
        while bottom < top :
            mid = ((top - bottom) // 2) + bottom
            

            
            if nums[mid] == target:
                return mid
            
            if mid == top or mid == bottom:
                return -1
            
            if nums[mid] > target:
                top = mid - 1
            else:
                bottom = mid + 1
        return -1 


def main():
    # Test cases for the search function
    test_cases = [
        ([-1,0,3,5,9,12], 9, 4),
        ([-1,0,3,5,9,12], 2, -1),
        ([1], 0, -1)
    ]
    
    sol = Solution()
    for nums, target, expected in test_cases:
        result = sol.search(nums, target)
        print(f"Test case: nums={nums}, target={target}")
        print(f"Expected: {expected}, Got: {result}")
        assert result == expected, f"Expected {expected} but got {result}"

    
    print("All test cases passed successfully.")

if __name__ == "__main__":
    main()