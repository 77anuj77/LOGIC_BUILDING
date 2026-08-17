check = lambda n: "Can be divided" if n % 2000 == 0 else "Cannot be divided"

n = int(input("Enter amount: "))
print(check(n))