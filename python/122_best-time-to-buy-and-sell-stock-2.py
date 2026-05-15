class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        buy: list[int] = [0] * n
        sell: list[int] = [0] * n

        buy[0] = -prices[0]
        sell[0] = 0

        for i in range(1, n):
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
            buy[i] = max(buy[i-1], sell[i-1] - prices[i], sell[i] - prices[i])

        return sell[n-1]


if __name__ == "__main__":
    solution = Solution()

    assert solution.maxProfit(prices=[7, 1, 5, 3,6, 4]) == 7
    assert solution.maxProfit(prices=[1, 2, 3, 4, 5]) == 4
    assert solution.maxProfit(prices=[7, 6, 4, 3, 1]) == 0
