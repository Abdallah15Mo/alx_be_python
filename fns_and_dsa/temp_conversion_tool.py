# temp_conversion_tool.py

# Global conversion factors (no spaces around "/")
FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

def convert_to_celsius(fahrenheit):
    # Use global conversion factor to convert Fahrenheit to Celsius
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    # Use global conversion factor to convert Celsius to Fahrenheit
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temp_input = input("Enter the temperature to convert: ").strip()
    scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    try:
        temp_value = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    if scale == 'C':
        converted = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {converted}°F")
    elif scale == 'F':
        converted = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {converted}°C")
    else:
        raise ValueError("Invalid temperature scale. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()
