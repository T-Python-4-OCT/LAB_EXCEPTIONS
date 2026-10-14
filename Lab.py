def addition(x, y):
  
  try:
    x = 10
    y = 20
    print("Addition:", x + b)
    print('The Operation is Successful')
    
  except Exception as e :
      print('The variable you added not initialized!')
      print('The Exception Error is:',type(e).__name__)

addition(10, 20)