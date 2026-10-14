def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    while True:
        try:
            user_input = input(
                'Enter a temperature and its unit (e.g., "25 C" or "77 F"): '
            )

            temperature, unit = user_input.split()
            temperature = float(temperature)
            unit = unit.upper()

            if unit == "C":
                result = celsius_to_fahrenheit(temperature)
                print(f"Temperature in Fahrenheit: {result} F")
            elif unit == "F":
                result = fahrenheit_to_celsius(temperature)
                print(f"Temperature in Celsius: {round(result, 2)} C")
            else:
                raise TypeError("Invalid unit")

            break

        except ValueError:
            print("Invalid temperature. Please enter a valid number and unit.")
        except TypeError:
            print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")


main()
