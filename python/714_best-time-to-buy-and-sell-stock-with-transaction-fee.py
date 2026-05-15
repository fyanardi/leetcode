class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        n = len(prices)
        buy: list[int] = [0] * n
        sell: list[int] = [0] * n

        buy[0] = -prices[0] - fee
        sell[0] = 0

        for i in range(1, n):
            buy[i] = max(buy[i-1], sell[i-1] - prices[i] - fee)
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])

        return sell[n-1]


if __name__ == "__main__":
    solution = Solution()

    assert solution.maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2) == 8
    assert solution.maxProfit(prices=[1, 3, 7, 5, 10, 3], fee = 3) == 6
