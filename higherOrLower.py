import gameData
import random
import art
import os

def clean():
    os.system("cls")

allData = gameData.data

def getOneData():
    oneIndex = random.randint(0, 49)
    return oneIndex

def getComparisionData(firstIn):
    twoIndex = random.randint(0,49)
    while twoIndex == firstIn:
        twoIndex = random.randint(0,49)
    return twoIndex

def determineHigher(one, two):
    if allData[one]["follower_count"] > allData[two]["follower_count"]:
        return "a"
    else:
        return "b"

def getAllData(index):
    name = allData[index]["name"]
    desc = allData[index]["description"]
    country = allData[index]["country"]
    return (f"{name}, a {desc}, from {country}.")


def game():

    score = 0
    continuePlay = True
    firstIndex = getOneData()
    
    while continuePlay:
        print(art.logo)
        secondIndex = getComparisionData(firstIn=firstIndex)
        winner = determineHigher(firstIndex, secondIndex)
        print(f"Compare A: {getAllData(firstIndex)}\n")
        print(art.vs)
        print(f"Against B: {getAllData(secondIndex)}\n")
        userGuess = input("Who has more followers? Type A or B: ").lower()
        if userGuess == winner: 
            score+=1
            continuePlay = True
            firstIndex = secondIndex
            clean()
            print(f"That's correct! The score is {score}")
        else:
            continuePlay = False
            clean()
            print(art.logo)
            print(f"Uh ho! That's incorrect. The final score is {score}")
            #firstIndex = getOneData()
        
        
    
    wannaPlayAgain = input("Do you want to play again? Type Y or N \n").lower()
    if(wannaPlayAgain == "y"):
        clean()
        game()


game()