def findMedianSortedArrays(num1,num2):
    new = num1+num2
    new.sort()
    n = len(new)
    
    if n % 2 != 0:
        return new[n // 2]
    else:
        return (new[n//2-1] + new[n//2]) / 2
        
        
        
        
num1 = [1,2]
num2 = [3,4]
print(findMedianSortedArrays(num1,num2))