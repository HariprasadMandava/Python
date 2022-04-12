Number=int(input("Enter number: "))
a=0
for i in range(2,Number//2+1):
    if(Number%i==0):
        a=a+1
if(a<=0):
    print("Number is prime")
else:
    print("Number isn't prime")