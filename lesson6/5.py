while True:
    st = input()
    if len(st) > 20 or 'книги' in st:
        continue
    elif 'спорт' in st:
        print("Казнить!")
        break
    elif st == "всё!":
        break
    print("Обещаю!")
