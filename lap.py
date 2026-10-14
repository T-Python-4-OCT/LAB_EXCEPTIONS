def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)


try:
    additoin(10, 20)
except NameError as err:
    print(f"A variable is not defined: {err}")
except Exception as err:
    print("There is an error")
else:
    print("the operation is successful")