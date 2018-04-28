array = [1,2,3,4,5,6,7,8,9,10]

x = 4



def binarysearch(array,l,r,x):
    if r>=l:
        middle = l + (r-l)//2


        if array[middle] == x:
            return middle


        elif array[middle] > x:
            return binarysearch(array,l,middle-1,x)

        else:
            return binarysearch(array,middle+1,r,x)
    else:
        return -1

result = binarysearch(array,0,len(array)-1,x)

if result != -1:
    print("Element is present at index {}." .format(result))
else:
    print("Number not in the array")