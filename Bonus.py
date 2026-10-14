
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def main():
    while True:
        try:
            user_input = input("Enter temperature and unit (e.g., 25 C or 77 F): ")

            parts = user_input.split()

            if len(parts) != 2:
                print("Invalid format. Please try again.\n")
                continue

            temperature = float(parts[0])
            unit = parts[1].upper()

            if unit == "C":
                result = celsius_to_fahrenheit(temperature)
                print("Temperature in Fahrenheit:", round(result, 2), "F")
                break

            elif unit == "F":
                result = fahrenheit_to_celsius(temperature)
                print("Temperature in Celsius:", round(result, 2), "C")
                break

            else:
                print("Invalid unit. Use C or F.\n")

        except ValueError:
            print("Invalid input. Please enter a valid temperature.\n")


main()
