s = "🧁Ass_Muffins🧁"
def convert_to_ord(s):
    lst = []
    for c in s:
        lst.append(ord(c))
    return lst

print(convert_to_ord(s))

def convert_to_str(ord_list):
    out = ""
    for ordinal in ord_list:
        out += chr(ordinal)
    return out

print(convert_to_str(convert_to_ord(s)))

print(chr(1114111))