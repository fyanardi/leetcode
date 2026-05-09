class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        # build a structure to represent list of connected cities from every city
        # this will be used to traverse the connectivity graph
        city_connectivity: dict[int, list[int]] = {}

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i != j and isConnected[i][j]:
                    if i not in city_connectivity:
                        city_connectivity[i] = []
                    city_connectivity[i].append(j)

        province = 0
        visited = [False] * len(isConnected)

        for i in range(len(isConnected)):
            if visited[i]:
                continue

            cities = [i]
            while len(cities) > 0:
                city = cities.pop()

                if visited[city]:
                    continue

                visited[city] = True

                if city in city_connectivity:
                    cities.extend(city_connectivity[city])

            province += 1

        return province



if __name__ == "__main__":
    solution = Solution()

    assert solution.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    assert solution.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
    assert solution.findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]) == 1
