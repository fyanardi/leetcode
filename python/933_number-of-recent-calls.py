class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        l = len(self.requests)
        count = l

        for i in range(l - 1, -1, -1):
            if self.requests[i] < t - 3000:
                count = l - i - 1
                break

        self.requests.append(t)

        return count + 1


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

if __name__ == "__main__":
    recentCounter = RecentCounter()
    # requests = [1], range is [-2999,1], return 1
    assert recentCounter.ping(1) == 1
    # requests = [1, 100], range is [-2900,100], return 2
    assert recentCounter.ping(100) == 2
    # requests = [1, 100, 3001], range is [1,3001], return 3
    assert recentCounter.ping(3001) == 3;
    # requests = [1, 100, 3001, 3002], range is [2,3002], return 3
    assert recentCounter.ping(3002) == 3
