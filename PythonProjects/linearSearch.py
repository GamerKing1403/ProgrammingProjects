ar = [13,14,25,54,43,32,3,7,8]
key = int(input("Enter the search Number"))
found = False
for i,j in enumerate(ar):
    if j == key:
        found = True
        break
    else:
        continue
if found:
    print(key,"FOUND at index",i)
else:
    print(key,"Not Found")
