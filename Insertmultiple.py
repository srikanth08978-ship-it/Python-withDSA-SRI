def add(a,b):
    for i in b:
        a=apnd(a,i)
    print(a)



def  apnd(a,e1):
    ar=[0 for i in range(len(a)+1)] 
    for i in range(len(a)):
        ar[i]=a[i]
    ar[-1]=e1
    return ar




n=int(input())
a=list(map(int,input().split(' ')))[:n]

m=int(input())
b=list(map(int,input().split(' ')))[:m]

add(a,b) 
