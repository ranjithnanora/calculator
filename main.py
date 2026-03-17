from Addition.add import add_two_number
from Subtraction.sub import sub_to_numbers

from Multiplication.mul import mul_two_numbers
print("Calculator")
num1=int(input("Enter num One: "))
num2=int(input("Enter num two: "))
operation=input("Enter the operation(+,-,*,/): ")
print(" = "*20)
print(" "*15,"Calculator")
print(" = "*20)
match operation:
    case add if add=="+":
        print("Addition")
        print("\t\t",num1,"+",num2,"=", add_two_number(num1,num2))
    case sub if sub=="-":
        print("subtraction")
        print("\t\t",num1,"-",num2,"=",sub_to_numbers(num1,num2))
    case mul if mul=="*":
        print("Multiplication")
        print("\t\t",num1,"*",num2,"=",mul_two_numbers(num1,num2))
    case div if div=="/":
        print("Division")
    case _:
        print("error: invalid operation")

print(" = "*20)