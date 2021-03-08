class Solution:
    def fib(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1

        f_2 = 0
        f_1 = 1
        f_n = 0
        for i in range(2, n + 1):
            f_n = f_1 + f_2
            f_2 = f_1
            f_1 = f_n

        return f_n


if __name__ == "__main__":
    solution = Solution()
    print('f(2):', solution.fib(2)) # 1
    print('f(3):', solution.fib(3)) # 2
    print('f(4):', solution.fib(4)) # 3
    print('f(10):', solution.fib(10)) # 55
    print('f(20):', solution.fib(20)) # 6765

