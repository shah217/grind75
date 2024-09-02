from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
            
        return True

        
    

def main():
    # Test cases for the isPalindrome function
    test_cases = [
        ("race a car", False),
        ("A man, a plan, a canal: Panama", True),
        (" ", True),
        ("0P", False)
    ]   
    sol = Solution()
    for s, expected in test_cases:
        result = sol.isPalindrome(s)
        print(f"Test case: {s}")
        print(f"Expected: {expected}, Got: {result}")
        assert result == expected, f"Expected {expected} but got {result}"
    
    print("All test cases passed successfully.")

if __name__ == "__main__":
    main()