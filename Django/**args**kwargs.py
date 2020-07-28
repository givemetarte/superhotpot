def plus(a, b, *args, **kargs):
    print(args)
    print(kargs)
    return a + b


plus(1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, kdys=True, ksyd=True)
