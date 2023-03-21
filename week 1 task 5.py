def square_sum():

    add=0
    arr = input("Enter comma-separated integers: ").split(",")

    array=[]
    for i in arr:
        array=array+[int(i),]

    sq=[]
    for j in array:
        sq=sq+[j**2,]

    for k in sq:
        add=add+k

    
    print("sum of the squares is : ",add)


square_sum()
