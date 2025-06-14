
import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
myCards = []
myCurrentScore = 0

pcCards = []
pcCurrentScore = 0

def pcHand():
    global pcCards, pcCurrentScore
    while pcCurrentScore <= 21:
        pcCards.append(random.choice(cards))
        pcCurrentScore += pcCards[-1]
    pcCurrentScore -= pcCards[-1]
    pcCards.pop(-1)
    # if pcCurrentScore == 21:
    #     print("BlackJack!")

def myHand():
    global myCards, myCurrentScore
    myCards.append(random.choice(cards))
    myCurrentScore += myCards[-1]

def info():
    print(f"Your cards: {myCards}, current score: {myCurrentScore}")
    print(f"Computer's first card: {pcCards[0]}")

def finalInfo():
    print(f"Your final cards: {myCards}, final score: {myCurrentScore}")
    print(f"Computer's final hand: {pcCards}, final score: {pcCurrentScore}")


 
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

pcHand()
myHand()
myHand()
info()



getCard = input("Type 'y' to get another card, type 'n' to pass: ").lower()

while getCard == "y":
    myHand()
    info()
    if myCurrentScore > 21:
        print("You went over. You Lose :(")
        finalInfo()
        break
    getCard = input("Type 'y' to get another card, type 'n' to pass: ").lower()

if getCard == "n":
    if myCurrentScore == 21:
        print("BlackJack!!!")
    while pcCurrentScore < myCurrentScore:
        pcCards.append(random.choice(cards))
        pcCurrentScore += pcCards[-1]
    finalInfo()
    if myCurrentScore > pcCurrentScore or pcCurrentScore > 21:
        print("You Win!!!")
    if myCurrentScore < pcCurrentScore and pcCurrentScore <= 21:
        print("You Lose!!!")
    if myCurrentScore == pcCurrentScore:
        print("Draw...")
