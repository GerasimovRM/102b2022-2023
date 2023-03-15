def func(x, y, z=3, w=4, *args, kw1=10, kw2=None, **kwargs):
    print(x, y, z, w)
    print(args)
    print(kw1, kw2)
    print(kwargs)


d = {"kw2": True,
     "find": 'Person1',
     "pasijdfaspifj": 'soudhfios'}
lst = list(range(100))
func(*lst, **d)
