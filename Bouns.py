user = input("Enter the temperature(25C or 77F): ")

def fahrenheit_to_celsius(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)
        result = (fahrenheit - 32) * 5 / 9
        print(result, "C")

    except ValueError:
        print("Please enter a valid number")


def celsius_to_fahrenheit(celsius):
    try:
        celsius = float(celsius)
        result = (celsius * 9 / 5) + 32
        print(result, "F")
    except ValueError:
        print("Please enter a valid number")

if user[-1].upper() == "F":
    fahrenheit_to_celsius(user[:-1])

elif user[-1].upper() == "C":
    celsius_to_fahrenheit(user[:-1])

else:
    print("Please enter C or F")