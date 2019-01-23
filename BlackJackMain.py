import random

deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
        '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
        '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
        '10 of Spades':10, 'Jack of Spades':10,
        'Queen of Spades':10, 'King of Spades': 10,
        'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
        '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
        '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
        '10 of Hearts':10, 'Jack of Hearts':10,
        'Queen of Hearts':10, 'King of Hearts': 10, 'Ace of Clubs':1,
        '2 of Clubs':2, '3 of Clubs':3, '4 of Clubs':4, '5 of Clubs':5,
        '6 of Clubs':6,'7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
        '10 of Clubs':10, 'Jack of Clubs':10,
        'Queen of Clubs':10, 'King of Clubs': 10,
        'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
        '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
        '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
        '10 of Diamonds':10, 'Jack of Diamonds':10,
        'Queen of Diamonds':10, 'King of Diamonds': 10}

def value(hand):
    hand_value = 0
    for i in hand:
        hand_value += deck[i]
    return hand_value


def main():
    keys = list(deck)
    random.shuffle(keys)

    player1_hand = []
    computer_hand = []

    player1_score = 0
    computer_score = 0
    for i in range(2):
        player1_hand.append(keys.pop())
    while player1_score < 21:
        player1_score = value(player1_hand)
        print ("Player 1's hand is ", player1_hand, "The value is ", player1_score)
        if player1_score < 21:
            response = int(input('How many cards should I deal to player1? '))
            if response == 0:
                break
            else:
                for i in range(int(response)):
                    player1_hand.append(keys.pop())
        else:
            print("Opponent's Turn")
            break
    #dealing to the Computer
    for i in range(2):
        computer_hand.append(keys.pop())
    while computer_score < 21:
        computer_score = value(computer_hand)
        print ("Opponents's hand is ", computer_hand, "The value is ", computer_score)
        if computer_score >= 17:
            print("Game Over")
            break
        else:
            computer_hand.append(keys.pop())


    print (player1_hand, value(player1_hand))
    print (computer_hand, value(computer_hand))

if __name__ == "__main__":
    main()