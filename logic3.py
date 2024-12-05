'''logic examples again
'''

x = 5
y = 7
z = 10

if x < y:
   print(x)
   #get a value
   z = int(input())
   if z % 2 == 0:
      print(z, "is even.")
   else:
      print(z, "is odd.")
else:
   print(y)

print(z)