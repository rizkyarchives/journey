# from art import logo
# from replit import clear

def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  return num1 / num2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
  
# print(logo)
print("Welcome to pyCalculator.")
running = True
number1 = float(input("First number: "))
while running:
  for key in operations:
    print(key)
  operationChosen = input("Choose one of these four operations above: ")
  number2 = float(input("Second number: "))
  result = operations[operationChosen](number1, number2)
  print(f"{number1} {operationChosen} {number2} = {result}")
  continuing = input(f"'y' to continue calculating with {result}, 'n' to start a new calculation, 'e' to exit the calculator: ")
  if continuing == 'y':
    number1 = result
  elif continuing == 'n':
    # clear()
    number1 = float(input("First number: "))
  elif continuing == 'e':
    print("BYE")
    running = False