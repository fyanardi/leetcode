class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)

        days = [0] * n
        # stack containing temperatures in increasing order of temperature & index
        # (top of the stack is the lowest temperature & index)
        higher_temps = [(temperatures[n-1], n-1)]

        for i in range(n-1, -1, -1):
            for j in range(len(higher_temps)-1, -1, -1):
                if temperatures[i] >= higher_temps[j][0]:
                    # remove temperature lower than the current temperature
                    higher_temps.pop()
                else:
                    days[i] = higher_temps[j][1] - i
                    higher_temps.append((temperatures[i], i))
                    break

            if len(higher_temps) == 0:
                higher_temps.append((temperatures[i], i))

        return days


if __name__ == "__main__":
    solution = Solution()
    assert solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert solution.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert solution.dailyTemperatures([30, 60, 90]) == [1, 1, 0]
