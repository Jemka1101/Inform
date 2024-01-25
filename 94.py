import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-50, 50, 500)
y1=((x**0.5)+(1**0.5))/x**0.5
y2=((x**(-0.5))+(1**(-0.5)))/x**(-0.5)
y3=((x**(-1.5))+(1**(-1.5)))/x**(-1.5)
plt.plot(x, y3, 'y')
plt.plot(x, y2, 'g')
plt.plot(x, y1, 'r')
plt.xlabel('ось x')
plt.ylabel('ось y')
plt.title('график2')
plt.legend(['a=1,b=0.5', 'a=1,b=-0.5','a=1,b=-1.5'])
plt.show()