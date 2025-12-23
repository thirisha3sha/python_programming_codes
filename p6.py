class find_diff:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def find(self):
        divisors = []
        non_divisors = []
        for i in range(1, self.m + 1):
            if i % self.n == 0:
                divisors.append(i)
            else:
                non_divisors.append(i)
        return divisors, non_divisors
n = int(input())
m = int(input())
a,b= find_diff(n, m).find()
a=sum(a)
b=sum(b)
diff=a-b
print(abs(diff))

