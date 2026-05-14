class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        money: list[int] = [0] * n
        max_money = 0

        for i in range(n - 1, -1, -1):
            if i + 2 > n - 1:
                money[i] = nums[i]
            else:
                # find the max money that can be obtained by robbing houses starting at i + 2
                for j in range(i + 2, n):
                    money[i] = max(money[i], money[j])
                # and include money obtained from robbing house i itself
                money[i] += nums[i]

            max_money = max(max_money, money[i])

        return max_money


if __name__ == "__main__":
    solution = Solution()

    assert solution.rob([1, 2, 3, 1]) == 4
    assert solution.rob([2, 7, 9, 3, 1]) == 12
