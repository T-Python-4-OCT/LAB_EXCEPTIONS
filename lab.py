def additoin(x, y):
    x = 10
    y = 20
    try:
        print("Addition:", x + y)
    except NameError:
        print("Operation failed: b is not defined!")
    else:
        print("the operation is successful")


additoin(10, 20)