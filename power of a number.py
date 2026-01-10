
number = int(input("Enter the  number: "))
multiplying = int(input("How many times should we multiply it? "))

result = 1


for i in range(multiplying):
    result = result * number

print(f"The answer is: {result}")
