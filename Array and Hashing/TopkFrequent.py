# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

def topKFrequent(nums: list[int], k: int) -> list[int]:
    if len(nums) == 1:
        return [nums[0]]
    hashMap = {}
    for i in set(nums):
        hashMap[i] = nums.count(i)
    hashMapSorted = sorted(hashMap.items(), key=lambda x:x[1], reverse=True)
    lst = []
    for i in range(k):
        lst.append(hashMapSorted[i][0])
    return lst
