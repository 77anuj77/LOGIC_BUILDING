check= lambda ch: "upper case" if ch.isupper() else ("lower case" if ch.islower() else ( "Digit" if ch.isdigit() else "special charecter"))

ch = input("Enter a character: ")
print(check(ch))