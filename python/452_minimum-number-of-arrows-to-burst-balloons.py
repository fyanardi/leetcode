class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 1:
            return n

        points = sorted(points)
        current_overlap = points[0]
        shots = 1

        for i in range(1, n):
            overlap = [max(current_overlap[0], points[i][0]), min(current_overlap[1], points[i][1])]
            if overlap[0] <= overlap[1]:
                current_overlap = overlap
            else:
                # not overlapping, increase number of shots by 1
                current_overlap = points[i]
                shots += 1

        return shots


if __name__ == "__main__":
    solution = Solution()
    assert solution.findMinArrowShots([[10, 16], [2, 8],[1, 6], [7, 12]]) == 2
    assert solution.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
    assert solution.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
