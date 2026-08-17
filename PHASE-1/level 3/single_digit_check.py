def digit_check(n):
    count = 0
    while(n>0):
        last_digit = n%10
        n = n//10
        print(last_digit)
        count= count +1

    if count==1:
        return "single digit"

    elif count==2:
        return "double digit"

    else:
        return "multidigit"

while True:
    n = int(input("Enter a 3-digit number: "))
    print(digit_check(n))