def find_even_index(arr):
    for i in range(len(arr)):
        print(sum(arr[:i]),"test test",sum(arr[i+1:]), "i= " ,i)
        if sum(arr[:i]) == sum(arr[i+1:]):
            return "end"
    return -1

arr = [1,2,3,4,3,2,1]
find_even_index(arr)
