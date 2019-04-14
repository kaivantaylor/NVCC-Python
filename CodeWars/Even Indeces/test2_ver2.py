#-------------------------case 1 try adding all and seeing if equals 0-----------------------#
def case1(arr):
    result = 0

    for num in arr:
        result += num

    #print(result)

    if result == 0:
        return True
    else:
        return False

#------------------------------ case 2 using length of both sides----------------------------------------#
def case2(arr):
    length = len(arr)
    for n in range(1,length):
        #print(arr[0:n],"   ", n, arr[n:length])
        
        result1= 0
        result2= 0

        for num1 in arr[0:n]:
            result1 += num1

        for num2 in arr[n:length]:
            result2 += num2
        #print(result1, result2, "\n")

        if result1 == 0:
            #print("result1 ==0", n)
            return n
            
        elif result2 == 0:
            #print("result2 ==0", result2)
            return result2
        else:
            #print("THIS CASE DOESNT WORK")
            return -1
            

#------------------------------ case 3 can find but using even sides-----------------------------------------------#
def case3(arr):
    
    length = len(arr)
    even_length = (length // 2) + 1
    arr2 = arr[::-1]
    
    for x in range(1,even_length):
        #print(arr[0:x],arr2[0:x])

        result3 = 0
        result4 = 0
        
        for variable in arr[0:x]:
            result3 += variable

        for variable2 in arr2[0:x]:
            result4 += variable2

        if result3 == result4:
            answer = x
    try:
        return answer
    except UnboundLocalError:
        return False          
    

#------------------------------ case 4 adding from the left -----------------------------------------------#
def case4(arr):
    length = len(arr)
    for y in range(1,length+1):
        #print(y)
        #print(arr[0:y])

        result5 = 0

        for help in arr[0:y]:
            result5 += help

        #print(result5)

        if result5 == 0:
            return y
    return False
#------------------------------ case 4 adding from the left -----------------------------------------------#
def case5(arr):
    length = len(arr)
    arr2 = arr[::-1]
    for y in range(1,length+1):
        #print(y)
        #print(arr[0:y])

        result5 = 0

        for help in arr2[0:y]:
            result5 += help

        #print(result5)

        if result5 == 0:
            return y
    return False
#----------------------------- M A I N ------------------------------------------------#
def find_even_index(arr):
    a = case1(arr)
    b = case2(arr)
    c = case3(arr)
    d = case4(arr)
    e = case5(arr)

    #print(a,b,c,d,e)

    if a == True:
        return 0
    elif b >= 0:
        return b
    elif c != False:
        return c
    elif d != False:
        return d
    elif e != False:
        return e
    else:
        return -1
