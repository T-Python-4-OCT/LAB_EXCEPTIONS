def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    while True:
        user_input = input('Enter a temperature and its unit (e.g., "25 C" or "77 F"): ')
        try:
            value, unit = user_input.split()

            temperature = float(value)  # raises ValueError if not a number
            unit = unit.upper()

            if unit == "C":
                result = celsius_to_fahrenheit(temperature)
                print(f"Temperature in Fahrenheit: {round(result, 2)} F\n")
            elif unit == "F":
                result = fahrenheit_to_celsius(temperature)
                print(f"Temperature in Celsius: {round(result, 2)} C\n")
            else:
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        except ValueError:
            print("Invalid temperature value. Please enter a number.\n")
        except TypeError as e:
            print(f"{e}\n")


main()
