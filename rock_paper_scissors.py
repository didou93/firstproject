import random

options = ["rock", "paper", "scissors"]

player= input("lets play dummy soooo 'rock' , 'paper' , or 'scissors' ?/n")
print("you played ",player)
computer = random.choice(options)
print("i played ",computer)
#in case of a tie
if player == computer:
    print ("its a tie lets play again")
#player wins   r..s   ///// s...p /////  p...r
if (player == 'rock' and computer == 'scissors') or (player == 'scissors' and computer == 'paper') or (player == 'paper' and computer == 'rock'):
    print ("okay you win but u still a dummy to me")
#player looses s...r //////  r...p /////   p...s
if (player == 'scissors' and computer == 'rock') or (player == 'rock' and computer == 'paper') or (player == 'paper' and 'computer' == 'scissors'):
    print ("as expected dummy you lose")