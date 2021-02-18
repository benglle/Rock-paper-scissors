import random as r
import time as t
values = {"rock_wins":0, "paper_wins":0, "scissor_wins":0, "draws":0}
rpc = ["rock", "paper", "scissors"]
clear = lambda: os.system("cls")
def rock_paper_scissors(times, show):
    while times != 0:
        x2 = r.choice(rpc)
        x1 = r.choice(rpc)

        print("The computer chose...", x1)
        print("The computer chose...", x2)

        if {x1, x2} == {"rock", "paper"}:
            print("Paper won!")
            values["paper_wins"] += 1

        if {x1, x2} == {"rock", "scissors"}:
            print("Rock won!")
            values["rock_wins"] += 1

        if x1 == x2:
            print("It is a draw!")
            values["draws"] += 1

        if {x1, x2} == {"paper", "scissors"}:
            print("scissors!")
            values["scissor_wins"] += 1

        print("-------------------------------")
        times -= 1
        if show == True:
            print(values)
        clear()
        
    print("-------------------------------")
    print("")
    print("Total values:")
    print("-------------------------------")
    print(values)

rock_paper_scissors(10000, False)

    
#18/02/2021
#Took a test of 10000 attempts, results are given:
#{'rock_wins': 2206, 'paper_wins': 2275, 'scissor_wins': 2245, 'draws': 3274}
