from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorder_list(self, head: Optional[ListNode]) -> None:
        def find_middle_node(head: Optional[ListNode]):
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        # linked lst reading forward -> middle node
        def first_half(head: Optional[ListNode]):
            forward = r = ListNode()
            middle = find_middle_node(head)
            while head is not middle:
                r.next = head
                head = head.next
                r = r.next
            return forward.next

        # second linked middle node -> end node reversed
        def reversed_second_half(head: Optional[ListNode]):
            previous = None
            current = head
            while current:
                temp_next = current.next
                current.next = previous
                previous = current
                current = temp_next
            return previous

        # merge 2 linked list with a cpy 3rd list
        def merge_linked_lists(
            first_half: Optional[ListNode], reversed_second_half: Optional[ListNode]
        ):
            dummy = reader = ListNode()
            counter = 0
            while first_half and reversed_second_half:
                if counter % 2 == 0:
                    reader.next = first_half
                    first_half = first_half.next
                else:
                    reader.next = reversed_second_half
                    reversed_second_half = reversed_second_half.next
                counter += 1
                reader = reader.next

            return dummy.next

        return merge_linked_lists(
            first_half(head), reversed_second_half(find_middle_node(head))
        )
