for i in range(1, 9):
    print("Началсь итерация", i)
    if i == 3:
        print("УПС. Неожиданный перескок на след. итерацию")
        continue
    elif i == 5:
        print("УПС. Неожиданное завершение цикла")
        break
    print("Закончилась итерация", i)
