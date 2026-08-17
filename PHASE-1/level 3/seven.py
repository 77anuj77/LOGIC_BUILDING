check= lambda n: "Divisible by 7" if n%7==0 and n!=0 else("Ends with 7" if n%10==7 else "Neither")

while True:
    n = int(input("Enter a 3-digit number: "))
    print(check(n))