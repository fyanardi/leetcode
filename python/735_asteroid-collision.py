class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        result = []

        for a in asteroids:
            # first asteroid
            if len(result) == 0:
                result.append(a)
            else:
                # collision - only when previous asteroid is heading right and current one is heading left
                if a < 0:
                    # whether to finally append current asteroid, depending on the last collision
                    append_a = True
                    while len(result) > 0 and result[-1] > 0:
                        if -a > result[-1]:
                            # a is bigger, whether to append a depends on the previous asteroid's size
                            result.pop()
                            append_a = True
                        elif -a == result[-1]:
                            # equal size, both discarded
                            result.pop()
                            append_a = False
                            break
                        else:
                            # a is smaller, keep previous asteroid, discard a
                            append_a = False
                            break
                    if append_a:
                        result.append(a)
                else:
                    result.append(a)

        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.asteroidCollision([5, 10, -5]) == [5, 10]
    assert solution.asteroidCollision([8, -8]) == []
    assert solution.asteroidCollision([10, 2, -5]) == [10]
    assert solution.asteroidCollision([3, 5, -6, 2, -1, 4]) == [-6, 2, 4]
    assert solution.asteroidCollision([-2,-1,1,2]) == [-2, -1, 1, 2]
