class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = 10001

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit


if __name__ == "__main__":
    solution = Solution()

    assert solution.maxProfit(prices=[7, 1, 5, 3, 6, 4]) == 5
    assert solution.maxProfit(prices=[7, 6, 4, 3, 1]) == 0
