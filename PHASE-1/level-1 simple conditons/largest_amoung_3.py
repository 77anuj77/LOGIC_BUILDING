def largest_amoung_3(a, b, c):
    greatest=lambda a, b, c: a if a>b and a>c else (b if b>c else c)
    print("%d ", greatest(a,b,c))

while True:
    a=int (input ("Enter the a:"))
    b=int (input ("Enter the b:"))
    c=int (input ("Enter the c:"))

    largest_amoung_3(a,b,c)