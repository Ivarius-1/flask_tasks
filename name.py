def sum_array(arr):
    if not arr:
        return 0
    return arr[0] + sum_array(arr[1:])

array = [-1,0,7,10,-5]
result = sum_array(array)
print(result)
