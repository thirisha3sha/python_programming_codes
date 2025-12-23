def sub_array_sum(arr,k):
    max_sum=0
    windows_sum=sum(arr[:k])
    max_sum=windows_sum
    for i in range(len(arr)-k):
        windows_sum=windows_sum-arr[i]+arr[i+k]
        max_sum=max(max_sum,windows_sum)
    return max_sum
arr=[2,1,5,1,3,2]
k=3
result=sub_array_sum(arr,k)
print(result)
