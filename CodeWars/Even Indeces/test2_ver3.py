def find_even_index(arr):
    sum = 0
    leftsum = 0
    length = len(arr)

    for i in arr:
        sum += i

    for i in range(0,length):
        sum -= arr[i]

        if leftsum == sum:
            return i

        leftsum += arr[i]

    return -1
