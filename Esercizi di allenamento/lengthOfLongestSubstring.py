def lengthOfLongestSubstring(s):
    viste = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in viste:
            viste.remove(s[left])
            left += 1
        viste.add(s[right])
        max_len= max(max_len,right - left + 1)
        
    return max_len
    
    
    
    
    
    
    
    
s1= "pwwkew"

print(lengthOfLongestSubstring(s1))