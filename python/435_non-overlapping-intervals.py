class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        if n <= 1:
            return 0

        erase = 0
        intervals = sorted(intervals)

        # end of the current interval with all previous intervals already non-overlapping
        min_end = intervals[0][1]

        for i in range(1, n):
            if intervals[i][0] >= min_end:
                min_end = intervals[i][1]
            else:
                erase += 1
                # minimize the end of the interval to reduce the chance of overlapping with the next
                min_end = min(min_end, intervals[i][1])

        return erase


if __name__ == "__main__":
    solution = Solution()
    assert solution.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert solution.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert solution.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
    assert solution.eraseOverlapIntervals([[1, 100], [11, 22], [1, 11], [2, 12]]) == 2
    assert solution.eraseOverlapIntervals([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]) == 2
    assert solution.eraseOverlapIntervals([
        [-52, 31], [-73, -26], [82, 97], [-65, -11], [-62, -49], [95, 99], [58, 95], [-31, 49],
        [66, 98], [-63, 2], [30, 47], [-40, -26]
    ]) == 7
