
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    while True:
        try:
            user_input = input(
                "Enter temperature and unit (e.g. 25 C): "
            )

            temperature, unit = user_input.split()

            temperature = float(temperature)
            unit = unit.upper()

            if unit == "C":
                result = celsius_to_fahrenheit(temperature)
                print(f"Temperature in Fahrenheit: {result:.2f} F")

            elif unit == "F":
                result = fahrenheit_to_celsius(temperature)
                print(f"Temperature in Celsius: {result:.2f} C")

            else:
                raise ValueError("Invalid unit! Use C or F.")

        except ValueError as error:
            print(f"Error: {error}")

        else:
            print("Conversion successful!")
            break


if __name__ == "__main__":
    main()
