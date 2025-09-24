# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# Helper to create linked list from list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(val=values[0])
    current = head
    
    for value in values[1:]:
        current.next = ListNode(val=value)
        current = current.next
    return head                   
                
                
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
        
    return result
    
                       
values = [1, 2, 3, 4, 5, 6]
head = create_linked_list(values)
sol = Solution()
mid_node = sol.middleNode(head=head)
result = linked_list_to_list(mid_node)
print(result)
