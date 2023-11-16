class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    # Helper function to count the number of nodes in the linked list
    def countNodes(head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    # Helper function to reverse a sublist of a linked list
    def reverseSublist(head, k):
        prev = None
        current = head
        for i in range(k):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev, current

    # Check if there are at least k nodes in the list
    if countNodes(head) < k:
        return head

    new_head, next_head = reverseSublist(head, k)

    head.next = reverseKGroup(next_head, k)

    return new_head

# Helper function to convert a list to a linked list
def listToLinkedList(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list to a list
def linkedListToList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example usage:
input_list = [1, 2, 3, 4, 5]
k = 3
head = listToLinkedList(input_list)
result = reverseKGroup(head, k)
output_list = linkedListToList(result)
print(output_list)  # Output: [2, 1, 4, 3, 5]
