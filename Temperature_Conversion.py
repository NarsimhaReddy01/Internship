def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return fahrenheit_to_celsius(fahrenheit) + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def convert_temperature(value, unit):
    if unit == "C":
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        return fahrenheit, kelvin
    
    elif unit == "F":
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        return celsius, kelvin
    
    elif unit == "K":
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        return celsius, fahrenheit
    
    else:
        return None, None
    

def main():
    print("Temperature Conversion")
    value = float(input("Enter the temperature value: "))
    unit = input("Enter the temperature unit (C, F, or K): ").upper()

    converted1, converted2 = convert_temperature(value, unit)

    if unit == "C":
        print(f"{value}°C is equal to {converted1:.2f}°F and {converted2:.2f}K")
    elif unit == 'F':
        print(f"{value}°F is equal to {converted1:.2f}°C and {converted2:.2f}K")
    elif unit == "K":
        print(f"{value}K is equal to {converted1:.2f}°C and {converted2:.2f}°F")
    else:
        print("Invalid unit of measurement. Please enter C, F, or K.")

if __name__ == "__main__":
    main()
