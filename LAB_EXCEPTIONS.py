def additoin(x, y):
    x = 10
    y = 20
    try:
        print("Addition:", x + b)
    except NameError as e:
        print(f"Operation failed: A NameError occurred because variable 'b' is not defined. ({e})")
    else:
        print("the operation is successful")

additoin(10, 20)