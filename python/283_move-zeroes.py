class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i is a pointer to current position that is non-zero, be it the original or after shiting
        i = 0
        # j is a pointer to the position being evaluated for non-zeroness
        j = 0
        while j < len(nums):
            # if non-zero, move the value at j to the current i
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            # always increment j
            j += 1

        # zeroize the remaining positions after shifting
        for k in range(i, len(nums)):
            nums[k] = 0


if __name__ == "__main__":
    solution = Solution()
    nums = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]

    nums = [0]
    solution.moveZeroes(nums)
    assert nums == [0]

    nums = [1, 3, 12]
    solution.moveZeroes(nums)
    assert nums == [1, 3, 12]

    nums = [0, 1, 0, 3, 0, 12, 0]
    solution.moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0, 0, 0]
