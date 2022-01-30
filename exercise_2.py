def get_combined_dict(dict1: dict[str, int], dict2: dict[str, int]) -> dict[str, int]:
    combined_dict = {}
    for k in dict1:
        if k in dict2:
            combined_dict[k] = dict1[k] + dict2[k]
    return combined_dict


my_dict_1 = {"a": 5, "b": 12, "c": 3, "d": 9}
my_dict_2 = {"b": 4, "c": 9, "d": 10, "e": 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)
