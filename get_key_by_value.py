def get_key_by_value(obj, value):
    return next((key for key, val in obj.items() if val == value), None)


my_dict = {"a": 1, "b": 2, "c": 3}
value_to_find = 2
key = get_key_by_value(my_dict, value_to_find)
print(key)
