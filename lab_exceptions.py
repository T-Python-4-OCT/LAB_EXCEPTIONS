def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)


try:
    additoin(10, 20)
except NameError as e:
    print("The operation failed: a variable is used before it is defined.")
    print("Details:", e)
else:
    print("the operation is successful")