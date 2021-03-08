# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        # l1_: pointer to current node of l1
        l1_ = l1
        # l2_: pointer to current node of l2
        l2_ = l2
        # l3_: pointer to start of node that has no corresponding node in the other list (by
        #      position). E.g if l1 = [1, 2, 3] and l2 = [4], l1 is longer than l2, and l3_ will be
        #      initialized to node with val=2. If l1 has the same length as l2, l3_ will be None
        l3_ = None

        result = ListNode()
        current_node = None

        while True:
            if not l1_:
                l3_ = l2_
                break
            if not l2_:
                l3_ = l1_
                break

            if not current_node:
                current_node = result
            else:
                current_node.next = ListNode()
                current_node = current_node.next

            sum = l1_.val + l2_.val + carry
            carry = sum // 10
            current_node.val = sum % 10

            l1_ = l1_.next
            l2_ = l2_.next

        # Remaining of one of the list
        while l3_:
            current_node.next = ListNode()
            current_node = current_node.next
            sum = l3_.val + carry
            carry = sum // 10
            current_node.val = sum % 10
            l3_ = l3_.next

        if carry > 0:
            current_node.next = ListNode()
            current_node.next.val = carry

        return result

