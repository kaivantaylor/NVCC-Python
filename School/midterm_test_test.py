def triangle_num():
    n = input("Enter integer:")
    n = int(n)

    dict = {}
    dict[1] = 1

    for num in range (2,n+1):
        dict[num] = dict[num-1] + num

    for num in range (1,n+1):
        print("n=",num,"s of n=",dict[num])
    
