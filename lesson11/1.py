st = '1234'
lst = list(st)
print(lst)
st2 = str(lst)
print(st2, st2[2:5])
st = 'Привет всем! Я тут!!\ndsfughsdiu\tsjdfgsuy'
print(st)
# split: str -> list[str]
lst = st.split()
print(lst)
st2 = 'Привет#всем!#Я#тут!!\ndsfughsd#iu\tsjdfgsuy'
lst2 = st2.split("#")
print(lst2)
