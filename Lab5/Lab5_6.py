import math


def card_shuffle(list):

    cards_first_half= list[0:len(list)//2]
    '''for i in range(0,(len(list))//2):
        cards_first_half.append(list[i])'''

    cards_second_half= list[len(list)//2:len(list)]

    '''for i in range((len(list))//2,len(list)):
        cards_second_half.append(list[i])'''

    shuffled_cards=[]
    for i in range (0,len(list)//2):
        shuffled_cards.append(cards_first_half[i])
        shuffled_cards.append(cards_second_half[i])

    print(shuffled_cards)




print("Enter the numbers on the cards with spaces in between (No of cards should be even) : ")
cards=[int(x) for x in input().split()]
card_shuffle(cards)

