def from_string_to_list(string, container):
    lst = [int(elem) for elem in string.split()]
    # I
    # for elem in lst:
    #     container.append(elem)
    # II
    # container += lst
    # III
    container.extend(lst)
