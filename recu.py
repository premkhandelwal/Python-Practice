def num(g):
    if(g == 10):
        return
    num(g + 1)
    print(g)


num(1)        