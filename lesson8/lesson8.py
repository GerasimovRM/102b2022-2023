from random import shuffle


st = """Григорий
Вадим
Валерий
Ярослав
Артем
Иван
Игорь
Константин
Анастасия
Максим
Виктория
Глеб
"""

lst = st.split()
shuffle(lst)
for i, name in enumerate(lst, 1):
    print(i, name)