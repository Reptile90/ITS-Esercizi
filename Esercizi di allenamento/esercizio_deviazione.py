def calculate_std_dev(nums:list[float])->float:
    media=0
    varianza = 0
    deviazione_standard=0
    somma=0
    if len(nums)== 0:
        raise ValueError("Lista vuota")
    for num in nums:
        somma+=num
    media = somma/len(nums)
    for num in nums:
        varianza += (num - media)**2/len(nums)
    
    deviazione_standard = varianza ** 0.5
    
    return deviazione_standard
    
    
    
    
    
nums_list = [1.0, 2.0, 3.0, 4.0, 5.0]

print(calculate_std_dev(nums_list))