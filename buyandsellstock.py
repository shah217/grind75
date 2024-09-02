from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit  = 0
        l = 0
        r = 1
        
        while r < len(prices):
            if prices[r] > prices[l]:
                tmp  = prices[r] - prices[l]
                profit = max(tmp, profit)
            else:
                l = r
            r = r + 1
            
        return profit

def main():
    # Test cases for the maxProfit function
    test_cases = [
        ([0, 9, 1, 2, 3, 9], 9)
        # ([7, 1, 5, 3, 6, 4], 5),
        # ([7, 6, 4, 3, 1], 0),
        # ([1, 2], 1),
        # ([2, 1], 0)
    ]
    
    sol = Solution()
    for prices, expected in test_cases:
        result = sol.maxProfit(prices)
        print(f"Test case: {prices}")
        print(f"Expected: {expected}, Got: {result}")
        assert result == expected, f"Expected {expected} but got {result}"
    
    
    print("All test cases passed successfully.")

if __name__ == "__main__":
    main()