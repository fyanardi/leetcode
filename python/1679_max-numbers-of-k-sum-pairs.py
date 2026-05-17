class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)
        i = 0
        j = n - 1

        nums = sorted(nums)
        operations = 0

        while i < j:
            sum = nums[i] + nums[j]
            if sum == k:
                operations += 1
                i += 1
                j -= 1
            elif sum > k:
                j -= 1
            else:
                i += 1

        return operations


if __name__ == "__main__":
    solution = Solution()

    assert solution.maxOperations(nums=[1, 2, 3, 4], k=5) == 2
    assert solution.maxOperations(nums=[3, 1, 3, 4, 3], k=6) == 1
