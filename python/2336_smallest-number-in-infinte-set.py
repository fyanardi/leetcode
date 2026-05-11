import heapq


class SmallestInfiniteSet:

    # Initial implementation without Priority Queue
    # Runtime: Beats 5.03%, Memory: Beats 99.79%

    #def __init__(self):
    #    self.removed = []

    #def popSmallest(self) -> int:
    #    if len(self.removed) > 0:
    #        smallest = self.removed[0]
    #        if smallest > 1:
    #            self.removed.insert(0, 1)
    #            return 1
    #        for i in range(1, len(self.removed)):
    #            if self.removed[i] - self.removed[i - 1] > 1:
    #                to_remove = self.removed[i - 1] + 1
    #                self.removed.insert(i, to_remove)
    #                return to_remove

    #        to_remove = self.removed[-1] + 1
    #        self.removed.append(to_remove)
    #        return to_remove

    #    self.removed.append(1)
    #    return 1

    #def addBack(self, num: int) -> None:
    #    if num in self.removed:
    #        self.removed.remove(num)

    # Revised implementation with Priority Queue
    # Runtime: Beats 62.01%, Memory: Beats 6.63%

    def __init__(self):
        self.current = 1
        self.added = []

    def popSmallest(self) -> int:
        if len(self.added) == 0:
            popped = self.current
            self.current += 1
            return popped

        if self.added[0] < self.current:
            popped = heapq.heappop(self.added)

            return popped

        popped = self.current
        self.current += 1
        return popped

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.added:
            heapq.heappush(self.added, num)


def execute_test_case(actions: list[str], params: list[list[int]], output: list[int | None]):
    smallestInfiniteSet = None
    for i in range(len(actions)):
        action = actions[i]
        if action == "SmallestInfiniteSet":
            smallestInfiniteSet = SmallestInfiniteSet()
        elif action == "addBack":
            assert smallestInfiniteSet is not None
            assert smallestInfiniteSet.addBack(params[i][0]) == output[i]
        elif action == "popSmallest":
            assert smallestInfiniteSet is not None
            r = smallestInfiniteSet.popSmallest()
            assert r == output[i], f"Invalid popSmallest() output at i={i} expected={output[i]} actual={r}"

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
if __name__ == "__main__":
    execute_test_case(
        actions=[
            "SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest",
            "addBack", "popSmallest", "popSmallest", "popSmallest",
        ],
        params=[[], [2], [], [], [], [1], [], [], []],
        output=[None, None, 1, 2, 3, None, 1, 4, 5],
    )

    execute_test_case(
        actions=[
            "SmallestInfiniteSet", "popSmallest", "popSmallest", "addBack", "popSmallest",
            "addBack", "popSmallest", "popSmallest"
        ],
        params=[[], [], [], [3], [], [2], [], []],
        output=[None, 1, 2, None, 3, None, 2, 4],
    )

    execute_test_case(
        actions=[
            "SmallestInfiniteSet", "popSmallest", "addBack", "addBack", "popSmallest",
            "addBack", "popSmallest", "popSmallest", "popSmallest",
        ],
        params=[[], [], [1], [1], [], [1], [], [], []],
        output=[None, 1, None, None, 1, None, 1, 2, 3],
    )
