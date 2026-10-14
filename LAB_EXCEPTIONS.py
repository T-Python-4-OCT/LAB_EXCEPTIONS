def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + y)

try:
    additoin(10, 20)
except NameError:
    print("Error: One of the variables in the operation is not defined.")
else:
    print("the operation is successful")