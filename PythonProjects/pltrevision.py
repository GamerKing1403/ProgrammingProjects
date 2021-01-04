import numpy as np
import matplotlib.pyplot as plt
col = [8000, 12000, 9800, 11200, 15500, 7300]
x = np.arange(6)
plt.title("Volunteering Week Collection")
plt.bar(x,col,color='r',width=0.25)

plt.bar(x, col, color='olive', width=0.25)
plt.xticks(x,['Mon','Tue','Wed','Thu','Fri','Sat'])
plt.xlabel('Days')
plt.ylabel('Collections')

plt.bar(x,col,color='g',width=0.25)
plt.xticks(x,['A','B','C','D','E','F'])
plt.xlabel("Sections")
plt.ylabel("Collection")
plt.show()
