def additoin(x, y):

    x = 10
    y = 20
    print("Addition:", x + b)

try:
    additoin(10, 20)
except NameError:
    print("Check the names in the printout.")
except Exception as f:
    print(f.__class__)
    print("Try again Something's wrong.")
else:
    print("The program is successful.")
