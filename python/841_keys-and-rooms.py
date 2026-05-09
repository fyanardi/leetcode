class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        # 2 <= n <= 1000, rooms[0] is guaranteed to be valid
        visited = [False] * len(rooms)
        keys = [0]

        while len(keys) > 0:
            key = keys.pop()

            if not visited[key]:
                visited[key] = True
                keys.extend(rooms[key])

        return len([v for v in visited if v is False]) == 0


if __name__ == "__main__":
    solution = Solution()

    assert solution.canVisitAllRooms([[1], [2], [3], []]) == True
    assert solution.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]) == False
