from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """Merge two linked lists sorted in non-decreasing order into one sorted linked list
        containing all nodes of given lists.

        Args:
            list1: Head of the first non-decreasing linked list.
            list2: Head of the first non-decreasing linked list.

        Returns:
            Head of non-decreasing linked list containing all nodes of given linked lists.

        """
        head = None
        previous = None
        while list1 or list2:
            if not list1 or list2 and list1.val >= list2.val:
                current = list2
                list2 = list2.next
            else:
                current = list1
                list1 = list1.next
            if previous:
                previous.next = current
            previous = current
            if not head:
                head = previous
        return head
