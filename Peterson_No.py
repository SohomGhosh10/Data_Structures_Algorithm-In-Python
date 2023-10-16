def fact(n):
    if(n<=1):
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter a no: "))
s=n
sum=0
while n>0:
    rem=n%10
    sum=sum+fact(rem)
    n=n//10
if sum==s:
    print("Petersion no.")
else:
    print("No, it is not a petersion no")