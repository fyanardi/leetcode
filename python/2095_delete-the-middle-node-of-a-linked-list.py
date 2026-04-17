# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return None

        # slow is the prev node before mid, fast keeps track of the last node evaluated
        # We initialize fast to be the index 2 and slow to be the head (index 0) - mid is at index 1
        # Mid at index 0 is when there is only 1 node, which is handled by the if head.next is None above
        # Mid at index 1 is either when there are only 2 or 3 nodes
        # - When there are 2 nodes, fast will be initialized to None, while loop is skipped
        # - When there are 3 nodes, fast.next will be None, while loop is also skipped
        # Subsequently, slow will keeps track of the previous node before mid and fast will be the end of
        # the linked list given mid to be the mid
        fast = head.next.next
        slow = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        slow.next = slow.next.next

        # Original solution, slower
        #node = head
        #prev_mid = head
        #mid_index = 0
        #count = 0

        #while node is not None:
        #    count += 1
        #    new_mid_index = int(count / 2)
        #    if new_mid_index != mid_index:
        #        mid_index = new_mid_index
        #        if count > 3:
        #            assert prev_mid.next is not None
        #            prev_mid = prev_mid.next
        #    node = node.next

        #mid = prev_mid.next
        #assert mid is not None
        #prev_mid.next = mid.next

        return head


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
        solution.deleteMiddle(python_list_to_linked_list([1,3,4,7,1,2,6]))
    ) == [1,3,4,1,2,6]
    assert linked_list_to_python_list(
        solution.deleteMiddle(python_list_to_linked_list([1, 2, 3, 4]))
    ) == [1, 2, 4]
    assert linked_list_to_python_list(
        solution.deleteMiddle(python_list_to_linked_list([2, 1]))
    ) == [2]
