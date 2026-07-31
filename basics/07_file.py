for i in range(10):
    if i==7:
        break
    print(i)

for i in range(10):
    if i==5:
        continue 
    print(i) 

for i in range(20):
    if i%2==0:
        continue
    print(i)

for i in range(10):
    a=int(input("Enter a number:"))
    if a==0:
        break