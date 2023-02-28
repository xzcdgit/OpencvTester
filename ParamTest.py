import cv2
import numpy as np

class ParamTester():
    '''
    图像拉杆测试类型，调用method_param_test方法传入所需的图像即可
    '''
    def __init__(self) -> None:
        pass

    def __method_binarization(self, nothing):
        #滤波
        img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        x = cv2.getTrackbarPos('blur_kernel_x','imgDemo')
        y = cv2.getTrackbarPos('blur_kernel_y','imgDemo')
        threshold = cv2.getTrackbarPos('threshold','imgDemo')
        if (x+y) != 0:
            if x%2==0 :
                x = x+1
            if y%2==0:
                y = y+1
            img = cv2.blur(img, (x, y), 1)
        if threshold != 0:
            #阈值化
            ret,img = cv2.threshold(img,threshold,255,0)
        
        
        #开闭运算
        #kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
        #img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel) #开运算
        #kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
        #img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel) #闭运算
        cv2.imshow('imgDemo',img)



    def method_param_test(self,img:cv2.Mat):
        '''
        图像参数测试器
        '''
        self.img = img
        height, width = self.img.shape[:2]
        name_window = 'imgDemo'
        cv2.namedWindow(name_window, cv2.WINDOW_KEEPRATIO)
        cv2.createTrackbar('blur_kernel_x',name_window,1,50,self.__method_binarization)
        cv2.createTrackbar('blur_kernel_y',name_window,1,50,self.__method_binarization)
        cv2.createTrackbar('threshold',name_window,1,255,self.__method_binarization)

        #cv2.createTrackbar('blur_kernel_y',name_window,1,50,self.__method_binarization)
        cv2.waitKey()
        cv2.destroyAllWindows()



def func_img_crop(img:cv2.Mat, row_start_scale:float, row_end_scale:float, col_start_scale:float, col_end_scale:float)->cv2.Mat:
    '''
    func_img_crop(img, row_start_scale, row_end_scale, col_start_scale, col_end_scale)->cv2.Mat
    @param img 需要处理的原图片，格式为opencv的Mat格式。
    @param row_start_scale 图片裁剪的行起始像素百分比位置，0-1之间。
    @param row_end_sacale 图片裁剪的行截止像素百分比位置，0-1之间。
    @param col_start_scale 图片裁剪的列起始像素百分比位置，0-1之间。
    @param col_end_sacle 图片裁剪的列截止像素百分比位置，0-1之间。
    '''
    height, width = img.shape[:2]
    row_start = int(height*row_start_scale)
    row_end = int(height*row_end_scale)

    col_start = int(width*col_start_scale)
    col_end = int(width*col_end_scale)

    img_crop = img[row_start:row_end,col_start:col_end]
    height, width = img_crop.shape[:2]
    return img_crop

def func_img_show(name_window: str, img: cv2.Mat)->None:
    '''
    预览图像
    @param name_windwo: 图像窗口的名称 字符串类型
    @param img: 图像 图像类型为cv.Mat格式
    '''
    cv2.namedWindow(name_window,0) #该行程序是将图片设置成可以拉伸的状态
    cv2.imshow(name_window,img) #显示图片
    cv2.waitKey()
    return

def func_testimg(img:cv2.Mat):
    #截取图片
    img = func_img_crop(img,0.35,0.55,0,1)
    
    #求图像长宽
    h, w = img.shape[:2]
    img_return = np.zeros((h, w, 3), np.uint8)
    img_return.fill(0)
    #赋值原始图像以便修改后回传
    #滤波
    img = cv2.GaussianBlur(img, (5, 5), 1)
    img_r1 = np.zeros((h, w, 3), np.uint8)
    img_r1.fill(0)
    #边缘检测
    img = cv2.Canny(img,120,150)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(2, 5))
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel) #闭运算
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) 
    print('length',len(contours))
    for obj in contours:
        if cv2.contourArea(obj)>500:
            cv2.drawContours(img_r1,obj,-1,(0,255,0),1)  #绘制轮廓线
            hull = cv2.convexHull(obj,True) #拟合凸包
            cv2.polylines(img_r1,[hull],True,(0,0,255),1) #绘制凸包
    return img_r1

if __name__ == '__main__':
    a = [[1,2],[3,4]]
    for i in a:
        i[0] = i[0]+1
    print(a)
    
    

