from Multiplication.mul import mul_two_numbers
print("Calculator")
num1=int(input("Enter num One: "))
num2=int(input("Enter num two: "))
operation=input("Enter the operation(+,-,*,/): ")

match operation:
    case add if add=="+":
        print("Addition")
    case sub if sub=="-":
        print("subtraction")
    case mul if mul=="*":
        print("Multiplication")
        print(num1,"*",num2,"=",mul_two_numbers(num1,num2))
    case div if div=="/":
        print("Division")
    case _:
        print("error: invalid operation")