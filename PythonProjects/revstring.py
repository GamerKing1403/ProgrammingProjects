string = input("Enter the string to reverse")
res = ''
for i in range(len(string)-1,-1,-1):
    res += string[i:i+1]
print(res)
