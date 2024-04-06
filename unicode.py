from pprint import pprint as p

s = "🫥"
def encode(s):
    lst = []
    for c in s:
        lst.append(ord(c))
    return lst

# p(encode(s))

def decode(ord_list):
    out = ""
    for ordinal in ord_list:
        out += chr(ordinal)
    return out

messages = [[76, 101, 116, 115, 32, 103, 101, 116, 32, 116, 104, 105, 115, 32, 127838], [65, 115, 115, 127828, 115]]

def pprint_messages(messages):
    for message in messages:
        p(decode(message))

p(pprint_messages(messages))