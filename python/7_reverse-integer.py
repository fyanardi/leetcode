class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2 ** 31 - 1
        n = x if x >= 0 else -x
        rev = 0
        m = 1
        while n > 0:
            if rev != 0 and max_int / rev < 10:
                return 0
            rev = rev * 10
            mod = n % 10
            if (x > 0 and max_int - rev < mod) or (x < 0 and max_int - rev + 1 < mod):
                return 0
            rev = rev + mod
            n = n // 10
        return rev if x > 0 else -rev


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(123))
    print(solution.reverse(-123))
    print(solution.reverse(120))
    print(solution.reverse(0))
    # max int: 2147483647, min int: -2147483648
    print(solution.reverse(7463847412)) # reversed to max int -> no overflow
    print(solution.reverse(8463847412)) # reversed to max int + 1 -> overflow
    print(solution.reverse(6463847412)) # reversed to max int - 1 -> no overflow
    print(solution.reverse(-8463847412)) # reversed to min int -> no overflow
    print(solution.reverse(-9463847412)) # reversed to min int - 1 -> overflow
    print(solution.reverse(-7463847412)) # reversed to min int + 1 -> no overflow
