class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def parse_linked_list(nodes: list[int]) -> ListNode | None:
    """
    Helper function to parse a list of int values into a linked list `ListNode` representation
    """
    if len(nodes) == 0:
        return None

    head = node = ListNode(val=nodes[0])

    for i in range(1, len(nodes)):
        node.next = ListNode(val=nodes[i])
        node = node.next

    return head


def serialize_linked_list(head: ListNode | None) -> list[int]:
    """
    Helper function to serialize binary tree `ListNode` represented by the head node into a list of int values
    """
    values = []
    node = head

    while node is not None:
        values.append(node.val)
        node = node.next

    return values
