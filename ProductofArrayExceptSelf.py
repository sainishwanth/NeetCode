def productExceptSelf(nums: list[int]) -> list[int]:
    product = 1
    count = 0
    for i in nums:
        if i == 0:
            count +=1
            if count > 1:
                return [0] * len(nums)
        else:
            product *= i
    lst = [0] * len(nums)
    for i in range(len(nums)):
        if nums[i] != 0 and count == 1:
            lst[i] == 0
        elif count == 0:
            lst[i] = int(product/i)
    return lst

print(productExceptSelf([-1,1,0,-3,3]))
