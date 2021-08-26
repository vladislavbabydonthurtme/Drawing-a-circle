import numpy as np
import matplotlib.pyplot as plt

R=2
center = (1,1)
Y_1 = []
Y_2 = []
circle =[]

def circl(R,center):
    for i in range(0,360):
        Y_1.append(center[1]+R*np.sin(i))
        Y_2.append(center[0]+R*np.cos(i))
    return Y_1,Y_2

        

ans=circl(R,center)
Y_1 = np.array(ans[0])
Y_2 = np.array(ans[1])
plt.plot(Y_1,Y_2,'ro')
plt.plot(center[0],center[1],'ro')
plt.show()