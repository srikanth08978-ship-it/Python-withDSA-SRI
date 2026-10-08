def calprefix(a):
  sum=a[0]
  res=[0 for _ in range(len(a))]
  res[0]=sum
  for i in range(1,len(a)):
    sum+=a[i]
    res[i]=sum
  return res

def rangesum(a,st,en):
  s=0
  for i in range(st,en+1):
    s+=a[i]
  return s 
def rangesum(a,st,en):
  return prefix[en]-prefix[st-1] 


def sumArray(a,k,tar):
    s=0
    for i in range(k):
      s+=a[i]
    if(s==tar):
      return[a[0],a[1],a[2]]

    for i in range(k,len(a)):
      s=s+a[i]-a[i-k]
      if(s==tar):
        return [a[i-k+1],a[i-1],a[i]]

    return[-1,-1]


a=[1,2,3,4,5,6,7,8,9]
prefix=calprefix(a)
print(prefix)    
print(rangesum(a,3,8))
print(rangesum(a,3,8))
print(sumArray(a,3,21))


   
def equilibriumindex(arr):
    total_sum = sum(arr)
    left_sum = 0
    
    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]
        
        if left_sum == right_sum:
            return i
        
        left_sum += arr[i]

    return -1

a= [-7, 1, 5, 2, -4, 3, 0]
   
