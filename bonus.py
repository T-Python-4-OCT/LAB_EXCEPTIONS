def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    while True:
        try:
            value, unit = input(
                '\nEnter a temperature and its unit (e.g., "25 C" or "77 F"): '
            ).split()

            temperature = float(value)
            unit = unit.upper()

            if unit == "C":
                result = celsius_to_fahrenheit(temperature)
                print(f"Temperature in Fahrenheit: {result:.2f} F")
            elif unit == "F":
                result = fahrenheit_to_celsius(temperature)
                print(f"Temperature in Celsius: {result:.2f} C")
            else:
                raise TypeError

        except ValueError:
            print("Invalid input. Enter a number and unit, like 25 C.")
        except TypeError:
            print("Invalid unit. Please use C or F.")
        else:
            break


main()