def foo(i,x=[]):
    x.append(i)
    return x
for i in range(3):
    print(foo(i),end=" ")
