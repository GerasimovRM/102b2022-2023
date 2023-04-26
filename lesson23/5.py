try:
    n = int(input())
    print(1. / n)
except ZeroDivisionError:
    print('на нуль делят только в пределе')
except ValueError:
    print('это не инт!!')

raise AttributeError('!!ывдмвыдм')
