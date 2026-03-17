from Subtraction.sub import sub_to_numbers
print("Calculator")
num1=int(input("Enter num One: "))
num2=int(input("Enter num two: "))
operation=input("Enter the operation(+,-,*,/): ")

match operation:
    case add if add=="+":
        print("Addition")
    case sub if sub=="-":
        print("subtraction")
        print(num1,"-",num2,"=",sub_to_numbers(num1,num2))
    case mul if mul=="*":
        print("Multiplication")
    case div if div=="/":
        print("Division")
    case _:
        print("error: invalid operation")