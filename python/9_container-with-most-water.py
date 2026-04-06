class Solution:
    def maxArea(self, height: list[int]) -> int:
        if len(height) <= 1:
            return 0

        i = 0
        j = len(height) - 1

        max_volume = 0

        while i < j:
            volume = (j - i) * min(height[i], height[j])
            max_volume = max(max_volume, volume)

            # advance the position with lower height (lower height determines the volume)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_volume


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert solution.maxArea([1,1]) == 1
    assert solution.maxArea([1]) == 0
    assert solution.maxArea([*list(range(0, 10001)), *list(range(9999, 0, -1))]) == 50000000
