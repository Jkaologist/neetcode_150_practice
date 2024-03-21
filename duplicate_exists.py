from typing import Counter


def two_or_more(my_list):
    c = Counter(my_list)
    for count in c.values():
        if count >= 2:
            return False
    return True


two_or_more([1, 2, 3, 4, 5])
