
# a = n // 100        # first digit
# b = (n // 10) % 10  # second digit
# c = n % 10          # last digit

check = lambda n: "All distinct" if (n // 100) != ((n // 10) % 10) and ((n // 10) % 10) != (n % 10) and (n // 100) != (n % 10) else "Digits are not distinct"

while True:
    n = int(input("Enter a 3-digit number: "))
    print(check(n))