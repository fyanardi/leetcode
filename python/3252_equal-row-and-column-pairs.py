class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        rows: dict[int, list[int]] = {}
        count: int = 0

        for i in range(n):
            h = hash(tuple(grid[i]))
            if h not in rows:
                rows[h] = []
            rows[h].append(i)

        for i in range(n):
            column: list[int] = []
            for j in range(n):
                column.append(grid[j][i])
            h = hash(tuple(column))
            if h in rows:
                count += len(rows[h])

        return count


if __name__ == "__main__":
    solution = Solution()

    assert solution.equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]) == 1
    assert solution.equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]) == 3
