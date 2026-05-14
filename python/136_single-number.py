class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        x = 0
        for n in nums:
            x ^= n
        return x


if __name__ == "__main__":
    solution = Solution()
    assert solution.singleNumber([2, 2, 1]) == 1
    assert solution.singleNumber([4, 1, 2, 1, 2]) == 4
    assert solution.singleNumber([1]) == 1
