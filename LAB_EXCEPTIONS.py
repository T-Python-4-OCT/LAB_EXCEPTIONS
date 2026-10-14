def additoin(x, y):
    try:
        x = 10
        y = 20
        result = x + b
        print("Addition:", result)
    except NameError:
        print("The operation failed: variable 'b' is not defined.")
    else:
        print("the operation is successful")


additoin(10, 20)