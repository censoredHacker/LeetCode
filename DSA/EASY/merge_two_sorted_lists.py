# Problem Name: Merge Two Sorted Lists
# Problem Link: https://leetcode.com/problems/merge-two-sorted-lists/
# Difficulty: Easy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Create res list
        list3 = ListNode(0) #dummy node
        result = list3

        # while loop till? pointer1 or pointer2 to be equal null
        while(list1 is not None and list2 is not None):

            # compare pointer 1 & pointer2
            if(list1.val <= list2.val):
                list3.next = list1
                # smaller one goes to list 3
            else:
                list3.next = list2

        if list1 is None:
            list3.next = list2
        else:
            list3.next = list1
        
        return result.next

if __name__ == "__main__":
    solution = Solution()        
    list1 = ListNode(0)
    temp1 = ListNode(1)
    list1.next = temp1
    temp2 = ListNode(2)
    temp1.next = temp2

    # list2 = [1,3,4]
    list2 = ListNode(0)
    temp1 = ListNode(2)
    list2.next = temp1
    temp2 = ListNode(4)
    temp1.next = temp2

    result = solution.mergeTwoLists(list1, list2)
    
    while result is not None:
        print(result.val)
        result = result.next