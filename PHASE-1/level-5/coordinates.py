# check= lambda x,y : "(x,y) lies on x-axis" if y==0 and x!= 0 else("(x,y) lies on y-axis" if x==0 and y!=0 else ("(x,y) lies at origin" if x==0 and y==0 else "Lies on cartisean plain"))
from pydantic import BaseModel, ValidationError
from typing import Optional, List, Dict, Literal


import pandas as pd
class coordinate(BaseModel):
    x: int
    y: int

def check(coordinate : coordinate) -> None:
    if coordinate[0] == 0 and coordinate[1] == 0:
        print("It is on the origin")
    elif coordinate[0] == 0 and coordinate[1] != 0:
        print("It is on the Y-Axis")
    elif coordinate[1] == 0 and coordinate[0] != 0:
        print("It is on the X-Axis")
    else:
        print("It does not lie on origin or any of the axes")



while True:
    try:
        a= float(input("Enter the a: "))
        b= float(input("Enter the b: "))
        check((a,b))
    except ValueError as e:
        print("error :", e)

