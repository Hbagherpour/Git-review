
from random import shuffle
def creat_deck ():
    deck = []
    face_values = ["A", "J", "Q", "K"]
    for i in range(4):
        for card in range(2, 11):
            deck.append(str(card))

        for card in face_values:
            deck.append(card)

    shuffle(deck)
    return deck

card_deck = creat_deck()

def showHelp():
    print("****************************************")
    instructions = """\nThe player who is "fishing “must have at least one card of the rank that was asked for in their hand.\nThe player who is addressed must hand over all the cards requested.\nIf the player has none, they say, "Go fish!" and the player who made the request draws the top card of the stock and places it in their hand.\n"""
    print(instructions)
    print("****************************************")


def specialInput(prompt):
    action = input(prompt)
    if action == '--help':
        print("")
        print("You need help ! ")
        showHelp()
        return specialInput(prompt)
    elif action == "--resume":
        print("You want to resume")
        return specialInput(prompt)
    else:
        return action

class Player:
    def __init__(self, name = "player", hand = [], score = 0):
        self.name = name
        self.hand = hand
        self.score = score

    def __str__(self):
        return self.name

    def get_card(self, card):
        for i in range(7):
            self.card = str(card_deck.pop())
            self.hand.append(card)


    def check_pairs(self, hand):
        self.points = 0
        for self.card in self.hand:
            if self.hand.count(card) > 1:
                self.hand.remove(card)
                self.hand.remove(card)
                self.points += 1
        return self.points


print(" Let's play go fish ! ")
print("")
print("These are our cards :) ")
print(card_deck)

first_hand = Player(get_card())
second_hand = Player(get_card())

print("")
player1 = Player(specialInput(" Please enter your name : "))

print(" ------------------------------------------------ ")
print(player1.get_card)
print(player2.get_card)
print(" ------------------------------------------------ ")



print(" ------------------------------------------------ ")

while True:
    if len(self.hand) < 1:
        break
    while True:
        print(" your cards are ", self.hand)
        ask_card = str(specialInput(f" what card do you want to ask {player1}? "))
        if ask_card is not player1_hand:
            print(" Please choose only the card which you have it on your hand ! ")
            print(" your cards are ", player1_hand)
            ask_card = specialInput(f" what card do you want to ask {player1}? ")
        if ask_card in player2_hand:
            print(" nice , you got it! ")
            player1_hand.remove(ask_card)
            player2_hand.remove(ask_card)
            player1_pairs += 1
            if len(player1_hand) < 1:
                break
            continue
        else:
            print(f" Go Fish {player1} ! ")
            if len(card_deck) < 1:
                break
            fish_card1 = str(card_deck.pop())
            if fish_card1 in player1_hand:
                print(" you are nice fisherman ! ")
                player1_hand.remove(str(fish_card1))
                player1_pairs +=1
                print(player1_hand)
                print(player2_hand)
                if len(player1_hand) < 1:
                    break
                continue
            else:
                print(f" you were not lucky {player1} ! , now it is computer turn ")
                print(player1_hand)
                print(player2_hand)
                break


    print(f" {player1} you have already achieved ",  player1_pairs,  " scores !" )
    print(" ------------------------------------------------------------ ")

    from random import choice
    while True:
        card_chosen = str(choice(player2_hand))
        print(" computer asked for " + card_chosen)
        if card_chosen in player1_hand:
            player1_hand.remove(card_chosen)
            player2_hand.remove(card_chosen)
            player2_pairs += 1
            print(" computer got the pair! ")
            print(player1_hand)
            print(player2_hand)
            if len(player2_hand) < 1:
                break
            continue
        else:
            print(" computer had to go for fishing ! ")
            if len(card_deck) < 1:
                break
            fish_card2 = str(card_deck.pop())
            if fish_card2 in player2_hand:
                print(" computer knows how to do fishery ! ")
                player2_hand.remove(str(fish_card2))
                player2_pairs +=1
                if len(player2_hand) < 1:
                    break
                continue
            else:
                print(f" computer could not get the pair by fishing, now it is your turn {player1}! ")
                print(" ------------------------------------------------------------------ ")
                break


    print(" computer has already achieved ",  player2_pairs, " scores ")
    print(" ------------------------------------------------------------------- ")


print(f"game over ! " + f" {player1} your scores is " , player1_pairs)
print(" game over ! " + "computer has gained ", player2_pairs, " scores ")
