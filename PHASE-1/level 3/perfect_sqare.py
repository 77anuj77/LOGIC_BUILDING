check= lambda n: any(i * i == n for i in range(1, n//2 +1))

while True:
    n = int(input("Enter a number: "))
    print("Perfect square" if check(n) else "Not a perfect square")
