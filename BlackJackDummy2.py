import random
import DeckClass


def value(hand):
    hand_value = 0
    for i in hand:
        hand_value += deck[i]
    return hand_value


def main():
    deckInstance = DeckClass
    deckInstance.
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