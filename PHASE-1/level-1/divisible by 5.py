def divisible_by_5(n):
    if n%5==0:
        if n==0:
            print("the number is zero")
        else:
            print("the number is divisible by 5")

    else:
        print("the number is not divisible by 5")

while True:
    n=int(input("Enter the number:"))
    divisible_by_5(n)
    
    if n==99:
        break