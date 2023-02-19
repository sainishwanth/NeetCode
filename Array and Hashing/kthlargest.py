def findKthLargest(nums: list[int], k: int) -> int:
    print(nums)
    nums.sort(reverse=True)
    return nums[k]
print(findKthLargest([1,2,3,4,5], 3))
