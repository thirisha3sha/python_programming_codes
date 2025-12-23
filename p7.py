class find_diff:
  @classmethod
  def find(cls,n,m):
    divisors=[]
    non_divisors=[]
    for i in range(1,m+1):
      if i%n==0:
        divisors.append(i)
      else:
        non_divisors.append(i)
    return sum(divisors)-sum(non_divisors)
n=int(input())
m=int(input())
diff=find_diff().find(n,m)
print(abs(diff))
