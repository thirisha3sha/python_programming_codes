def pin(n1,n2,n3,n4):
    small_n1=min(int(i) for i in str(n1))
    large_n2=max(int(i) for i in str(n2))
    small_n3=min(int(i) for i in str(n3))
    guess_pin=(small_n1*large_n2*small_n3)-n4
    return guess_pin                 
n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())
result=pin(n1,n2,n3,n4)
print(result)

