lst = [1,2,2,3,3]

num1 = 12
num2 = 12
num3 = num1 | num2 # syntax for or
num4 = num1 & num2 # syntax for and
num5 = num1 ^ num2 # syntax for xor

print(num3) # 12
print(num4) # 12
print(num5) # 0
print(bin(num2)) # quick convert to binary NOTE: remove header elements @ positions 0 and 1
print(int(bin(num2)[2:], 2)) # passing int module a base of 2 will convert back to decimal
print(int(bin(num2), 2)) # 12
