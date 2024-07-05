lst = [1,2,2,3,3]

num1 = 12
num2 = 12
num3 = num1 | num2 # syntax for or NOTE: if any are on
num4 = num1 & num2 # syntax for and NOTE: everything on every other case is off
num5 = num1 ^ num2 # syntax for xor NOTE: exclusively one on one off

print(num3) # 12
print(num4) # 12
print(num5) # 0
print(bin(num2)) # quick convert to binary NOTE: remove header elements @ positions 0 and 1
print(int(bin(num2)[2:], 2)) # passing int module a base of 2 will convert back to decimal
print(int(bin(num2), 2)) # passing entire representation also converts

hex1 = 0xc
bit2 = 0b100
num7 = bit2 >> 1
num8 = bit2 << 1
print(num7) # 2
print(num8) # 8

print(hex1 << 1) # NOTE: can shift hexadecimal as well