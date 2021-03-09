/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr) {
            return head;
        }
        if (head->next == nullptr) {
            return head;
        }
        ListNode *tail = new ListNode(head->val);
        return reverseListHelper(tail, head->next);
    }

    ListNode* reverseListHelper(ListNode* prev, ListNode* node) {
        if (node->next != nullptr) {
            return reverseListHelper(new ListNode(node->val, prev), node->next);
        }
        else {
            return new ListNode(node->val, prev);
        }
    }
};
