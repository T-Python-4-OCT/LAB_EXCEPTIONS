def to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    print(" Temperature Converter🌡️ ")
    print(" Enter a temperature like: 25 C or 77 F 💡")
    print(" Type q to quit 🚪")
    print("-" * 40)

    while True:
        user_input = input("📥 Enter temperature: ").strip()

        if user_input.lower() == "q":
            print(" Goodbye!👋 ")
            break

        try:
            value_text, unit = user_input.split()
            value = float(value_text)
            unit = unit.upper()

            if unit == "C":
                converted = to_fahrenheit(value)
                new_unit = "F"

            elif unit == "F":
                converted = to_celsius(value)
                new_unit = "C"

            else:
                raise TypeError(
                    " Invalid unit! Use C for Celsius or F for Fahrenheit.⚠️ "
                )

        except ValueError:
            print(" Invalid temperature! Enter a number followed by C or F.❌ ")

        except TypeError as error:
            print(error)

        else:
            print(f" Converted temperature: {converted:.2f} {new_unit}✅")
            break


main()

