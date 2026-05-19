class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        from collections import deque

        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    # Each entry in the queue is a nested tuple ((row, column), level)
                    q.append(((i, j), 0))

        level = 0
        while len(q) > 0:
            orange, l = q.popleft()

            row, column = orange
            # it's possible that the same orange is visited by more than one different rotten oranges
            if visited[row][column]:
                continue

            # only assign level once it's confirmed that this orange has not been visited before
            level = l
            visited[row][column] = True

            if row > 0:
                if grid[row-1][column] == 1 and not visited[row-1][column]:
                    q.append(((row-1, column), level+1))
            if row < m-1:
                if grid[row+1][column] == 1 and not visited[row+1][column]:
                    q.append(((row+1, column), level+1))
            if column > 0:
                if grid[row][column-1] == 1 and not visited[row][column-1]:
                    q.append(((row, column-1), level+1))
            if column < n-1:
                if grid[row][column+1] == 1 and not visited[row][column+1]:
                    q.append(((row, column+1), level+1))

        # fresh = 0
        # find any unvisited fresh orange
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    return -1

        return level


if __name__ == "__main__":
    solution = Solution()

    assert solution.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert solution.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert solution.orangesRotting([[0, 2]]) == 0
    assert solution.orangesRotting([[0]]) == 0
    assert solution.orangesRotting([[1], [2]]) == 1
    assert solution.orangesRotting([[2, 2], [1, 1], [0, 0], [2, 0]]) == 1
