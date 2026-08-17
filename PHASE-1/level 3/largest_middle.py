def middle(n):
    first_digit= n//100
    middle_digit= (n//10)%10
    last_digit= n%10

    if middle_digit> last_digit and middle_digit> first_digit:
        return "middle is the greatest"
    elif middle_digit< last_digit and middle_digit< first_digit:
        return "middle is the smallest"

    else:
        print("Neither")


check = lambda n: "Middle Digit is Greatest" if ((n // 10) % 10)> n//100 and ((n // 10) % 10) > (n % 10) else ("Middle is Smallest" if (n//10)%10 < n//10 and (n//10)%10 < n%10 else "Neither")

while True:
    n = int(input("Enter a 3-digit number: "))
    print(middle(n))
    print(check(n))