'''Scrivere un programma in linguaggio Python che legge dall’utente due stringhe s1 e s2 corripondenti a frammenti di
DNA e verifica se s2 puo' essere sovrapposta su s1 in modo che una parte iniziale (prefisso) di s2 coincida con
una parte finale (suffisso) di s1.
 
Il programma dovra' dare la lunghezza della massima sovrapposizione (0 se non si possono sovrapporre).
 
Ad esempio, se l’utente ha inserito:
s1= CAGCTGATCGATGCTAGCCTG
s2= AGCCTGTTGCACCTAGA

Le due stringhe si sovrappongono come segue:
CAGCTGATCGATGCTAGCCTG
               AGCCTGTTGCACCTAGA

Il programma dovra' quindi stampare in output:

    le stringhe sovrapposte come nell'esempio.

    La massima lunghezza di sovrapposizione e' 6.


NOTA1:
il programma dovra' anche verificare la correttezza dell’input, ovvero le stringhe inserite dall’utente devono essere effettivamente frammenti di DNA.
Suggerimento: scrivere una funzione isDNA() che, data in input una sequenza, restituisca True se la sequenza passata è una valida sequenza del DNA formata dai soli caratteri A, C, G o T, e che restituisca False altirmenti.
Può essere utile usare una regex.

Nota2: trovare una soluzione che eviti di scrivere codice replicato per inizializzare le sequenze s1 e s2.

Infine, verificare le seguenti coppie di frammenti di DNA:
- s1= TTGACCAGGTCA
- s2= AACCGGTTAA
La massima lunghezza è 1

- s1= GGTACCGTGA
- s2= CGTGAACCTT
La massima lunghezza è 5

- s1= AAGCTTACG
- s2= ACGTTCGA
La massima lunghezza è 3

- s1= TTACGAGTACGCTAGT
- s2= ACGCTAGTCCGA
La massima lunghezza è 8'''


import re

def isDNA(sequenza:str):
    if re.fullmatch(r'^[CAGT]+$', sequenza):
        return True
    return False

def sovrapponi(s1,s2):
    if isDNA(s1) and isDNA(s2):
        nuova_stringa:str = ""
        if s1 != s2:
            count:int = 0
            for char in s1:
                if char == s2[count]:
                    count += 1

                    nuova_stringa += char

                elif char == s2[0]:
                    count = 1
                    nuova_stringa = char
                else:
                    count = 0
                    nuova_stringa = ""
            if count > 0:
                return f" La sequenza trovata è {nuova_stringa}, la lunghezza massima è {count}"
            else:
                return "Nessuna sequenza trovata"
    else:
        raise ValueError("La sequenza deve avere i caratteri A/C/G/T")
    





s1= "GGTACCGTGA"
s2= "CGTGAACCTT"
print(sovrapponi(s1,s2))











