import matplotlib as mpl
import matplotlib.pyplot as plt

#print(mpl.__version__)



x = [1,3,5,10,15]
y = [1, 6,4,10,5]

x1 = [1,3,5,10,15]
y1 = [1, 10,7,4,10]

plt.plot(x,y,label = "Plots 1")
plt.plot(x1,y1,label = "Plots 2")

plt.legend()
plt.show()