from random import randint as rand

player1_score = 0
player2_score = 0

def game(score):
    terminate = False
    play = True
    while play:
        die1 = rand(1,6)
        die2 = rand(1,6)
        print(f"Die1 = {die1}")
        print(f"Die2 = {die2}")
        d1_d2 = die1 == 1 or die2 == 1
        temp_score = 0

        if not(d1_d2):
            temp_score = die1 + die2
            print(f"You scored {temp_score} this round.")
            print("")
        elif (d1_d2) and not(die1 == 1 and die2 == 1):
            temp_score = 0
            print("Oops! You rolled a one your score this round is 0.")
            print("")
            break
        else:
            terminate = True
            print("Oops! You rolled two ones your entire score just became 0.")
            print("")
            break
        play = input("Continue playing?(Y/N): ").lower()
        if play == 'y':
            play = True
            continue
        else:
            score += temp_score
            play = False
            print(f"Your score this round was {score}.")
    return score, terminate

while player1_score < 100 and player2_score < 100:
    input("Press ENTER for Player1: ")
    print("    Player 1")
    player1_score , terminate1 = game(player1_score)
    if terminate1:
        player1_score = 0
    print(f"p1 = {player1_score}")
    input("Press ENTER for Player2: ")
    print("    Player 2")
    player2_score , terminate2 = game(player2_score)
    if terminate2:
        player2_score = 0
    print(f"p2 = {player2_score}")

if player1_score >= 100:
    print("Congrats! Player1 Won.")
else:
    print("Congrats! Player2 Won.")
input()