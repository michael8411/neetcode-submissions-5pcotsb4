# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def merge_sort(list):
#     if len(list) <= 1:
#         return list

#     mid = len(list) // 2
#     left_half = merge_sort(list[:mid])
#     right_half = merge_sort(list[mid:])
#     return merge(left_half, right_half)


# def merge(left, right):
#     sorted = []
#     left_index = 0
#     right_index = 0

#     while left_index < len(left) and right_index < len(right):
#         if left[left_index] <= right[right_index]:
#             sorted.append(left[left_index])
#             left_index += 1
#         else:
#             sorted.append(right[right_index])
#             right_index += 1
#     sorted.extend(left[left_index:])
#     sorted.extend(right[right_index:])
#     return sorted


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode(0)
        curr = dummy

        
        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        curr.next = left or right                                                                                                                                                                                             
        return dummy.next
                                                                                                                                                                                                                                                                                                                                                                     