"""
Given a non-empty, singly linked list with head node head,
return a middle node of linked list.

Note:
The number of nodes in the given list will be between 1 and 100.
.*.*.*.*.*.

# Example 1
# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])

Explanation: 
The returned node has value 3.  
(The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 
and ans.next.next.next = NULL.

# Example 2
# Input: [1,2,3,4,5,6]
# Output:  Node 4 from this list (Serialization: [4,5,6])
Explanation: 
Since the list has two middle nodes with values 3 and 4, 
we return the second one.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Solution 1
def middleNode(head):
	# input: head: ListNode
	# output: ListNode
	mid, count = head, 0
	while head:
		if count%2:
			mid = mid.next
		head = head.next
		count += 1

	return mid

# Solution 2
def middleNode2(head):
	# input: head: ListNode
	# output: ListNode
	if head.next is None:
		return head

	fast = head.next.next
	slow = head.next
	while fast and fast.next:
		fast = fast.next.next
		slow = slow.next

	return slow



if __name__ == "__main__":
	print 'Execute input ListNode=[1,2,3,4,5]:: ', middleNode(head).val
	print 'Execute input ListNode=[1,2,3,4,5]:: ', middleNode2(head).val
	
