class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next


my_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
def my_func(listnode):
    return "HELL YEAH"

print(my_func(my_list)) # "HELL YEAH"