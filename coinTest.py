import coin

mycoin = coin.Coin()

print(mycoin.getSide())
print(mycoin.getValue())

#toss the coin
for t in range(10):
	mycoin.toss()

#now print again
	print(mycoin.getSide())

mycoin.__sideup = 'edge'
print(mycoin.getSide())
print(mycoin.getValue())
'''
otherCoin = coin.Coin(25)

print(mycoin.getSide())
print(otherCoin.getSide())
print(otherCoin.getValue())
print(mycoin.getValue())
'''
counters = [0] * 26

mstring = "aaa bbb cccc ddddd".upper()
for ch in mstring:
	if ch.isalpha():
		counters[ord(ch)-65]+=1
		
print(counters)
