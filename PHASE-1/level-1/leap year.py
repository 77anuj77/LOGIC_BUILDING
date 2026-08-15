def leap_year(n):
    if n%400==0 or (n%100 != 0 and n%4==0):
        print("this is leap year")

    else :
        print("this is not a leap year")

while True:
    n=int(input("Enter the number:"))
    leap_year(n)
    
    if n==99:
        break

