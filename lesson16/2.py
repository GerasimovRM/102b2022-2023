def matrix(n=1, m=None, a=0):
    if m is None:
        m = n
    lst = [[a] * m for _ in range(n)]
    return lst

