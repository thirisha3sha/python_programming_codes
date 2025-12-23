""" Write a program to print all the Non-Prime numbers between A and B?
Sample Input: A = 12 B = 19
Sample Output:
14, 15, 16, 18

Definition:
 A prime number is a natural number greater than 1 that has exactly two distinct positive divisors —
👉 1 and the number itself.
 example: 2,3,5,7,11,17
  """
a = int(input())
b = int(input())
for x in range (a,b+1):
    if x > 1:
        for i in range (2, x):
            if (x%i)== 0:
                break
        else:
            print (x)
