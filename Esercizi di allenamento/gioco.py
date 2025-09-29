def dedup_stable(nums: list[int]) -> list[int]:

    if len(nums)== 0:
        return nums
    newlist = [nums[0]]
    for num in nums:
        if num != newlist[-1]:
            newlist.append(num)
    return newlist

nums = [2,4,5,6,6,4,3,8,7,1,9,8,6,4,4,5,7,8,9,3,46,345,6]
print(dedup_stable(nums))