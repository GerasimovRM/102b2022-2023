is_player1 = True

s = set()
city_tmp = None

while True:
    if is_player1:
        city = input("Player 1: ")
    else:
        city = input("Player 2: ")
    if not city:
        break
    if not city_tmp:
        s.add(city)
    elif city_tmp[-1] == city[0] and city not in s:
        s.add(city)
    else:
        print("Попробуйте еще раз!")
        continue

    city_tmp = city
    is_player1 = not is_player1
