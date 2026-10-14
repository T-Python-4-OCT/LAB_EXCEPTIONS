def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    while True:
        text = input('\nEnter a temperature and its unit (e.g., "25 C" or "77 F") '
                     "[q to quit]: ").strip()

        if text.lower() == "q":
            print("Goodbye!")
            break

        try:
            value, unit = text.split()
            temperature = float(value)

            unit = unit.upper()
            if unit != "C" and unit != "F":
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

        except ValueError:
            print("Invalid temperature value. Please enter a number then a unit (e.g., 25 C).")
        except TypeError as e:
            print(e)
        else:
            if unit == "C":
                result = celsius_to_fahrenheit(temperature)
                print(f"Temperature in Fahrenheit: {round(result, 2)} F")
            else:
                result = fahrenheit_to_celsius(temperature)
                print(f"Temperature in Celsius: {round(result, 2)} C")


main()