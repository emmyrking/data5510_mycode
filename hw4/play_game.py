# import Class made in other file
from DeckOfCards import *


#--------------- Welcome User to the game and set up deck---------------#
print("Welcome to Black Jack!")

# Create a deck of cards, print, shuffle, and print again - referencing functions in the class
deck = DeckOfCards()
deck.print_deck()
print()
deck.shuffle_deck()
deck.print_deck()

#--------- User's hand ---------#
# deal two cards to the user
card = deck.get_card()
card2 = deck.get_card()

# tell user what two cards were dealt
print(f"Card Number 1 is: {card}")
print(f"Card number 2 is: {card2}")

score = 0
# calculate the user's hand score
score += card.val
score += card2.val
print("Your score is: ", score)

#--------- Dealer's hand ---------#
# deal two cards to the dealer
card3 = deck.get_card()
card4 = deck.get_card()

dealer_score = 0
# calculate the dealer's hand score
dealer_score += card3.val
dealer_score += card4.val




#------- Start while loop to continuing asking if user wants to hit -------#

# establish counter variable to keep track number of times hit
times = 0

while(True):

    # ask user if they would like a "hit" (another card)
    hit = input("Would you like a hit? (y/n)")

    # if user replies yes and first time hitting
    if hit == 'y' and times == 0:
        card5 = deck.get_card()
        score += card5.val
        print(f"Card number 3 is: {card5}")
        print("New score: ", score)
        times += 1

        # if user's score exceeds 21 they bust!
        if score > 21:
                print("You busted! Dealer wins.")
                break
    

    # if user replies yes and second time hitting
    elif hit == 'y' and times == 1:
        card6 = deck.get_card()
        score += card6.val
        print(f"Card number 4 is: {card6}")
        print("New score: ", score)
        times += 1

        # if user's score exceeds 21 they bust!
        if score > 21:
                print("You busted! Dealer wins.")
                break
    
    # if user replies no
    elif hit == 'n':
        break
    
    # if user enters anything besides y or n
    else:
        print("Please enter either y for yes or n for no")


#---------- Showing dealer score and declaring winner ----------#

# if user did not bust, show dealer score
if score <= 21:
    print(f"Dealer card number 1 is: {card3}")
    print(f"Dealer card number 2 is: {card4}")
    print("Dealer score is: ", dealer_score)

    # if your score is higher than the dealers...
    if score > dealer_score:
        print("Your score is higher than the dealers, you win!!!")

    # if dealer score is higher than yours...
    elif score < dealer_score:
        print("Dealer score is higher, you lose!")

    # if you and the dealer have the same score
    else:
        print("Your score is the same as the dealer. It's a tie!")



