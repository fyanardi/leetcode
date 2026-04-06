class Solution:
    def maxArea(self, height: list[int]) -> int:
        if len(height) <= 1:
            return 0

        max_volume = 0
        for i in range(len(height) - 1):
            if height[i] == 0:
                continue

            # skip j where it is not possible to have volume greater than the current max volume
            skip = 1
            if height[i] < max_volume:
                skip = -( -max_volume // height[i])

            for j in range(i + skip, len(height)):
                if height[j] == 0:
                    continue

                volume = min(height[i], height[j]) * (j - i)
                max_volume = max(max_volume, volume)

        return max_volume


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert solution.maxArea([1,1]) == 1
    assert solution.maxArea([1]) == 0
