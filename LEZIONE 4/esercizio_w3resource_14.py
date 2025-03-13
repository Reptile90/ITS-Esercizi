'''Write a Python function to check whether a string is a pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog" '''


def pangram_check(string:str):
    alphabet:set = {
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"
    }
    pangram:bool= False
    set_character:set = set({})
    for lettera in string:
        if lettera != " ":
            set_character.add(lettera.lower())
        
    if  set_character == alphabet:
            pangram = True
        
        
    print(pangram)


pangram_check("The quick brown fox jumps over the lazy dog")



