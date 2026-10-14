def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    while True:
        text = input('Enter a temperature and its unit (e.g., "25 C" or "77 F"): ')

        try:
            value, unit = text.split()
            value = float(value)
            unit = unit.upper()
            if unit == "C":
                print(f"Temperature in Fahrenheit: {round(celsius_to_fahrenheit(value), 2)} F")
            elif unit == "F":
                print(f"Temperature in Celsius: {round(fahrenheit_to_celsius(value), 2)} C")
            else:
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

        except ValueError:
            print("Invalid temperature. Enter a number and a unit, e.g. '25 C'.")
        except TypeError as e:
            print(e)

        print()


main()


#MohammedAlnsafi