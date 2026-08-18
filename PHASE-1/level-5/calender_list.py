from typing import List

def check_date(month: int, day: int) -> str:

    days = [31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]

    if 1 <= month <= 12 and 1 <= day <= days[month - 1]:
        print("Valid Date")

    else:
         print("invalid Date")


while True:
        m= int(input("Enter the month: "))
        d= int(input("Enter the day: "))
        check_date(m,d)
