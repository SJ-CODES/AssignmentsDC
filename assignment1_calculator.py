

def Calculator():
    first_number = float(input( "Enter your first number: "))
    operator = input( "Enter your operand type: ")
    second_number = float(input( "Enter your second number: "))
    print(f"what is your equation {first_number} {operator} {second_number} ")
    
    if operator == "+":
        print(f"{first_number} {operator} {second_number} ")
        print(first_number + second_number)

    if operator == "-":
        print(f"{first_number} {operator} {second_number} ")
        print(first_number - second_number)
    if operator == "/":
        print(f"{first_number} {operator} {second_number} ")
        print(first_number / second_number)
    if operator == "*":
       print(f"{first_number} {operator} {second_number} ")
       print(first_number * second_number)

Calculator()


