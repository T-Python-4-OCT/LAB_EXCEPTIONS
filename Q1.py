# class notDefinedError(Exception):
    # pass

def addition(x, y):
    try:

        print("Addition:", x + b)
        print("The operation is successful.")
        
    except NameError:
        print("Error: variable is not defined.")
    except Exception as e:
        print(e)
    

addition(10, 20)

# def addition1(x, y):
#     try:

#         print("Addition:", x + y)
#         print("The operation is successful.")
        
#     except NameError:
#         print("Error: variable is not defined.")
#     except Exception as e:
#         print(e)

# addition1(10, "v")
