def blackjack_hand_total(cards:list[int]) -> int:
    total:int = sum(cards)  # Calcola la somma iniziale dei valori delle carte
    num_aces:int = cards.count(11)  # Conta quanti assi (valore 11) sono presenti nella mano
    
    # Se il totale supera 21 e ci sono assi, riduci il valore degli assi a 1
    while total > 21 and num_aces > 0:
        total -= 10  # Cambia un asso da 11 a 1 per ridurre il totale
        num_aces -= 1  # Aggiorna il conteggio degli assi modificati
    
    return total  # Restituisce il valore totale della mano

# Test case
print(blackjack_hand_total([2, 3, 5]))  # Output: 10
print(blackjack_hand_total([10, 11]))   # Output: 21 (l'asso vale 11)
print(blackjack_hand_total([11, 8, 4])) # Output: 13 (l'asso diventa 1 per evitare il bust)