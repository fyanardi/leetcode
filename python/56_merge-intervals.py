class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        n = len(intervals)
        if n <= 1:
            return intervals

        intervals = sorted(intervals)
        merged: list[list[int]] = []
        interval = intervals[0]

        for i in range(1, n):
            # interval[0] is guaranteed to be the minimum since intervals are already sorted
            if interval[1] >= intervals[i][0]:
                interval = [interval[0], max(interval[1], intervals[i][1])]
            else:
                merged.append(interval)
                interval = intervals[i]

        merged.append(interval)

        return merged


if __name__ == "__main__":
    solution = Solution()
    assert solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert solution.merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert solution.merge([[4, 7], [1, 4]]) == [[1, 7]]
