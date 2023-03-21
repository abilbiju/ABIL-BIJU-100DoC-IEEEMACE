def array_sum():
    inp= input("Enter comma-separated values: ").split(",")
    sum=0
    array=[]
    for i in inp:
        array=array+[int(i),]


    for j in array:
        sum=sum+int(j)
    print("inputed array=",array)
    print("sum of the elements=",sum)

array_sum()
