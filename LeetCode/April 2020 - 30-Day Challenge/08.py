# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def middleNode(self, head: ListNode) -> ListNode:
		nodes = []
		while head != None:
			nodes.append(head)
			head = head.next
		return nodes[len(nodes) // 2]
