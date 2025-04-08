def blackjack_hand_total(cards):
    total = 0
    for card in cards:
        total+= card
    aces = cards.count(11)
    
    while total > 21 and aces:
        total -= 10
        aces -= 1
    
    return total


print(blackjack_hand_total([2, 3, 5]))  
print(blackjack_hand_total([11, 5, 5])) 


