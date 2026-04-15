class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        max_altitude = 0
        altitude = 0

        for g in gain:
            altitude += g
            max_altitude = max(max_altitude, altitude)

        return max_altitude


if __name__ == "__main__":
    solution = Solution()
    assert solution.largestAltitude([-5, 1, 5, 0, -7]) == 1
    assert solution.largestAltitude([-4, -3, -2, -1, 4, 2, 2]) == 0
