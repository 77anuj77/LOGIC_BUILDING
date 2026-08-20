from typing import List
import numpy as np

def pythagoras_check(numbers : List[float])-> str:
    
    check= lambda numbers: pow(numbers[0], 2) + pow(numbers[1], 2) == pow(numbers[2], 2) or pow(numbers[1], 2) + pow(numbers[2], 2) == pow(numbers[0], 2) or pow(numbers[0], 2) + pow(numbers[2], 2) == pow(numbers[1], 2)
    print("Can form Pythagoras triplet" if check(numbers) else "No")

def check(triplet: np.array) -> bool:
    triplet_sq = triplet ** 2 
    return triplet_sq.sum() / 2 == triplet_sq[np.argmax(triplet_sq)]

while True:
    a= int(input("Enter the lenght of a: "))
    b= int(input("Enter hte length of b: "))
    c= int(input("Enter hte length of c: "))

    print("It is a triplet" if check(np.array([a,b,c])) else "It is not a triplet")


