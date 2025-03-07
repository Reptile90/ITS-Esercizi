'''User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.'''



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

cont: int = 0
insert= []
while cont <2:
    artista:str = input("Inserisci un artista: ")
    album:str = input("Inserisci un album: ")
    num_songs:int = int(input("Inserisci il numero di canzoni: "))
    insert.append((artista,album,num_songs))
    cont += 1

for i in insert:
    print_album(make_album(i[0],i[1],i[2]))

    




    
    




