'''Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the  dictionaries are storing the album information correctly. Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.'''


def make_album(artist_name:str, album_title:str, song_number:int=None)->dict:
    if song_number is None:
        information:dict[str,int]={"Artist Name": artist_name, "Album": album_title}
    else:
        information:dict[str,int] = {"Artist Name": artist_name, "Album": album_title, "Song":song_number}

    return information

def print_album(information):
    for key,values in information.items():
        if key != "Songs":
            print(f"{key}: {values}", end = " - ")
        else:
            print(f"{key}: {values}", end =" - ")
    print("\n")
        
        

    

print_album(make_album("Red Hot Chili Peppers","Californication"))
print_album(make_album("Periphery","Periphery 2 This Time Is Personal", 12))
print_album(make_album("Tesseract","War Of Being", 9 ))



