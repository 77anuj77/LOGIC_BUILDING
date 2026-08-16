number = [i for i in range(1, 11)]
print(number)
print("\n")

even = [i for i in range(1,51) if i%2==0 and i!=0]
print("Even number till 50: ", even)
print("\n")

squares= [i*i for i in range (1,11)]
print(squares, "\n")

'''
⚠️ Notice the difference:

Only if:

[i for i in range(10) if i % 2 == 0]

if-else:

["Even" if i % 2 == 0 else "Odd" for i in range(10)]
'''

