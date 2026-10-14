# The original code raises a NameError: the variable `b` is never defined.
# (The parameters x and y are also overwritten inside the function.)

def additoin(x, y):
    x = 10
    y = 20
    try:
        print("Addition:", x + b)
    except NameError as e:
        print("The operation failed - a variable is not defined:", e)
    else:
        print("the operation is successful")


additoin(10, 20)
