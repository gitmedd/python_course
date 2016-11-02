"""
Main program description.

    Author: Dr David Drury
    Date: 1st November 2016
    Version: 0.1

    Now on git repository

    Aim: Python Homework Project 2: Design and code a Blackjack game using
    the principle of obejcts extensively

    TODOS:
    This is the file that defines the functions and implements the main code
    for the Blackjack game problem.
    DONE - Define a card class
    DONE - Define a deck class
    DONE - Define a player
    TODO - Implement Gameplay
    DEFINITION
    DONE - 1. Dealer deal first card to each player face down then
    the dealer lays face up
    DONE - 2. Each player lays out stake
    DONE - 3. Dealer deals out second card to all including dealer, face down
    IN PROGRESS - 4. Each player has the following choices:
    DONE - Twist, get another card for no extra stake, face up
    IN PROGRESS - Buy, purchase another card at the initial stake, face down
    DONE - Bust, stop having got over 21, lose stake, turn cards face up
    DONE - Stick, wait and pass to next player, cards remain face down
    5. Once all players have engaged in step 4. then the dealer turns his cards
    and plays to the highest score
"""


from __future__ import print_function
import random


class Card(object):
    """
    Primimtive card class definintion.

    A simple card class that stores info about the suit and value of a card.
    """

    def __init__(self, cardID, suit=1, name=1, faceUp=False):
        """Initialisation of the card function."""
        self.cardID = cardID
        self.suit = suit
        self.name = name
        self.faceUp = False


class Pile(object):
    """
    Main class for piles of cards.

    The base class for any pile of cards.
    This can be a deck, a players hand or a discard/pick up pileTop
    """

    colors = 2
    suitsPerColor = 2
    valuesPerSuit = 13
    jokersPerColor = 1
    jokersNeeded = ""
    suits = ["Clubs", "Spades", "Diamonds", "Hearts"]
    suitsAbb = ["C", "S", "D", "H"]
    cardNames = [
        "1", "2", "3", "4",
        "5", "6", "7", "8",
        "9", "10", "Jack", "Queen",
        "King", "Joker"
    ]
    cardNamesAbb = [
        "1", "2", "3", "4",
        "5", "6", "7", "8",
        "9", "10", "J", "Q",
        "K", "W"
    ]
    cardValues = [
        1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 10, 10,
        10, 1
    ]

    pileTop = 0
    pileLocation = 0

    def __init__(self, full):
        """
        Function - Initialisation of the module.

        Parameters
            - full - parameter that determines whether or not
            the deck contains cards
            if full = 0 an empty deck is dealt
            if full = 1 a full deck is dealt and shuffled
        """
        self.cards = []

        if full == 1:
            # Insert the normal cards into the deck
            for loop1 in range(0, self.suitsPerColor*self.colors):
                for loop2 in range(0, self.valuesPerSuit):
                    self.cards.append(
                        Card(loop2+(loop1*self.valuesPerSuit), loop1,
                             loop2, False)
                    )
            # print("Normal cards inserted")
            # Insert jokers into the deck
            for loop1 in range(0, self.jokersPerColor*self.colors):
                self.cards.append(Card(loop1 + (
                    self.colors*self.suitsPerColor*self.valuesPerSuit),
                    loop1*2, 13, False)
                )
            # print("Jokers inserted")
            # Update the total number of cards into the deck
        self.pileTotal = len(self.cards)
        # print("Number of cards =", self.pile_count())

        # Shuffle the deck
        # self.list_pile()
        if full == 1:
            self.pile_shuffle()
        # self.list_pile_short()

        # print("Done\n")

    def print_card_name(self, card):
        """Print the full name of the card (number and suit)."""
        print(self.cardNames[card.name], "of", self.suits[card.suit])

    def print_card_name_short(self, card):
        """
        Short printout.

        Print a short version of the card number and suit (one
        letter for each).
        """
        print(
            self.cardNamesAbb[card.name], ":",
            self.suitsAbb[card.suit],
            sep="", end="")

    def pile_count(self):
        """
        Count the number of cards in the pile.

        Return an integer with the nuber of cards in the pile.
        """
        return len(self.cards)

    def pile_value(self, private):
        """
        Pile Value Calculator.

        Return an integer with the total face value of the cards
        in the pile_value.
        """
        tempTotal = 0
        for loop1 in range(0, self.pile_count()):
            tempTotal += self.cardValues[self.cards[loop1].name]
            if private is True:
                tempTotal = 0
        return tempTotal

    def pile_shuffle(self):
        """
        Routine that shuffles the deck.

        This is the routine that shuffles the deck by
        randomising the pile order.
        """
        random.shuffle(self.cards)
        # print("Pile Shuffled")

    def list_pile(self):
        """
        List the contents of the pile longform.

        Return a string with each card described followed by a line
        return.
        """
        for loop1 in range(0, self.pile_count()):
            print("Card %d is the %s of %s" % (
                loop1, self.cardNames[self.cards[loop1].name],
                self.suits[self.cards[loop1].suit])
            )

    def list_pile_short(self, private):
        """
        Shortform pile listing.

        Return a string with the entire pile described using
        short codes and normal line returns.
        """
        for loop1 in range(0, self.pile_count()):
            if ((private is False) or (self.cards[loop1].faceUp is True)):
                print("%2s:%s | " % (
                    self.cardNamesAbb[self.cards[loop1].name],
                    self.suitsAbb[self.cards[loop1].suit]),
                    end=""
                )
            else:
                print(" X:X | ", end="")

    def get_pile_pos(self):
        """Return an integer expressing the location in the pile."""
        return self.pileLocation

    def show_top_card(self):
        """
        A function to revela the top card.

        Function that gives details of the top
        card without affecting its position in the pile.
        """
        return self.cards[self.get_pile_pos()]

    def remove_card(self, location):
        """
        remove_card.

        location: Location of card in the deck to remove
        Function that removes the card at the location from the pile.
        """
        self.cards.pop(location)

    def add_to_pile(self, cardGiven):
        """Add the card in the argument to the pile."""
        # print("Appending ", end="")
        # print("", end="")
        # self.print_card_name_short(cardGiven)
        self.cards.append(cardGiven)

        # print()

        # def show_pile_order(self):
        #     for loop1 in range(1, self.pileCount):
        #         print(self.pileOrder[loop1], ",")

    def make_card_face_up(self, cardLocation):
        """Function that converts card at given location to face up."""
        self.cards[cardLocation].faceUp = True

    def give_top_card(self):
        """Function that gives the top card away from this pile."""
        cardToGive = self.show_top_card()
        # print("Top card being given = ", end="")
        # self.print_card_name_short(cardToGive)
        # print()
        self.remove_card(self.pileLocation)
        return cardToGive
        # return self.cardpackOrder
        # print pile.card[pileOrder[loop1]].cardID

    def move_top_to_bottom(self):
        """
        A function.

        Function that places the card on the top of the pile
        and places it on the bottom of the pile.
        """
        self.pileLocation += 1
        if (self.pileLocation / self.pileCount == 1):
            self.pileLocation = self.pileLocation - self.pileCount

    def take_card(self, card):
        """Function that accepts a card from another pile."""


class Player(object):
    """
    Player class.

    Base class that contains a players hand (as a pile)
    and his stake.
    """

    stake = 0

    def __init__(self, playerNumber, cashTotal):
        """Initialisation function for the player class."""
        # print("Player %d pile initialising" % (playerNumber+1))
        self.pile = Pile(0)
        self.cashTotal = cashTotal
        self.playerNumber = playerNumber
        self.status = "OK"
        self.initialStake = 0

    def print_cards(self, private):
        """Printer out the players cards or XXs if they area face down."""
        print(
             "| Player %2d |  %6s  |  %4d  |  %4d |  %4d | "
             % (self.playerNumber+1,
                self.status, self.cashTotal, self.stake,
                self.pile.pile_value(private)
                ), end="")
        self.pile.list_pile_short(private)
        print("")

print("Setup main deck")

deck = Pile(1)
players = 3
turn = 0
endGame = False
player = []
initial_cash = 100
dealer = 0


def print_game_status(cardsPrivate, playerNo):
    """Print out the status of the game for all players."""
    print("=================================================")
    print("| Player No |  STATUS  | Wallet | Stake | Total | Cards")
    print("-------------------------------------------------")
    for loop1 in range(0, players):
        if (loop1 == playerNo):
            player[loop1].print_cards(cardsPrivate)
        else:
            player[loop1].print_cards(True)
    print("=================================================\n")


def playTurn(playerNo):
    """Play the turn for player number PlayerNo."""
    turnFinished = False
    print("Player %2d" % (playerNo+1))
    while turnFinished is False:
        if player[playerNo].pile.pile_value(False) > 21:
            print("You have bust!! Game over for you!!!")
            player[0].cashTotal += player[playerNo].stake
            player[playerNo].stake = 0
            player[playerNo].status = "BUST!"
            turnFinished = True
            break
        print_game_status(False, playerNo)
        moveType = raw_input(
                            "Would you like to twist (T), stick (S)"
                            " or buy a card(B)? "
                            )
        print(moveType.lower())
        print()
        if moveType.lower() == "t":
            player[playerNo].pile.add_to_pile(deck.give_top_card())
            player[playerNo].pile.make_card_face_up(
                                                    player[playerNo]
                                                    .pile.pile_count()-1)
            print ("Card Added")
        elif moveType.lower() == "s":
            player[playerNo].status = "STICK!"
            turnFinshed = True
            break
        elif moveType.lower() == "b":
            print("buy start")
            player[playerNo].pile.add_to_pile(deck.give_top_card())
            player[playerNo].cashTotal -= player[playerNo].initialStake
            player[playerNo].stake += player[playerNo].initialStake
            print("buy end")


# deck.list_pile()

# print("Initialise players piles\n========================")
print("\nGame On!!!")
for loop1 in range(0, players):
    player.append(Player(loop1, initial_cash))
    player[loop1].pile.add_to_pile(deck.give_top_card())
    if loop1 is 0:
        player[loop1].pile.make_card_face_up(0)
print_game_status(True, 2)


"""Take players initial stakes"""
for loop1 in range(1, players):
    stakeRequired = True

    while stakeRequired:
        try:
            print("Player %d, Make your initial stake" % (loop1+1))
            print_game_status(False, loop1)
            print("Player %d, Your " % (loop1+1), end="")
            stake = round(float(raw_input("Stake = ")))
        except ValueError:
            print()
            print("Your stake must be a number less than your wallet content"
                  " in whole pounds")
            print()
            continue
        else:
            if stake < player[loop1].cashTotal:
                print("Accepted stake = %d, wallet = %d."
                      % (stake, player[loop1].cashTotal-stake), end="")
                response = raw_input("  Happy? (Y/N): ")
                if response.lower() == "y":
                    print("Stake accpeted")
                    player[loop1].stake = stake
                    player[loop1].initialStake = stake
                    player[loop1].cashTotal -= stake
                    print("Player %d Accepted stake = %d, wallet = %d."
                          % (loop1+1, stake, player[loop1].cashTotal-stake))
                    stakeRequired = False
                    print("Stake successfully entered")
            else:
                print()
                print("Stake too large, please try again")
                print()
print("All stakes entered")

print()
print("Second cards dealt")
for loop1 in range(0, players):
    player.append(Player(loop1, initial_cash))
    player[loop1].pile.add_to_pile(deck.give_top_card())
    if loop1 is 0:
        player[loop1].pile.make_card_face_up(0)
    player[loop1].print_cards(False)
print("\n==============\n")

print()
for loop1 in range(1, players):
    playTurn(loop1)

playTurn(0)  # Need to adjust Playturn so that dealer gives money away

print()
print("Game Over for all")
print_game_status(False, 0)
