import math
import random

cards = [1,2,3,4,5,6,7,8,9,"A","Q","K"]


def card_picker():
    range_card = random.choice(cards)
    return range_card

def total_sum(card_list):
    sum = 0
    for i in card_list:
        if i == "K" or i == "Q":
            sum +=10
        elif i != "A":
            sum += i
    if "A" in card_list:
        if sum > 11:
            sum += 1
        elif sum < 11:
            sum += 1

    return sum


player_cards = []
player_sum = 0
computer_cards = []
computer_sum = 0
player_cards.append(card_picker())
computer_cards.append(card_picker())
computer_cards.append(card_picker())

player_sum = total_sum(player_cards)

game_continue = True

while game_continue:
    print("Your cards and sum ",player_cards,player_sum)
    print("Computer cards ",computer_cards[0])
    more_card = input("Would you like to pick another card: (y/n)")
    if more_card == "y":
        player_cards.append(card_picker())
        player_sum = total_sum(player_cards)
    elif more_card == "n":
        game_continue = False

while total_sum(computer_cards)>16:
    computer_cards.append(card_picker())

computer_sum = total_sum(computer_cards)
player_sum = total_sum(player_cards)

if player_sum > 21:
    print("YOU LOOSE")
    print("your cards",player_cards,player_sum)
    print("computer cards", computer_cards, computer_sum)

elif player_sum > computer_sum:
    print("YOU WIN")
    print("your cards",player_cards,player_sum)
    print("computer cards", computer_cards, computer_sum)

elif player_sum < computer_sum:
    print("YOU LOOSE")
    print("your cards", player_cards, player_sum)
    print("computer cards", computer_cards, computer_sum)

else:
    print("DRAW")
    print("your cards", player_cards, player_sum)
    print("computer cards", computer_cards, computer_sum)