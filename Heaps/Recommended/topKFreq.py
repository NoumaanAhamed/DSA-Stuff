import heapq

# using max heap
def topKfreq(nums, k):
    freq = {}
    temp = []
    res = []
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    for key, value in freq.items():
        temp.append((-1 * value, key))
    heapq.heapify(temp)

    for _ in range(k):
        res.append(heapq.heappop(temp)[1])

    return res
        

# using bucket sort
def topKfreq2(nums, k):
    freq = {}
    bucket = [None] * (len(nums) + 1)   
    res = []
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    for key, value in freq.items():
        if not bucket[value]:
            bucket[value] = []
        bucket[value].append(key)
    count = len(nums) + 1
    while count > 0 and k > 0:
        for key in bucket[count]: # type: ignore
            res.append(key)
            k -= 1
        count -= 1


    return res


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKfreq(nums, k))

# heapify vs heappush n times
# heapify is faster than heappush n times
# heapify is O(n) and heappush n times is O(nlogn)
