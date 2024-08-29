class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack


def main():
    # Test the function
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True)
    ]
    
    sol = Solution()
    for s, expected in test_cases:
        result = sol.isValid(s)
        print(f"Test case: {s}")
        print(f"Expected: {expected}, Got: {result}")
        assert result == expected, f"Expected {expected} but got {result}"
    print("All test cases passed successfully.")


if __name__ == "__main__":
    main()