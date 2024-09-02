from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        S = {}
        T = {}
        
        for i in range(len(s)):
            S[s[i]] = 1 + S.get(s[i], 0)
            T[t[i]] = 1 + T.get(t[i], 0)
            
        for c in S:
            if S[c] != T.get(c,0):
                return False
            
        return True

        
    

def main():
    # Test cases for the isPalindrome function
    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("", "", True)
    ]
    sol = Solution()
    for s, t, expected in test_cases:
        result = sol.isAnagram(s, t)
        print(f"Test case: s={s}, t={t}")
        print(f"Expected: {expected}, Got: {result}")
        assert result == expected, f"Expected {expected} but got {result}"
    
    print("All test cases passed successfully.")

if __name__ == "__main__":
    main()