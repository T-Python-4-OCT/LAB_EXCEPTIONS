def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        try:
            user_input = input('Enter a temperature and its unit (e.g., "25 C" or "77 F"): ').strip()
            parts = user_input.split()
            
            if len(parts) != 2:
                raise ValueError("Invalid format.")
                
            temp_value = float(parts[0])
            unit = parts[1].upper()
            
            if unit == "C":
                converted = celsius_to_fahrenheit(temp_value)
                print(f"Temperature in Fahrenheit: {converted:.1f} F")
                break
            elif unit == "F":
                converted = fahrenheit_to_celsius(temp_value)
                print(f"Temperature in Celsius: {converted:.2f} C")
                break
            else:
                raise TypeError("Invalid unit.")
                
        except ValueError:
            print("Invalid temperature value. Please try again.")
        except TypeError:
            print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

main()