
# 
def celsius_to_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * 5/9
  return celsius

def Converter():
  
  while True:
    try: 

      UserEnter = (input('Please Enter a Temprature and its unit (e.g., "25 C" or "77 F")').split())
    
      if len(UserEnter) != 2:
        raise ValueError("Please enter a temperature and a unit.")

      toFloat = float(UserEnter[0])
      toString = str(UserEnter[1])

      if toString == 'C':
          result = celsius_to_fahrenheit(toFloat)
          print(f"The Temperature in Fahrenheit: {result:.2f} F")
          break
      
      elif toString == 'F':
          result = fahrenheit_to_celsius(toFloat)
          print(f"The Temperature in Celsius: {result:.2f} C")
          break
      
      else:
        raise TypeError ('Invalid Unit Entered!')
    
    except ValueError as e:
            print("Invalid temperature:", e)
            print("Please try again.")
    
    except TypeError as e:
      print(type(e).__name__)


Converter()