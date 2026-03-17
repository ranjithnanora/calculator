def div_two_numbers(num1: int, num2: int)->float|None:
    """
    This function divides two numbers
    :param num1:
    :param num2:
    :return: num1/num2 | None if num2==0
    """
    if num2==0:
        print("Divisor cant be Zero")
        return None
    return num1/num2