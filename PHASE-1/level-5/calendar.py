from typing import Dict
from pydantic import ValidationError
import pandas

def check_day_month(date : Dict[int ,int])-> str:
        print(date.items())
        days = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
        # for mon, day in date.items():
        #         if mon in days and 1<=day<= days[mon]:
        #                 print("it is a valid Date")
        #         else :
        #                 print("Not")

        check_date = lambda date: all(mon in days and 1 <= day <= days[mon] for mon, day in date.items())

        print("Date" if check_date(date) else "Not a Date")

while True:
        m= int(input("Enter the month: "))
        d= int(input("Enter the day: "))
        check_day_month({m:d})

   

'''
If you want the for inside the lambda, use all():

check_date = lambda date: (
    "it is a valid Date"
    if all(mon in days and 1 <= day <= days[mon]
           for mon, day in date.items())
    else "not"
)
Why?

The for part:

for mon, day in date.items()

is a generator expression. It needs something like all() or any() to consume it.

Your condition:

mon in days and 1 <= day <= days[mon]

is evaluated for each (mon, day).

So conceptually:

all(
    condition
    for mon, day in date.items()
)

means:

Check the condition for every month/day pair, and return True only if all are valid.

Complete example
'''