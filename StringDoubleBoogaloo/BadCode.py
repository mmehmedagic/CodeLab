s = 'Hey there epic fortnite gamers!'  # input("String? ")  # not counted

# 84 chars
b=0
for x in bin(int.from_bytes(s.encode(),'big')).replace('0b',''):b+=int(x)
b**-.5

print(b**-.5)  # not counted
