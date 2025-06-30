def recoursivePalindrome(stringa:str)->bool|str:
    new_string = stringa.lower().replace(" ","")
    if new_string == "":
        return True
    if new_string[0] == new_string[-1] and recoursivePalindrome(new_string[1:-1]):
        return True
    return False


print(recoursivePalindrome("Radar"))
print(recoursivePalindrome("Anna"))
print(recoursivePalindrome(" I topi non avevano nipoti"))
print(recoursivePalindrome("casa"))
print(recoursivePalindrome("Marta"))
print(recoursivePalindrome("Roma e Amore"))



    
     
