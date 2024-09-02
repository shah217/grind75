from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        test_set = set()
        
        for i in nums:
            if i in test_set:
                return True
            test_set.add(i)
            
        return False
    

def main():
    # Test cases for the containsDuplicate function
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)
    ]
    
    sol = Solution()
    
    for nums, expected in test_cases:
        result = sol.containsDuplicate(nums)
        print(f"Test case: {nums}")
        print(f"Expected: {expected}, Got: {result}")
        assert result == expected, f"Expected {expected} but got {result}"
    
    print("All test cases passed successfully.")

if __name__ == "__main__":
    main()