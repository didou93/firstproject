import random

def game():
    player= input("lets play dummy soooo 'rock' , 'paper' , or 'scissors' ?")

    computer = random.choice(options)
print(computer)
#in case of a tie
    if player == computer:
        return ("its a tie lets play again")

#player wins   r..s   ///// s...p /////  p...r
    if (player == rock and computer == scissors) or (player == scissors and computer == paper) or (player == paper and computer == rock)
        return ("okay you win but u still a dummy to me")

#player looses s...r //////  r...p /////   p...s
    if (player == scissors and computer == rock) or (player == rock and computer == paper) or (player == paper and computer == scissors)
        return ("as expected dummy you lose")