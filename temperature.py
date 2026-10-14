def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def parse_input(text):
    parts = text.split()
    if len(parts) != 2:
        raise ValueError('Invalid input. Enter a number and a unit, e.g. "25 C".')

    value_text, unit = parts
    try:
        value = float(value_text)
    except ValueError:
        raise ValueError("Invalid temperature value. Please enter a number.")
    if value != value or value in (float("inf"), float("-inf")):
        raise ValueError("Invalid temperature value. Please enter a number.")

    unit = unit.upper()
    if unit not in ("C", "F"):
        raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

    return value, unit


def main():
    while True:
        text = input('Enter a temperature and its unit (e.g., "25 C" or "77 F") or "exit" to quit: ').strip()
        if text.lower() == "exit":
            print("Goodbye!")
            break

        try:
            value, unit = parse_input(text)
        except ValueError as error:
            print(error)
        except TypeError as error:
            print(error)
        else:
            if unit == "C":
                print("Temperature in Fahrenheit:", round(celsius_to_fahrenheit(value), 2), "F")
            else:
                print("Temperature in Celsius:", round(fahrenheit_to_celsius(value), 2), "C")
            break
        print()


main()