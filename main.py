number = int(input("Enter any number : "))
power = int(input("Enter the power of the number needed : "))

result=1

for i in range(power):

    result: int = result * number


print(f"{number} raised to the power of {power} is: {result}")
