def additoin(x, y):
    try:
        x = 10
        y = 20

        print("Addition:", x + d)
    except NameError:
        print("the Name is not found")
    except Exception as a:
        print(a.__class__)
    else:
        print("the operation is successful")

additoin(10, 20)
