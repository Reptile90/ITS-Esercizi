def unique_count(nums: list[int]) -> int:
    nums_set = set(nums)
    return len(nums_set)


nums = [7, 3, 7, 2, 3, 9, 2, 1]
print(unique_count(nums))