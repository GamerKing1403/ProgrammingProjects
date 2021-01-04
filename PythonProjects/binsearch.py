def binsearch(ar,key):
    low = 0
    high = len(ar)-1
    while low<= high:
        mid = int((low+high)/2)
        if key == ar[mid]:
            return mid
        elif key < ar[mid]:
            high = mid-1
        else:
            low = mid +1
    else:
        return -999

#__main__

ar = [5,6,7,8,9,10,11,12,13,14]
item = int(input("Enter search item:- "))
res = binsearch(ar,item)
if res>=0:
    print(item,"FOUND at index", res)
else:
    print(item,"Not Found")
