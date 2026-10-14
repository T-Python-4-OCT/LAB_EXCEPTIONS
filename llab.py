def additoin(x, y):
    x = 10
    y = 20
    #print("Addition:", x + b)
    try:
        print("Addition:", x + b)
    except NameError as e:
        print(" Error is: ",e)   
    else:
        print("the operation is successful")


additoin(10, 20)