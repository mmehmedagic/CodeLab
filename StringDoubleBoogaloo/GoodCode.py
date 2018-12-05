s = 'Hey there epic fortnite gamers!'  # input("String? ")  # not counted

b = 0
a = bin(int.from_bytes(s.encode(),'big')).replace('0b','')
for x in a:
  b += int(x)
b**-.5

print(b**-.5)  # not counted
