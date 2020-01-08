def remove_duplicates(list):
    list2 = []
    if list:
        for item in list:
            if item not in list2:
                list2.append(item)
    else:
        return list
    return list2


print(remove_duplicates([1, 2, 3, 3, 4, 4]))§
