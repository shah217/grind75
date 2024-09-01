
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the start of the merged list
        dummy = ListNode()
        current = dummy
        
        # Traverse both lists and merge them
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If there are remaining nodes in either list, append them
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # Return the merged list, which starts at dummy.next
        return dummy.next

def main():
    # Helper function to create a linked list from a list of values
    def create_linked_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    # Helper function to convert a linked list to a list of values
    def linked_list_to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    # Test cases
    test_cases = [
        ([1, 2, 4], [1, 3, 4]),
        ([], []),
        ([], [0]),
        ([2], [1]),
        ([5, 6, 7], [1, 2, 3, 4])
    ]

    solution = Solution()

    for i, (list1_vals, list2_vals) in enumerate(test_cases):
        list1 = create_linked_list(list1_vals)
        list2 = create_linked_list(list2_vals)
        merged_list = solution.mergeTwoLists(list1, list2)
        merged_list_vals = linked_list_to_list(merged_list)
        print(f"Test case {i + 1}: {merged_list_vals}")



if __name__ == "__main__":
    main()