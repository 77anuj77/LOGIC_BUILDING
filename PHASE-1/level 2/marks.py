grade= lambda x: "A" if x>90 else ("B" if x > 80 else ("C" if x > 70 else("D" if x>60 else ("E" if x>50 else "F"))))

while True:
    a=int(input("Enter the a: "))
    # b=int(input("Enter teh b: "))
    # c=int(input("Enter teh c: "))
    print(grade(a))