def count_even(nums: list[int]) -> int:
    pari = 0
    for num in nums:
        if num % 2 == 0:
            pari += 1
            
    return pari
        