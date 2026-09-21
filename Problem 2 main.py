N = int(input("Enter a nmuber:"))
sum = 0
count = 0 
for i in range(1,N+1):
    if i%2==0 and i%4!=0:
        count = count +1
        sum = sum +i
        print("Total of sorted numbers sum","+",i,"=",sum)
print("Count",count,"numbers")
