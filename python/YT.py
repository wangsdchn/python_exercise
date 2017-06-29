import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
def YT(imgPath):
    imgName=[]
    imgName=path2list(imgPath)
    for i in imgName:
        if not os.path.isfile(i):
            continue
        print(i)
        src=cv2.imread(i)
        Lab=cv2.cvtColor(src,cv2.COLOR_BGR2HSV)
        L,a,b=Lab[:,:,0],Lab[:,:,1],Lab[:,:,2]
        B,G,R=src[:,:,0],src[:,:,1],src[:,:,2]
        src=b
        cv2.namedWindow('src')
        cv2.imshow('src',src)
#        rgb_list=np.empty((256,3))
#        for i in range(int(src.shape[0])):
#            for j in range(src.shape[1]):
#                rgb_list[src[i,j],0]+=1
#        i=range(255)
#        pltArr(i,rgb_list[1:,])
        if(27==cv2.waitKey(0)&0xff):
            exit()
def pltArr(i,arr):
    fig,ax=plt.subplots(2,2)
    plt.subplot(2,2,1)
    plt.plot(i,arr[:,0])
    plt.subplot(2,2,2)
    plt.plot(i,arr[:,1])
    plt.subplot(2,2,3)
    plt.plot(i,arr[:,2])
    plt.show()
    plt.close() 
def path2list(imgPath):    
    imgName=[]
    files=os.listdir(imgPath)
    #files1=os.listdir(imgPath1)
    for f in files:
        fs=imgPath+f
        if os.path.isdir(fs):
            continue
        if fs[-3:]!="bmp":
            continue
        imgName.append(fs)
#    for f in files1:
#        fs=imgPath1+f
#        if os.path.isdir(fs):
#            continue
#        imgName.append(fs)
    return imgName
    
if __name__=='__main__':
    #ap=argparse.ArgumentParser()
    #ap.add_argument('-i','--image',required=True,help='Path to image')
    #args=vars(ap.parse_args())
    imgPath='./01/'
    #imgPath1='E:/ime/Fruit/picture/YT/BaoXiaoHai/'
    YT(imgPath)
    cv2.destroyAllWindows()
