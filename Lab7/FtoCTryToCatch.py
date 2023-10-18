try:
    fahrenheit = float(input("Please enter degrees in Fahrenheit: "))
    celsius = (5.0/9.0) * (fahrenheit - 32)
    print(f"{fahrenheit} degrees Fahrenheit is {celsius:.2f} degrees Celsius")
except ValueError as ex:
    print(f"Your input is not valid: {ex}")
finally:
    print("Finally")

print("Good Bye")
