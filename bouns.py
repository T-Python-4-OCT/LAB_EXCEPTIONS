def celsius_to_fahrenheit(celsius):
    return round((celsius * 9 / 5) + 32, 2)

def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5 / 9, 2)

def main():
    while True:
        Question = input('Enter a temperature and its unit (e.g., "25 C" or "77 F"): ')
        try:
            value, unit = Question.split()
            temperature = float(value)
            unit = unit.upper()

            if unit == "C":
                print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(temperature)} F")
            elif unit == "F":
                print(f"Temperature in Celsius: {fahrenheit_to_celsius(temperature)} C")
            else:
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
            break

        except ValueError:
            print("Invalid temperature value. Example: 25 C or 100 F")
        except TypeError as error:
            print(error)
        print()
main()