# (кофе, молоко, сливки)
d = {
    "Эспрессо": [1, 0, 0],
    "Капучино": [1, 3, 0],
    "Маккиато": [2, 1, 0],
    "Кофе по-венски": [1, 0, 2],
    "Латте Маккиато": [1, 2, 1],
    "Кон Панна": [1, 0, 1]
}


def choose_coffee(*args):
    global ingredients
    for arg in args:
        drink = d[arg]
        if ingredients[0] >= drink[0] and \
                ingredients[1] >= drink[1] and \
                ingredients[2] >= drink[2]:
            ingredients[0] -= drink[0]
            ingredients[1] -= drink[1]
            ingredients[2] -= drink[2]
            return arg
    return "К сожалению, не можем предложить Вам напиток"
