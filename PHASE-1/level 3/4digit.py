def digit(n):
    first_digit= n//1000
    last_digit= n%10

    if first_digit == last_digit:
        return "first and last digit are equal"

    else:
        return "not equal"

while True:
    n = int(input("Enter a 4-digit number: "))
    print(digit(n))