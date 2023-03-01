def from_str_to_tuple(st):
    sym_alpha, sym_num = st
    x = ord(sym_alpha.lower()) - ord('a') + 1
    y = int(sym_num)
    return x, y


def from_tuple_to_str(t):
    x, y = t
    sym_alpha = chr(x + ord('a') - 1).upper()
    sym_num = str(y)
    return sym_alpha + sym_num


def possible_turns(cell):
    x, y = from_str_to_tuple(cell)
    turns = [
        (-1, -2),
        (-2, -1),
        (-2, 1),
        (-1, 2),
        (1, 2),
        (2, 1),
        (2, -1),
        (1, -2),
    ]

    result = []
    for i, j in turns:
        new_x = x + i
        new_y = y + j
        if 8 >= new_x >= 1 and 8 >= new_y >= 1:
            result.append(from_tuple_to_str((new_x, new_y)))
    return result


print(from_str_to_tuple("C2"))
print(from_tuple_to_str((3, 4)))
print(possible_turns("B1"))
