import random

CARD = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
PLAYER = []
DEALER = []
PLAYER_TOTAL = []
DEALER_TOTAL =[]


def hit():
    """Hit"""
    return random.choice(CARD)


def player_start():
    PLAYER.append(hit())
    PLAYER.append(hit())
    print(f"Player: {PLAYER}")


def player_total_count():
    for P in PLAYER:
        if P == "J":
            P = 10
        elif P == "Q":
            P = 10
        elif P == "K":
            P = 10
        elif P == "A":
            P = 11
        else:
            P = int(P)
        PLAYER_TOTAL.append(P)
    print(f"Player scores: {sum(PLAYER_TOTAL)}")
    print("""""")


def dealer_start():
    DEALER.append(hit())
    print(f"Dealer: {DEALER}")


def dealer_total_count():
    for D in DEALER:
        if D == "J":
            D = 10
        elif D == "Q":
            D = 10
        elif D == "K":
            D = 10
        elif D == "A":
            D = 11
        else:
            D = int(D)
        DEALER_TOTAL.append(D)
    print(f"Dealer scores: {sum(DEALER_TOTAL)}")


def player_hit_or_not():
    while True:
        c = input("Do you want one more card? (Y/N): ")
        if c == "Y" or c == "y":
            PLAYER.append(hit())
            print(f"Player: {PLAYER} ")
            for P in PLAYER:
                if P == "J":
                    P = 10
                elif P == "Q":
                    P = 10
                elif P == "K":
                    P = 10
                elif P == "A":
                    P = 1
                else:
                    P = int(P)
            PLAYER_TOTAL.append(P)
            print(f"Player scores: {sum(PLAYER_TOTAL)}")
            print("""""")
            if sum(PLAYER_TOTAL) > 21:
                print("You Lose!")
                break
        elif c == "N" or c == "n":
            while sum(DEALER_TOTAL) < sum(PLAYER_TOTAL):
                DEALER.append(hit())
                print(f"Dealer: {DEALER}")
                for D in DEALER:
                    if D == "J":
                        D = 10
                    elif D == "Q":
                        D = 10
                    elif D == "K":
                        D = 10
                    elif D == "A":
                        D = 1
                    else:
                        D = int(D)
                DEALER_TOTAL.append(D)
                print(f"Dealer scores: {sum(DEALER_TOTAL)}")
                print("""""")
            if sum(DEALER_TOTAL) >= sum(PLAYER_TOTAL) and sum(DEALER_TOTAL) <= 21:
                print("You Lose!")
                break
            else:
                print("You won!")
                break
        else:
            print("Please enter 'Y' or 'N'.")


def main():
    player_start()
    player_total_count()
    dealer_start()
    dealer_total_count()
    player_hit_or_not()

main()


