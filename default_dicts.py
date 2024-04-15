from collections import defaultdict

new_dict = dict(one=1, two=1, three = 3)
print(new_dict['one']) # 1

# print(new_dict['four']) # throws key_error for dict

"""default dictionary of integers"""
first_default_dict = defaultdict(int) # defaults keys that DNE to 0
print(first_default_dict[4]) # 0

"""default dictionary of sets"""
second_default_dict = defaultdict(set) # defaults keys that DNE to 0
print(second_default_dict[4]) # set()

second_default_dict['one'].add(1)
second_default_dict['two'].add(2)
second_default_dict['one'].add('1')
second_default_dict['three'] # assigned as an empty set
print(second_default_dict.items())

"""default dictionary of lists"""
third_default_dict = defaultdict(list)

third_default_dict['one'].append(1)
third_default_dict['two'].append(2)
third_default_dict['one'].append('1')
third_default_dict['three'] # assigned as an empty set
print(third_default_dict.items())
