from helpers.linkedlist import (
    ListNode,
    parse_linked_list,
    serialize_linked_list,
)


class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None

        node: ListNode = head
        head_odd = None
        head_even = None
        odd = None
        even = None
        i = 1

        while node is not None:
            if i % 2 == 1:
                if odd is None:
                    head_odd = node
                else:
                    odd.next = node
                odd = node
            else:
                if even is None:
                    head_even = node
                else:
                    even.next = node
                even = node

            node = node.next
            i += 1

        if head_even is not None:
            odd.next = head_even
        if even is not None:
            even.next = None

        return head_odd


if __name__ == "__main__":
    solution = Solution()

    assert serialize_linked_list(solution.oddEvenList(parse_linked_list([1, 2, 3, 4, 5]))) == [1, 3, 5, 2, 4]
    assert serialize_linked_list(solution.oddEvenList(parse_linked_list([2, 1, 3, 5, 6, 4, 7]))) == [2, 3, 6, 7, 1, 5, 4]
