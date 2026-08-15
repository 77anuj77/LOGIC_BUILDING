def divisible_by_3_5(n):
    if (n%3 and n%5)==0 and n!=0:
        print("the number is divisible by 3 and 5")

    else:
        print("NOT")

while True:
    n= int(input("Enter the number: "))
    divisible_by_3_5(n)