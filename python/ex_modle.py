# -*- coding: utf-8 -*-
# python 2.7
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
start=time.clock()
print len(sys.argv), sys.argv[0]

func=np.poly1d(np.array([1,0,2]).astype(float))
func1=func.deriv(m=1)	
x=np.linspace(-40,40,50)
y=func(x)
y1=func1(x)
fig=plt.figure()
#plt.plot(x,y,'ro',x,y1,'g--')
"""
plt.subplot(211)
plt.plot(x,y,'ro')
plt.subplot(212)
plt.plot(x,y1,'g^')
plt.xlabel('x')
plt.ylabel('sinc')
#plt.show()
"""
ax=fig.add_subplot(121)
ax.scatter(x,y)     #散点图
end=time.clock()
print end-start