'''Un calcolatore interattivo: È necessario sviluppare un calcolatore interattivo con almeno 10 casi di test utilizzando UnitTest cercando di (possibilmente) coprire tutti i percorsi di esecuzione! Si assume che l'input dell'utente sia una formula che consiste in un numero, un operatore (almeno + e -), e un altro numero, separati da uno spazio (ad esempio 1 + 1). Dividi l'input dell'utente usando str.split(), e verifica se la lista risultante è valida:

    Se l'input non consiste di 3 elementi, solleva un'eccezione FormulaError, che è un'eccezione personalizzata.
    Prova a convertire il primo e il terzo input in un float (così: float_value = float(str_value)). Cattura qualsiasi ValueError che si verifica, e invece solleva un'eccezione FormulaError.
    Se il secondo input non è '+' o '-', solleva di nuovo un'eccezione FormulaError.
    Se l'input è valido, esegui il calcolo e stampa il risultato. L'utente viene quindi invitato a fornire un nuovo input, e così via, fino a quando l'utente inserisce "quit".
'''