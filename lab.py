
def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)
     
     
try:
    additoin(10, 20)
         
except NameError as e:
    print("There is no b in the Function-->",e)
    print(e.__class__)
    
else:
    print("The addition went seccissfuly")
    
finally:
    print("run whethrt successful or not ")

    

