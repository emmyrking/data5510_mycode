# import Class made in other file
from DeckOfCards import *


#--------------- Welcome User to the game and set up deck---------------#
print("Welcome to Black Jack!")

# Create a deck of cards
deck = DeckOfCards()

# start a round of Black Jack 
while(True):

    # print the deck, shuffle the deck, and print againg
    print()
    print("Deck before shuffle:")
    deck.print_deck()
    print()
    print("Deck after shuffle:")
    deck.shuffle_deck()
    deck.print_deck()


    #--------- User's hand (plus keeping track of aces) ---------#
    # deal two cards to the user
    card = deck.get_card()
    card2 = deck.get_card()

    # establish variable to keep track of user's aces
    aces = 0

    # if the card value is 11, that means it is an ace
    if card.val == 11:
        aces += 1

    if card2.val == 11:
        aces += 1


    # tell user what two cards were dealt
    print(f"Card Number 1 is: {card}")
    print(f"Card number 2 is: {card2}")

    # establish starting variable for user score
    score = 0

    # calculate the user's hand score
    score += card.val
    score += card2.val

    # if user has two aces and busted, the ace will be valued at 1 instead of 11
    while(score > 21 and aces > 0):
        score -= 10
        aces -= 1

    # print out score to the user
    print("Your score is: ", score)

    #--------- Dealer's hand ---------#
    # deal two cards to the dealer
    card3 = deck.get_card()
    card4 = deck.get_card()

    # establish variable to keep track of dealer's score
    dealer_score = 0

    # calculate the dealer's hand score
    dealer_score += card3.val
    dealer_score += card4.val

    # establish variable to keep track of dealer's aces
    dealer_aces = 0

    # if the card value is 11, that means it is an ace
    if card3.val == 11:
        dealer_aces += 1

    if card4.val == 11:
        dealer_aces += 1

    # if dealer has an ace and busted, the ace will be valued at 1 instead of 11
    while(dealer_score > 21 and dealer_aces > 0):
        dealer_score -= 10
        dealer_aces -= 1

    #------- Start while loop to continuing asking if user wants to hit -------#

    # establish variable to keep track of number of times hit
    times = 0

    # first cleck to see if user's score is equal to 21
    if score == 21:
        print("Congrats!! You got 21!!!")

    else: 
        while(True):

            # ask user if they would like a "hit" (another card)
            hit = input("Would you like a hit? (y/n)")

            # if user replies yes 
            if hit == 'y':
                card5 = deck.get_card()
                score += card5.val
                times += 1

                # if the card value is 11, that means it is an ace
                if card5.val == 11:
                    aces += 1

                # if user has an ace and busted, the ace will be valued at 1 instead of 11
                while(score > 21 and aces > 0):
                    score -= 10
                    aces -= 1

                # print out the card shown and the new score
                print(f"Card number {times + 3} is: {card5}")
                print("New score: ", score)

                # if user's score exceeds 21 they bust!
                if score > 21:
                    print("You busted! Dealer wins.")
                    break

                # if user's score is equal to 21
                if score == 21:
                    print("Congrats!! You got 21!!!")
                    break
            
            # if user replies no
            elif hit == 'n':
                break
            
            # if user enters anything besides y or n
            else:
                print("Please enter either y for yes or n for no")


    #---------- Showing dealer score and declaring winner ----------#
    dealer_times = 0

    # if user did not bust, show dealer score
    if score <= 21:
        print(f"Dealer card number 1 is: {card3}")
        print(f"Dealer card number 2 is: {card4}")

        # if dealer's score is less than or equal to 16, they hit
        while(dealer_score <= 16): 
            card6 = deck.get_card()
            dealer_score += card6.val
            print(f"Dealer hits, card number {dealer_times + 3} is: {card6}")
            dealer_times += 1
        
            # if the card value is 11, that means it is an ace
            if card6.val == 11:
                dealer_aces += 1

            # if dealer has an ace and busted, the ace will be valued at 1 instead of 11
            while(dealer_score > 21 and dealer_aces > 0):
                dealer_score -= 10
                dealer_aces -= 1

        # print out dealers score
        print("Dealer score is: ", dealer_score)

        # if dealer's score exceeds 21 they bust!
        if dealer_score > 21:
            print("Dealer busted! You win!!!")

        # if your score is higher than the dealers...
        elif score > dealer_score:
            print("Your score is higher than the dealers, you win!!!")

        # if dealer score is higher than yours...
        elif score < dealer_score:
            print("Dealer score is higher, you lose!")

        # if you and the dealer have the same score
        else:
            print("Your score is the same as the dealer. Dealer wins, you lose!")


    #------ ask user if they want to play another game ------#
    another_game = input("Do you want to play another game?(y/n)").lower()

    if another_game == 'y':
        pass

    elif another_game == 'n':
        break

    else:
        print("Please enter either y or n")

print("Thank you for playing Black Jack!")



