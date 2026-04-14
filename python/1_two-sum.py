class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indices = {}
        for i in range(len(nums)):
            n1 = nums[i]
            n2 = target - n1
            if n2 in indices:
                return [i, indices[n2]]
            indices[n1] = i
        return []

