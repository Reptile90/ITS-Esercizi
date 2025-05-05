'''User Albums: Start with your program from Exercise 8-7.
Write a while loop that allows users to enter an album’s artist and title.
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created.
Be sure to include a quit value in the while loop.'''


def make_album(artist_name: str, album_title: str, num_songs=None) -> dict:
    album: dict = {"Artist": artist_name, "Album": album_title}
    if num_songs is not None:
        album['songs'] = num_songs
    return album

while True:
    artist_name = input("Inserisci un artista: ")
    if artist_name.lower() == 'esci':
        break
    album_title = input("Inserisci l'album dell'artista che ha digitato: ")
    if album_title.lower() == 'esci':
        break
    num_songs_str = input("Inserisci il numero di canzoni contenuto nell'album o scrivi 'esci' per uscire: ")
    if num_songs_str.lower() == 'esci':
        break
    try:
        num_songs = int(num_songs_str)
    except ValueError:
        num_songs = None
        print("Numero di canzoni non valido, verrà memorizzato come assente.")

    album = make_album(artist_name, album_title, num_songs)
    print(album)

    scelta = input("Digita 'Esci' per uscire o premi Invio per continuare ad inserire: ").lower()
    if scelta == 'esci':
        break
    

    

    
