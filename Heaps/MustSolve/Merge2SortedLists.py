class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"
    



def MergeTwoSortedLists(l1, l2):
    res = ListNode(0)
    temp = res
    while l1 and l2:
        if l1.val < l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next
        temp = temp.next
    if l1:
        temp.next = l1
    if l2:
        temp.next = l2
    return res

def MergeKSortedLists(lists):
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]
    if len(lists) == 2:
        return MergeTwoSortedLists(lists[0], lists[1])
    mid = len(lists) // 2
    left = MergeKSortedLists(lists[:mid])
    right = MergeKSortedLists(lists[mid:])
    return MergeTwoSortedLists(left, right)

def MergeKSortedListsUsingHeap(lists):
    import heapq
    heap = []
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i))
    res = ListNode(0)
    temp = res
    while heap:
        val, idx = heapq.heappop(heap)
        temp.next = ListNode(val)
        temp = temp.next
        if lists[idx].next:
            lists[idx] = lists[idx].next
            heapq.heappush(heap, (lists[idx].val, idx))
    return res.next

# res = MergeTwoSortedLists(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4))))
# print(res) # [1,1,2,3,4,4]

# res = MergeKSortedLists([ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))])
# print(res) # [1,1,2,3,4,4,5,6]

res = MergeKSortedListsUsingHeap([ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))])
print(res) # [1,1,2,3,4,4,5,6]