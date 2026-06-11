from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       newmerge=  ListNode()
       tail = newmerge
       while list1 and list2:
           if list1.val< list2.val:
               tail.next = list1
               list1=list1.next
               
           else:
               tail.next = list2
               list2=list2.next
           tail = tail.next
               
       if not list1:
           tail.next = list2
       else :
           tail.next = list1 


           


       return newmerge.next


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)


# 1 -> 3 -> 4
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4) 
yes = Solution.mergeTwoLists(None,list1 = list1, list2 = list2)

print(yes)