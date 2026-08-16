alphabet_check= lambda n: "between a and m" if 97 <= ord(n) <= 109 else "between n and z"

while True:
    n=input("Enter the n: ")
    # b=int(input("Enter teh b: "))
    # c=int(input("Enter teh c: "))
    print(alphabet_check(n))
    
# a='a'
# print(ord(a))
# b='m'
# print(ord(b))
# x='n'
# print(ord(x))
# y='z'
# print(ord(y))