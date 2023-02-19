class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}
        for n, i in enumerate(nums):
            diff = target - i
            if diff in dic:
                return [dic[diff], n]
            dic[i] = n

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
