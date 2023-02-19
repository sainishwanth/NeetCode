def getConcatenation(nums: list[int]) -> list[int]:
        lst = [i for i in nums]
        print(lst)
        for j in range(len(lst)):
            lst.append(lst[j])
        return lst

print(getConcatenation([1,2,3,4]))
