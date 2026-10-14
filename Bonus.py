def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def get_temperature():

    while True:

        try:
            user_input = input("Enter temperature and unit, for example 25 C: ")

            temperature, unit = user_input.split()

            temperature = float(temperature)

            if unit == "C":
                result = celsius_to_fahrenheit(temperature)
                print("Temperature in Fahrenheit:", round(result, 2) , "F")
                break

            elif unit == "F":
                result = fahrenheit_to_celsius(temperature)
                print("Temperature in Celsius:", round(result , 2), "C")
                break

            else:
                raise TypeError

        except ValueError:
            print("Invalid temperature. Please try again.")

        except TypeError:
            print("Invalid unit. Please use C for Celsius or F for Fahrenheit.")

        except Exception as e:
            print("An error occurred:", e)

        finally:
            print("Thank you for using the temperature converter.")    


get_temperature()
