words = ["Zero", "One", "Two", "Three", "Four",
         "Five", "Six", "Seven", "Eight", "Nine"]

n = int(input("Enter a digit (0-9): "))

if 0 <= n <= 9:
    print(words[n])
else:
    print("Invalid digit")