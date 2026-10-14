# Bonus

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius



def temperature_convertert():
    try:
        temperature_input = input('Enter a temperature and its unit (e.g., "25 C" or "77 F"): ')
        
        temperature, unit = temperature_input.split()
        temperature = float(temperature)
        unit = unit.upper()

        if unit == "C":
            result = celsius_to_fahrenheit(temperature)
            print(f"Temperature in Fahrenheit:{result:.2f} F")

        elif unit == "F":
            result = fahrenheit_to_celsius(temperature)
            print(f"Temperature in Celsius:{result:.2f} C")

        else:
            raise TypeError("Invalid unit")
                  


    except ValueError:
       print("Invalid temperature. Please try again.")
       temperature_convertert()

    except TypeError:
       print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
       temperature_convertert()



temperature_convertert()