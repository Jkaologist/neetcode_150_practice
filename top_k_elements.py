import heapq
from typing import Counter


# sort by highest freq, chop k elements
def topKFrequent(nums, k):
    c = Counter(nums)
    sorted_nums = sorted(c.items(), key=lambda x: x[1], reverse=True)[:k]
    print(sorted_nums)
    return [x[0] for x in sorted_nums]


# top k elements, maintain with max heap
def topKFrequent(nums, k):
    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) + 1
    return heapq.nlargest(k, counter, key=counter.get)


# set to 0 after max read
def topKFrequent(nums, k):
    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) + 1
    out = []
    while k > 0:
        curr_max = max(counter, key=counter.get)
        out.append(curr_max)
        counter[curr_max] = 0
        k -= 1
    return out


# list pop
def topKFrequent(nums, k):
    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) + 1
    out = []
    while k > 0:
        curr_max = max(counter, key=counter.get)
        del counter[curr_max]
        out.append(curr_max)
        k -= 1
    return out


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(topKFrequent([1], 1))
