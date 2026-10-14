def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        try:
            user_input = input('Enter a temperature and its unit ("25 C" or "77 F"): ')
            parts = user_input.split()
            
            if len(parts) != 2:
                raise ValueError
                
            temp_str, unit = parts
            temp_value = float(temp_str)
            
            unit = unit.upper()
            
            if unit == 'C':
                converted = celsius_to_fahrenheit(temp_value)
                print(f"Temperature in Fahrenheit: {converted:.2f} F")
                break
            elif unit == 'F':
                converted = fahrenheit_to_celsius(temp_value)
                print(f"Temperature in Celsius: {converted:.2f} C")
                break
            else:
                raise TypeError
                
        except ValueError:
            print("Invalid temperature value. Please try again.")
        except TypeError:
            print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()