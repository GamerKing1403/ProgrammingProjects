from decimal import *

# noinspection SpellCheckingInspection
getcontext().prec = 2944


def abc(x):
    flag = False
    for i in range(x.index(".") + 1, len(x) - 1):
        b = x[i]
        for j in range(i + 1, len(x) - 1):
            if b == x[j: i + 2*len(b)] and b == x[i + 2*len(b): i + 3*len(b)]:
                flag = True
                break
            else:
                b = b + x[j]
        if flag:
            return len(b)
    return 0


m = 0
p = 0
for k in range(2, 1000):
    y = abc(str(Decimal(1)/Decimal(k)))
    if y > m:
        m = y
        p = k

print(m)
print(p)
print(Decimal(1)/Decimal(p))
