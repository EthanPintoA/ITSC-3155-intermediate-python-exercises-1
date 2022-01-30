def get_unique_list(l: list) -> list:
    return list(set(l))


my_list = [0,9,8,6,5,9,6,4,4,1]
unique_list = get_unique_list(my_list)
print(unique_list)
