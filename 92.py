from matplotlib import pyplot as plt
import numpy as np
fig=plt.figure()
x = np.linspace(-100, 100, 100)
y1=((x**1)+(1**1))/x**1
y2=((x**(1))+(2**(1)))/x**(1)
y3=((x**(2))+(1**(2)))/x**(2)
plt.plot(x, y3, 'g')
plt.plot(x, y2, color='orange')
plt.plot(x, y1, 'b')
plt.legend(['a=1,b=2', 'a=2,b=1','a=1,b=1'])
plt.xlabel('ось x')
plt.ylabel('ось y')
plt.title('график1')
axes1=fig.add_axes([0.2, 0.4, 0.15, 0.15])
axes1.plot([0.15,0.05])
axes1.plot([0.25,0.15])
axes1.plot([0.25,0.3])
plt.show()