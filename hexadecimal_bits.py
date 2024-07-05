num2 = 3

print(hex(num2)) # quick convert to hex NOTE: remove header elements @ positions 0 and 1
print(int(hex(num2)[2:], 16)) # hexadecimal base of 16 will convert back to decimal
print(int(hex(num2), 16)) # 12