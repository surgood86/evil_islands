def merge_dictionaries(*dicts):
    my_dict = {}
    for d in dicts:
        for key, value in d.items():
            if key not in my_dict:
                my_dict[key] = value
    return my_dict


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

my_dict = merge_dictionaries(dict1, dict2)
print(my_dict)
