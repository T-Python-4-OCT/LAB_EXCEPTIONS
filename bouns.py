
def celsius_to_fahrenheit(celsius):
    fahranheit=(celsius*9/5)+32
    return fahranheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9.
    return celsius



def main ():
    
    while True:
        tempreter:str=input("Enter the Tempreter and its unit(e.g ,25 C or 77 F ) q to Quit: ")
        if tempreter.strip().lower() == "q":
            print("Goodbye!")
            break
        
        try:
           
            
            vlaue,unit=tempreter.split()
            vlaue=float(vlaue)
            unit=unit.upper()
            
            if unit == "C":
                result=celsius_to_fahrenheit(vlaue)
                unitt="F"
                

            elif unit =="F":
                result= fahrenheit_to_celsius(vlaue)
                unitt="C"
            
                
            else:
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
            
            
        except TypeError as e :
            print(e)
            
        except ValueError:
            print("Invalid temperature value. Enter a number followed by a unit, e.g. '25 C'.")
            
        else:
            print(f" Your result:  {result:.2f} {unitt}")
            break

main()
    
    
    
