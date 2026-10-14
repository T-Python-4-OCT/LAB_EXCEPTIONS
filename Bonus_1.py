def celsius_to_fahrenheit(celsius):

  
        fahrenheit = round((celsius * 9/5) + 32, 2)
        print(f"{celsius}°C is equal to {fahrenheit}°F")
        return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    
        celsius = round((fahrenheit - 32) * 5/9, 2)
        print(f"{fahrenheit}°F is equal to {celsius}°C")
        return celsius

      
def main():
    while True:
        temperature = input("Enter the temperature (e.g., 25C or 77F): ")
        try:
            if not temperature:
                continue
                
            unit = temperature[-1].upper()

            if unit not in ('C', 'F'):
                raise TypeError("Invalid unit")
            value = float(temperature[:-1])
            
            if unit == 'C':
                celsius_to_fahrenheit(value)
            elif unit == 'F':
                fahrenheit_to_celsius(value)
                
        except ValueError:
            print("Invalid temperature value. Please enter a valid number for the temperature.\n")
        except TypeError:
            print("Invalid unit. Please enter a temperature followed by 'C' or 'F'\n")
        else:
            break
main()