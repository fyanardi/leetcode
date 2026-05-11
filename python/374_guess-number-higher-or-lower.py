# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

pick = -1

def guess(num: int) -> int:
    global pick
    if num == pick:
        return 0
    elif num > pick:
        return -1
    else:
        return 1


class Solution:
    def guessNumber(self, n: int) -> int:
        start = 0
        end = n

        num = (start + end) // 2

        while start <= end:
            g = guess(num)
            if g == 0:
                return num
            elif g == -1:
                end = num - 1
            elif g == 1:
                start = num + 1
            num = (start + end) // 2
            g = guess(num)

        return -1


if __name__ == "__main__":
    solution = Solution()

    pick = 6
    assert solution.guessNumber(10) == 6

    pick = 1
    assert solution.guessNumber(1) == 1

    pick = 1
    assert solution.guessNumber(1) == 1
