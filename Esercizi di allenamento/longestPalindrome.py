def longestPalindrome(s):
    def expandAroundCenter(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    longest = ""
    for i in range(len(s)):
        # Palindromo dispari
        temp1 = expandAroundCenter(i, i)
        # Palindromo pari
        temp2 = expandAroundCenter(i, i+1)
        # Aggiorna il più lungo
        if len(temp1) > len(longest):
            longest = temp1
        if len(temp2) > len(longest):
            longest = temp2
    return longest