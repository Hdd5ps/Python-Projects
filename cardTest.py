import card

def main():
    mycard = card.Card()
    
    print(mycard)
    
    mycard.setFace(30)
    mycard.setSuit(50)
    print("the card face is:",mycard.getFace())
    print("the card suit is:",mycard.getSuit())
    print(mycard)
    yourcard = card.Card(2,'diamonds')
    print(yourcard)

main()
