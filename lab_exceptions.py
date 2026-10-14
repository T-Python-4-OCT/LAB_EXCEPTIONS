def additoin(x, y):
    
        x = 10
        y = 20

        print("Addition:", x + b)
try:
    additoin(10, 20)
except NameError:
    print("the Name is not found")
except Exception as a:
        print(a.__class__)
else:
        print("the operation is successful")


