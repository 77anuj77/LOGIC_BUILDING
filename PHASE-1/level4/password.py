password_check= lambda p: len(p)>8 and any(ch.isdigit() for ch in p) 

while True:
    password= input("Enter the Password: ")
    password_check(password)
    print("Valid password" if password_check(password) else "Enter a valid Password")

    