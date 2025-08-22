#CALCULATOR
def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")
    print("5. MODULUS")
          
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    choice = input("Enter the operation(1/2/3/4/5):")

    if choice == '1':
       result = num1 + num2
       operation = "+"
    elif choice == '2':
         result = num1 - num2
         operation = "-"
    elif choice == '3':
         result = num1 * num2
         operation = "*"
    elif choice == '4':
      if num2!= 0:
         result = num1 / num2
         operation = "/"
      else:
         print("Error: Dividion by zero not allowed.")
         return
    elif choice == '5':
        result = num1 % num2
        operation = "%"
    else:
         print("Invalid input")
         return

    print(f"{num1} {operation} {num2} = {result}")
calculator()

