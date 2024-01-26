a= int(input("enter a num"))
c=0
for i in range(1, a+1):
    if(a%i==0):
        c=c+1
if c==2:
    print("prime num")
else:
    print("not prime num")        
