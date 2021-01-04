import matplotlib.pyplot as pl
import numpy as np

# x = np.linspace(1,5,6)
# y = np.log(x)
# pl.plot(x,y)
# pl.show()


# a = [1,2,3,4]
# b = [2,4,6,8]
# c = [1,4,9,16]
# pl.plot(a,b)
# pl.show()


# x = np.arange(0,10,0.1)
# a = np.cos(x)
# b = np.sin(x)
# pl.plot(x,a,'y')
# pl.plot(x,b,'g')
# pl.show()

# a = np.arange(1,20,1.25)
# b = np.log(a)
# pl.plot(a,b,'bd')
# c = np.cos(a)
# pl.plot(a,c,'ro')
# pl.show()


# a,b,c = [1,2,3,4],[2,4,6,8],[1,4,9,16]
# pl.bar(a,b)
# pl.xlabel("Values")
# pl.ylabel('Doubles')
# pl.show()
# pl.xlabel("Values")
# pl.ylabel('Squares')
# pl.bar(a,c)
# pl.show()

# cities = ['Delhi','Mumbai','Banglore','Hyderabad']
# population = [23456123,20083104,18456123,13411093]
# pl.bar(cities,population,color = 'red')
# pl.xlabel("Cities")
# pl.ylabel("Population")
# pl.show()

# Val = [[5.,25.,45.,20.],[4.,23.,49.,17.],[6.,22.,47.,19.]]
# x = np.arange(4)
# pl.bar(x+0.00,Val[0],color='b',width=0.25)
# pl.bar(x+0.25,Val[1],color='g',width=0.25)
# pl.bar(x+0.50,Val[2],color='r',width=0.25)
# pl.show()

# cities = ['Delhi','Mumbai','Banglore','Hyderabad']
# population = [23456123,20083104,18456123,13411093]
# pl.barh(cities,population,color = 'red')
# pl.ylabel("Cities")
# pl.xlabel("Population")
# pl.show()

# contri = [17,8.8,12.75,14]
# houses = ['Vidya','Kshama','Namrta','Karuna']
# pl.pie(contri,labels = houses)
# pl.show()

# x = np.arange(4)
# y = [5.,25.,45.,20.]
# pl.xlim(-2.0,4.0)
# pl.bar(x,y)
# pl.title("Simple Bar Chart")
# pl.show()

# x = np.arange(4)
# y = [5.,25.,45.,20.]
# pl.xlim(-4.0,1.0)
# pl.bar(x,y)
# pl.title("Simple Bar Chart")
# pl.show()

# col = [8000,12000,9800,11200,15500,7300]
# x = np.arange(6)
# pl.title("Volunteering Week Collection")

# # a
# pl.bar(x,col,color='r',width=0.25)
# pl.show()

# # b
# pl.bar(x,col,color='olive',width=0.25)
# pl.xticks(x,['Mon','Tue','Wed','Thu','Fri','Sat'])
# pl.xlabel("Days")
# pl.ylabel("Collection")
# pl.show()

# # c
# pl.bar(x,col,color='g',width=0.25)
# pl.xticks(x,['A','B','C','D','E','F'])
# pl.xlabel("Sections")
# pl.ylabel("Collection")
# pl.show()

# data = [[5., 25., 45., 20.], [8., 13., 29., 27.],[9.,29.,27.,39.]]
# x = np.arange(4)
# pl.plot(x, data[0], color='b',label='range1')
# pl.plot(x, data[1], color='g',label='range2')
# pl.plot(x, data[2], color='r',label='range3')
# pl.legend(loc='upper left')
# pl.title("Multi Range Line Chart")
# pl.xlabel("X")
# pl.ylabel("Y")
# pl.show()

# con = [23.4, 17.8, 25, 34,40]
# zones = ['East','West','North','South','Central']
# pl.axis("equal")
# pl.pie(con,labels=zones,explode = [0,0,0.2,0,0], autopct = "%1.2f%%")
# pl.show()

# x = [1,2,3,4,5]
# y = [1,4,9,16,25]
# pl.plot(x,y,'r-')
# pl.xlabel('x')
# pl.ylabel('y')
# pl.title("My Chart")
# pl.show()

# p = ([1,2,3,4])
# pl.bar(p,p**2,color='r',width = 0.3)
# pl.bar(p+0.3,p*2, color = 'b',width = 0.3)
# pl.show()

# x =  np.arange(0.,10., 0.1)
# a = np.cos(x)
# b = np.sin(x)
# pl.plot(x,a,'b')
# pl.plot(x,b,'r')
# pl.show()

# p = [1,2,3,4]
# q = [2,4,6,8]
# pl.plot(p,q,'k', marker='d',markersize=5,markeredgecolor = 'red')
# pl.show()

# pl.plot(p,q,'r+',linestyle='solid')
# pl.show()

# pl.plot(p,q, 'r+',linestyle = 'solid',markeredgecolor = 'blue')
# pl.show()

# pl.plot(p,q,'ro')
# pl.show()

# a = np.arange(1,20,1.25)
# b = np.log(a)

# #a
# pl.plot(a,b)

# b
# pl.plot(a,b)
# pl.xlabel('Random Values')
# pl.ylabel('Logarithm Values')

#c
# c = np.cos(a)
# pl.plot(a,b)
# pl.plot(a, c, linestyle='dashdot' )

#d
# c = np.cos(a)
# pl.plot(a,b)
# pl.plot(a,c, 'bo',linestyle = 'dashdot')

#e
# c = np.cos(a)
# pl.plot(a,b,'bd')
# pl.plot(a,c,'ro')
# pl.show()


