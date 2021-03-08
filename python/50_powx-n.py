class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.__pow(x, n)


    def __pow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        pow_n_2 = self.__pow(x, abs(n) // 2)
        pow_n = pow_n_2 * pow_n_2
        if n % 2 == 1:
            pow_n = pow_n * x

        return pow_n if n > 0 else 1 / pow_n


if __name__ == "__main__":
    solution = Solution()
    print(solution.myPow(2.00000, 10))
    print(solution.myPow(2.10000, 3))
    print(solution.myPow(2.00000, -2))
