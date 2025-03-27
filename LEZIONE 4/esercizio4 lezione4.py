                                                    
def word_frequency(text_analized:str)->dict:        #definizione della funzione
    
    words_list = text_analized.lower().split()      #funzione split per ritornare una lista con le singole parole
    words_container:dict={}                         #creazione dizionario vuoto
    
    for word in words_list:                         #ciclo for per iterare le parole
        
        if word in words_container:                 #condizione per contare le parole
            words_container[word]+=1
        else:
            words_container[word]=1
    
    for word,count in words_container.items():#ciclo per poter stampare chiave e valore del dizionario
        print(f"la parola {word} è contenuta {count} volte nel testo.")
    return words_container


word_frequency("Daylight fading \
Desolate skyline \
Sun retreating giving way to dusk \
Canvas sinking to darkness \
Flickering are candles in the wind \
Following behind the trail of the living to the feeding ground \
All are one and the pulsing of a heart keeps an eternal bound \
Open your veins \
Hook up the line \
It’s feeding time \
Open the veins \
Drink of the body \
Blood like wine \
Bow low \
The children of the blood glow for the one eternal \
Pray now, lest the darkness fall upon our rite, to the one eternal \
Peering in the night \
Servants \
Everybody on the lane coddled in peace \
The body had to cease \
Soar below your sky \
No wind below his dead wings \
To the pale one, this life, we owe \
Whispers trail in the breeze  \
Ignore the sound, though malicious it seems \
Bow low \
The children of the blood glow for the one eternal \
Pray now, lest the darkness fall upon our rite, to the one eternal \
Oh the beauty abound \
Bow low before the pale one \
Pray now, lest the darkness fall upon our rite, to the one eternal \
Interference howls in the dead of night \
Remnants of an elden order circling \
Hold tight \
Our innocence betrays our safety \
The reality of our destruction reaching for our sanity \
Solidarity besieged \
The remnants of an elden order servicing their vanity \
Weep as the darkness surrounds \
Silent, in the moonlight, as she goes \
The air is stale as he lingers on his own \
Harboring the foresight, with the teeth drawn, a commanding shadow pushes onward toward the throne \
Draining borrowed blood and roaring loud as thunder \
Nails tearing through the pale \
The preservation of a life gone \
Blood rains heavy in her trail \
Mirrored image \
The child of coddled demeanor \
A family torn \
Carry on by his side \
Wide in the middle \
Terrorize \
The hunger showing teeth \
Severing mortality \
The hunger grows inside \
Measuring a quarter in size \
He moves swiftly into the night \
So stay low \
The fury of the stealth-blow \
Drain the blood and the cries out to terrorize see it in their eyes \
The pleasure of the hunt is recognized \
Painting the town rose red beneath his feet \
Red upon his face \
For the taste \
For the vengeance \
Deemed the savior eternally \
Servants \
Everybody on the street living in peace \
They rid it of disease \
Open up your veins \
Hook up the line \
Drink of the body \
Blood like wine \
Open your veins \
Drink of the body \
Blood like wine \
Son of darkness, feed in the dead of night" )