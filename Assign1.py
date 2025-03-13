num1=5
num2=10

operation=input("(+, -, *, **, /):")

operation == '+'
result = num1 + num2 
print(f"{num1} + {num2} = {result}")

operation == '-'
result = num2 - num1 
print(f"{num2} - {num1} = {result}")

operation == '*'
result = num1 * num2 
print(f"{num1} * {num2} = {result}")

operation == '**'
result = num2 ** num1
print(f"{num2} ** {num1} = {result}")

operation == '/'
result = num2 / num1 
print(f"{num2} / {num1} = {result}")
