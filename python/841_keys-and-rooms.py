class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        # 2 <= n <= 1000, rooms[0] is guaranteed to be valid

        # use array of boolean to keep track of visited rooms
        #visited = [False] * len(rooms)
        #keys = [0]

        #while len(keys) > 0:
        #    key = keys.pop()

        #    if not visited[key]:
        #        visited[key] = True
        #        keys.extend(rooms[key])

        #return len([v for v in visited if v is False]) == 0

        # alternative version using bits to keep track of visited rooms
        visited = [False] * len(rooms)
        all_visited = (1 << len(rooms)) - 1
        visited = 0
        keys = [0]

        while len(keys) > 0:
            key = keys.pop()
            mask = 1 << key

            if (visited & mask) == 0:
                visited = visited | mask
                keys.extend(rooms[key])

                if visited == all_visited:
                    return True

        return visited == all_visited


if __name__ == "__main__":
    solution = Solution()

    assert solution.canVisitAllRooms([[1], [2], [3], []]) == True
    assert solution.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]) == False
