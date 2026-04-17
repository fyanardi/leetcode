# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None

        node = ListNode(head.val)
        next: ListNode |  None = head.next

        while next is not None:
            node = ListNode(next.val, next=node)
            next = next.next

        return node

# Helper functions
def python_list_to_linked_list(values: list[int]) -> ListNode | None:
    if len(values) == 0:
        return None

    head: ListNode = ListNode(val=values[0])
    node: ListNode = head

    for i in range(1, len(values)):
        node.next = ListNode(val=values[i])
        node = node.next

    return head


def linked_list_to_python_list(head: ListNode | None):
    if head is None:
        return []

    values = []
    node = head
    while node is not None:
        values.append(node.val)
        node = node.next

    return values


if __name__ == "__main__":
    solution = Solution()
    assert linked_list_to_python_list(
        solution.reverseList(python_list_to_linked_list([1, 2, 3, 4, 5]))
    ) == [5, 4, 3, 2, 1]
    assert linked_list_to_python_list(
        solution.reverseList(python_list_to_linked_list([]))
    ) == []
