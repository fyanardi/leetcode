class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque

        r_indices = deque()
        d_indices = deque()

        for i in range(len(senate)):
            if senate[i] == 'R':
                r_indices.append(i)
            else:
                d_indices.append(i)

        banned = 0
        while len(r_indices) > 0 and len(d_indices) > 0:
            r_index = r_indices.popleft()
            d_index = d_indices.popleft()

            banned += 1
            # To maintain the relative index of newly re-inserted senator
            new_index = len(senate) + banned - 1

            if r_index < d_index:
                # r is ahead of d and has voted to ban the next d, re-add r into the back of the queue
                # d has been banned by removing it from the queue
                r_indices.append(new_index)
            else:
                d_indices.append(new_index)

        return "Radiant" if len(r_indices) > len(d_indices) else "Dire"


if __name__ == "__main__":
    solution = Solution()
    assert solution.predictPartyVictory("RD") == "Radiant"
    assert solution.predictPartyVictory("RDD") == "Dire"
    assert solution.predictPartyVictory("DDRRR") == "Dire"
    assert solution.predictPartyVictory("RDRDRDDRDRDRDRDRRDRDRDRDRDRDDDDRRDRDRDRDRDRDRDRRRRRDRDRDRDRDDDDDRDRDRDRDRDRDRDRRDRDRDRDRDRDRRDRDRDRDRDRDRDRDRRDRDRDRDRDRRD") == "Radiant"
