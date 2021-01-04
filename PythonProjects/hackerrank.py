height,width = input().split(" ")
height = int(height)
width = int(width)
c = ".|."
for i in range(int((height-1)/2)): 
    print((c).rjust(6,"-"))
