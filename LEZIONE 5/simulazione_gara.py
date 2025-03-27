import random

def init_race():
    turtle_position:int= 1
    hare_position:int=  1
    turtle_stamina = 100
    hare_stamina = 100
    obstacles = {15: -3, 30: -5, 45: -7}
    bonuses = {10: +5, 25: +3, 50: +10}
    print(F"Turtles position: {turtle_position} Hare position: {hare_position}")
    print("BANG !!!!! AND THEY'RE OFF !!!!!")
    return turtle_position, hare_position, turtle_stamina, hare_stamina, obstacles, bonuses
    

def turtleMove(turtle_position, turtle_stamina)-> int:
    t_move:int = random.randint(1,10)
    cost_move = 0
    verify_mode= False
    
    if 1 <= t_move <= 5:
        turtle_position += 3
        cost_move = 5
        verify_mode = True
        
    elif  6<= t_move <= 7:
        turtle_position -= 6
        cost_move=10
        verify_mode = True
    elif 8 <= t_move <= 10:
        turtle_position += 1
        cost_move = 3
        verify_mode= True

    if verify_mode:
        turtle_stamina -= cost_move
    else:
        turtle_stamina += 10
        if turtle_stamina > 100:
            turtle_stamina = 100

    if  turtle_position <= 0:
        turtle_position = 1
    if turtle_position > 70:
        turtle_position = 70
    
    if turtle_stamina == 0:
        turtle_position += 0
        turtle_stamina += 10
    return turtle_position,turtle_stamina

def hareMove(hare_position, hare_stamina):
    h_move = random.randint(1,10)
    hare_cost = 0
    verify_hare = False
    
    if 1 <= h_move <= 2:
        hare_position += 0
        hare_stamina += 10
    elif 3 <= h_move <= 4 and hare_stamina >= 15:
        hare_position += 9
        hare_cost = 15
        verify_hare = True
    elif h_move == 5 and hare_stamina >= 20:
        hare_position -= 12
        hare_cost = 20
        verify_hare = True
    elif 6 <= h_move <= 8 and hare_stamina >= 5:
        hare_position += 1
        hare_cost = 5
        verify_hare = True
    elif 9 <= h_move <= 10 and hare_stamina >= 8:
        hare_position -= 2
        hare_cost = 8
        verify_hare = True
    
    if verify_hare:
        hare_stamina -= hare_cost
        if hare_stamina < 0:
            hare_stamina = 0
    
    if hare_stamina > 100:
        hare_stamina = 100
    
    if hare_position < 1:
        hare_position = 1
    if hare_position > 70:
        hare_position = 70
    
    return hare_position, hare_stamina


def printTrack(turtle_position, hare_position):
    print(f"\n[T: {turtle_position} | H: {hare_position}]")
    create_track:list = ["_"] * 70
    valid_turtle = 1 <= turtle_position <= 70
    valid_hare = 1 <= hare_position <= 70
    if valid_turtle and valid_hare and turtle_position == hare_position:
        create_track[turtle_position-1] = "OUCH!!!"
    else:
        if valid_turtle:
            create_track[turtle_position - 1] = "T"
        if valid_hare:
            create_track[hare_position - 1] = "H"
    print(''.join(create_track))

def checkWinner(turtle_position, hare_position):
    if turtle_position >= 70 and hare_position >= 70:
        return "IT'S A TIE"
    if turtle_position >= 70:
        return "TORTOISE WINS! || VAY!!!"
    if hare_position >= 70:
        return "HARE WINS || YUCH!!!"
    return None

def changeWeather():
    weather = random.choices(["sun", "rain"], weights=[70, 30])[0]
    return weather
    
    
def applyObstacles(position: int, obstacles: dict, bonuses: dict) -> int:
    original_pos = position
    
    if position in obstacles:
        penalty = obstacles[position]
        position += penalty
        print(f"Obstacles at position {original_pos}! Penalty: {penalty}")
        if position < 1:
            position = 1
        elif position > 70:
            position = 70
        return position
    
    if position in bonuses:
        bonus = bonuses[position]
        position += bonus
        print(f"Bonus {original_pos}! Advance: {bonus}")
        if position < 1:
            position = 1
        elif position > 70:
            position = 70
        return position
    
    return position
def race():
    turtle_position, hare_position, turtle_stamina, hare_stamina, obstacles, bonuses = init_race()
    turni = 0
    weather = "sun"
    
    while True:
        if turni % 10 == 0:
            weather = changeWeather()
            print(f"\nChange Weather: {weather.upper()}!")
            if weather == "rain":
                turtle_position -= 1
                if turtle_position < 1:
                    turtle_position = 1
                hare_position -= 2
                if hare_position < 1:
                    hare_position = 1
        
        turtle_position, turtle_stamina = turtleMove(turtle_position, turtle_stamina)
        hare_position, hare_stamina = hareMove(hare_position, hare_stamina)
        
        turtle_position = applyObstacles(turtle_position, obstacles, bonuses)
        hare_position = applyObstacles(hare_position, obstacles, bonuses)

        printTrack(turtle_position, hare_position)

        winner = checkWinner(turtle_position, hare_position)
        if winner:
            print(f"{winner} after {turni} turns!")
            break

        turni += 1


race()

