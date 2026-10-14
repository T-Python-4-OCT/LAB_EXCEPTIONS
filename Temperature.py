
def ftoc(temp):
    celsius = (temp - 32) * 5/9
    return celsius


def ctof(temp):
    fahrenheit = (temp * 9/5) + 32
    return fahrenheit


def main():
    while True:
        try:
            temp = input("Enter Degree of temperature by C or F: ")# take input from user 
            teemp, unit = temp.split() # to take two digit and another letter
            teemp = float(teemp)
            unit = unit.upper()# totake upper case only 

            if unit == "C":
                result = ctof(teemp)
                print(f"The Fahrenheit degree is: {result:.2f} F")

            elif unit == "F":
                result = ftoc(teemp)
                print(f"The Celsius degree is: {result:.2f} C")

            else:
                raise TypeError("Invalid unit. Enter C or F.")

            break

        except ValueError:
            print("Invalid input. Try again, for example: 33 C") 

        except TypeError as e:
            print(e)


main()

