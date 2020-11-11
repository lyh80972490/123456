import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-10.0,10.0,1000)  #通过linspace函数指定t的取值范围
plt.ylim(0,5)                          #定义纵轴取值范围
plt.subplot(221)     #显示的位置
plt.title(u'exp(-0.6*t)')   #图名
ft = np.exp(-0.6*t)              #调用exp函数计算指数信号
plt.plot(t,ft)                #绘图
plt.subplot(222)
plt.title(u'exp(0.6*t)')
ft1 = np.exp(0.6*t)
plt.plot(t,ft1)
plt.subplot(212)
plt.title(u'exp(0*t)')
ft2 = np.exp(0*t)
plt.plot(t,ft2)
plt.show()
