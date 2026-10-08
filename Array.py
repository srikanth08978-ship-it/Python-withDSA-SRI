def linearsearch(a,e1):
  for i in range(len(a)):
    if a[i]==e1:
      print(i)
      return
print('no element found')
def occurence(a,e1):
  ar=[]
  for i in range(len(a)):
    if a[i]==e1:
      ar.append(i)
  if len(ar)>0:
    print(ar)
  else:
    print('element not found')
def maxsubArray(a,k):
  sum=0
  for i in range(k):
    sum+=a[i]
  max=sum
  for i in range(k,len(a)):
    sum=sum+a[i]-a[i-k]
    if(sum>max):
     max=sum
  print(max)
      

    
def minsubArray(a,k):
  sum=0
  for i in range(k):
    sum+=a[i]
  min=sum
  for i in range(k,len(a)):
    sum=sum+a[i]-a[i-k]
    if(sum<min):
     min=sum
  print(min)



a=[1,2,3,4,5,2,3,2]
e1=2
linearsearch(a,e1)
occurence(a,e1)
k=3
maxsubArray(a, k)
minsubArray(a,k)



def subarrays(a):
  for i in range(len(a)):
    for j in range(i+1,len(a)):
      print(f'[{a[i]},{a[j]}]')



print(a)

subarrays(a)


def sumpair(a,e1):
  l=0
  r=len(a)-1
  for i in range(len(a)//2):
    if a[l]+a[r]==e1:
      print(i,r)
    l+=1
    r+=1
def is_palindrome(a,e1):
  l=0
  r=len(s)-1
  while l<r:
    if s[i]!=s[r]:
      return False
    l+=1
    r+=1
  return True
  print(is_palindrome("madam"))

a=[12,7,18,9,21,16]
target=28
sumpair(a,target)

is_palindrome(a,e1)
 
