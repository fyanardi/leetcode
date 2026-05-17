class StockSpanner:

    def __init__(self):
        self.stocks: list[tuple[int, int]] = []

    def next(self, price: int) -> int:
        n = len(self.stocks)
        lte_count = 1
        for i in range(n-1, -1, -1):
            if self.stocks[i][0] <= price:
                lte_count += self.stocks[i][1]
                self.stocks.pop()
            else:
                break

        self.stocks.append((price, lte_count))

        return lte_count


def execute_test_case(actions: list[str], params: list[list[int]], output: list[int | None]):
    stock_spanner = None
    for i in range(len(actions)):
        action = actions[i]
        if action == "StockSpanner":
            stock_spanner = StockSpanner()
        elif action == "next":
            assert stock_spanner is not None
            r = stock_spanner.next(params[i][0])
            assert r == output[i], f"Invalid next() output at i={i} expected={output[i]} actual={r}"


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
if __name__ == "__main__":
    execute_test_case(
        actions=["StockSpanner", "next", "next", "next", "next", "next", "next", "next"],
        params=[[], [100], [80], [60], [70], [60], [75], [85]],
        output=[None, 1, 1, 1, 2, 1, 4, 6],
    )
