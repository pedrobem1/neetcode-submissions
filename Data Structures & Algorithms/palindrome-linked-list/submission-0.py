# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next

            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        if fast: #caso impar
            slow = slow.next

        left = prev
        while left:
            if slow.val == left.val:
                left = left.next
                slow = slow.next

            else:
                return False

        return True

