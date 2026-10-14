

def celsius_to_fahrenheit(celsius):
  return (celsius * 9 / 5) + 32



def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9



def main():
  while True:
    try:
     
      user_input = input(
          'Enter a temperature and its unit ( "25 C" or "77 F"): '
      )

     
      parts = user_input.split()
      if len(parts) != 2:
        raise ValueError(
            "Invalid format. Please enter number and unit separated by space."
        )

      temp_value = float(parts[0])  
      unit = parts[1].upper()  

      if unit == "C":
        converted = celsius_to_fahrenheit(temp_value)
        print(f"Temperature in Fahrenheit: {converted} F\n")
        break 

      elif unit == "F":
        converted = fahrenheit_to_celsius(temp_value)
        print(f"Temperature in Celsius: {converted} C\n")
        break 
      else:
        raise TypeError(
            "Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit."
        )

    except ValueError as e:
      print(f"Error: {e}. Please try again.\n")
    except TypeError as e:
      print(f"{e}\n")


main()
