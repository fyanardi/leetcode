class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occurrences: dict[int, int] = {}
        for v in arr:
            if v not in occurrences:
                occurrences[v] = 1
            else:
                occurrences[v] += 1

        return len(list(occurrences.values())) == len(set(occurrences.values()))


if __name__ == "__main__":
    solution = Solution()

    assert solution.uniqueOccurrences([1, 2, 2, 1, 1, 3]) == True
    assert solution.uniqueOccurrences([1, 2]) == False
    assert solution.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]) == True
