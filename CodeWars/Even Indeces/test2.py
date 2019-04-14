#def find_even_index(arr):
arr = [1,2,3,4,5,6]

max_length = len(arr)//2
#print(max_length)

arr1 = arr
arr2 = arr[::-1]

sum1 = 0
sum2 = 0

counter = 0

while counter <= max_length:
    
    if sum1 == sum2:
        sum1 += arr1[counter]
        sum2 += arr2[counter]
        print("sum1 ",sum1,"sum2 ",sum2,"counter ", counter)

        counter_final = counter 
        counter += 1
    else:
        break

if (counter_final == 0) and sum1 != sum2:
    print(0)
elif counter_final == 0:
    print(-1)

else:
    print(counter_final)

