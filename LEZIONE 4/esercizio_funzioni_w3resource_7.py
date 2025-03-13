'''Write a Python function that accepts a string and counts the number of upper and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12'''


def counter_letters(string:str)-> str:
    upper_case:int = 0
    lower_case:int = 0
    for lettere in string:
        if (lettere.upper() == lettere) and (lettere != " "):
            upper_case += 1
        elif lettere == " ":
            pass
        else:
            lower_case += 1
    print(f"No. of Upper case characters: {upper_case}")
    print(f"No. of Lower case characters: {lower_case}")



    


