eve_odd= lambda a,b: "Both even" if a%2==0 and b%2==0 else("Both Odd" if a%2!=0 and b%2!=0 else "One is odd and one is even")

while True:
    a=int(input("Enter the a: "))
    b=int(input("Enter teh b: "))
    # c=int(input("Enter teh c: "))
    print(eve_odd(a,b))