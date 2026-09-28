# Online Python compiler (interpreter)
# Write and run Python online using this editor.



n = int(input("enter a num: "))
A = len(str(n))
print("Even Digits=")
v = 0

for i in range(A+1):
    G = n%10
    n = n//10
    

    if G%2==0 and G!=0:
        print(G, end=" ")
        v = v+G
print("Total sum of Even Digits=", v)
    
    
        
