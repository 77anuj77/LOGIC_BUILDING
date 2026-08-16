check= lambda a,b,c: "Traingle" if a<b+c and b< c+a and c< a+b else "Not a triangle"

while True:
    a=int(input("Enter the a: "))
    b=int(input("Enter teh b: "))
    c=int(input("Enter teh c: "))
    print(check(a,b,c))