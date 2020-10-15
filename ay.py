import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math
 
size = 300
new_im = Image.new("RGBA",(size,size)) #创建一个空的图片
 
a_img = np.array(new_im)  #获取空图片的数据
 
m = (size-50)/2 #函数的摆幅
for i in range(0,size):
    x = 2 * math.pi * (  i / size )  #控制 根据 i / size 的比例，控制 x 的值为  0-2π
    y = size/2 - m*math.sin(x)  #将正弦函数画在中间
    y = int(y)
    if y < size and y >= 0:
        a_img[y][i] = (0,0,0,255)   
 
 
plt.figure("beauty")
plt.imshow(a_img)
#plt.axis('off')
plt.show()