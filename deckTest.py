import deck

def main():
    adeck = deck.Deck()
    print(adeck)
    adeck.shuffle()
    print("****AFTER SHUFFLING****")
    print(adeck)
    mycard = adeck.deal()
    print(mycard)
    yourcard = adeck.deal()
    print(yourcard)

main()
