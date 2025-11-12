def min_coins(amount: int, coins: list[int]) -> int:
    coin_needed = [1000000000] * (amount + 1)
    coin_needed[0] = 0

    for i in range(1, amount + 1):
        for c in coins:
            if i - c >= 0:
                coin_needed[i] = min(coin_needed[i], coin_needed[i - c] + 1)

    return coin_needed[amount]
    
    
    
    
    
    
    
    
    
    
    
    
    
amount = 10222
coins = [50,100,200,500]
print(min_coins(amount,coins))
