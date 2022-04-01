#fibonnaci series

n=int(input("enter upto to how many terms:"))

l1=0
l2=1
count=0

if n<=0:
    print("enter a number more then zero")
elif n==1:
    print("fibonacci series is:")
    print(l1)
else:
    print("fibonacci series:")
    while count<n:
        print(l1)
        n3=l1+l2
        l1=l2
        l2=n3
        count+=1
    
