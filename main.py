from PyQt5.QtCore import pyqtSlot, QThread, pyqtSignal, QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QFileDialog, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
import matplotlib.pyplot as plt
import Ui_Main
from Ui_ChildParam import Ui_ChildParam
import time
import sys
import os
import cv2
import numpy as np
font = cv2.FONT_HERSHEY_TRIPLEX

class QtOpencv():
    '''一系列图像操作'''
    def __init__(self) -> None:
        #self.operate_name_list = ['灰度化', '高斯滤波','二值化','膨胀','腐蚀','开运算','闭运算','边缘检测','轮廓查找']
        self.img = None
        self.img_readed = False

    def method_open_img(self, input_dir:str):
        img_bgr = cv2.imread(input_dir)
        img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
        self.img = img_rgb
        self.img_readed = True
        return self.img
        
    def method_deal_img(self, param_list:list):
        tips = ''
        if self.img_readed == False:
            tips += '未加载图像\n'
            return 1, 0, tips
        img_res = self.img.copy()
        for i in param_list:
            #RGB图像转灰度图像
            if i[0] == 0:
                try:
                    img_res = cv2.cvtColor(img_res,cv2.COLOR_RGB2GRAY)
                except cv2.error:
                    opt_index = param_list.index(i)
                    return 2,0,'错误步骤序号：'+str(opt_index)+' 图像通道错误，检查进行灰度操作的图像是否为多通道图像\n'
            #图像高斯模糊
            elif i[0] == 1:
                if i[1]%2 == 0:
                    i[1] += 1
                    tips += '警告：高斯模糊卷积核x向为偶数，已自动+1\n'
                if i[2]%2 == 0:
                    i[2] += 1
                    tips += '警告：高斯模糊卷积核y向为偶数，已自动+1\n'
                img_res = cv2.GaussianBlur(img_res, (i[1], i[2]), i[3])
            #图像二值化
            elif i[0] == 2:
                res, img_res = cv2.threshold(img_res, i[1], i[2], i[3])
            #膨胀
            elif i[0] == 3:
                if i[1] == 0:
                    i[1] += 1
                    tips += '警告：膨胀卷积核x向为0，已自动+1\n'
                if i[2] == 0:
                    i[2] += 1
                    tips += '警告：膨胀卷积核y向为0，已自动+1\n'
                kernel = np.ones((i[1],i[2]),np.uint8)
                img_res = cv2.dilate(img_res,kernel,i[3])
            #腐蚀
            elif i[0] == 4:
                if i[1] == 0:
                    i[1] += 1
                    tips += '警告：腐蚀卷积核x向为0，已自动+1\n'
                if i[2] == 0:
                    i[2] += 1
                    tips += '警告：腐蚀卷积核y向为0，已自动+1\n'
                kernel = np.ones((i[1],i[2]),np.uint8)
                img_res = cv2.erode(img_res,kernel,i[3])
            #开运算
            elif i[0] == 5:
                kernel = np.ones((i[1],i[2]),np.uint8)
                img_res = cv2.morphologyEx(img_res,cv2.MORPH_OPEN,kernel)
            #闭运算
            elif i[0] == 6:
                kernel = np.ones((i[1],i[2]),np.uint8)
                img_res = cv2.morphologyEx(img_res,cv2.MORPH_CLOSE,kernel)
            #边缘检测
            elif i[0] == 7:
                img_res = cv2.Canny(img_res,i[1],i[2])
            #轮廓查找
            elif i[0] == 8:
                try:
                #二值化结果 轮廓散点信息 层级
                    contours,hierarchy = cv2.findContours(img_res,i[1],i[2])
                    model = np.zeros((img_res.shape[0],img_res.shape[1],3),np.uint8)
                    img_res = cv2.drawContours(model,contours,-1,(255,255,0),1)
                except cv2.error:
                    opt_index = param_list.index(i)
                    return 2,0,'错误步骤序号：'+str(opt_index)+' 图像通道错误，检查进行灰度操作的图像是否为单通道图像\n'
        #print(0,img_res,tips)
        return 0, img_res, tips

class ParamAdjust(QThread):
    '''
    参数调整线程
    '''
    signal_finish = pyqtSignal(str) #结束信号
    signal_param = pyqtSignal(list) #参数返回信号
    def __init__(self) -> None:
        super().__init__()#调用父类的__init__()函数
    def run(self):

        self.signal_finish.emit('thread is end')

class ChildParamWindow(QDialog, Ui_ChildParam):
    signal_img_fresh = pyqtSignal(list)#信号 刷新主界面显示图像信号
    signal_close = pyqtSignal() #子窗口关闭信号

    def __init__(self) -> None:
        super().__init__() #初始化窗口框架
        self.setupUi(self) #初始化窗口控件
        self.setParam() #设置实例参数
        self.setSign() #关联信号
    
    def setSign(self):
        '''
        关联信号
        '''
        #关联信号 双击后再操作列表里新增一个对应的操作流程
        self.listWidget_2.itemDoubleClicked.connect(self.method_add_item)
        #关联信号 单击一个操作流程 显示该流程的各项参数信息并可以修改这些参数
        self.listWidget.itemClicked.connect(self.method_set_param)
        #关联信号 双击后删除列表里的操作流程
        self.listWidget.itemDoubleClicked.connect(self.method_remove_item)
        #关联信号 拉杆变化返回
        for i in self.slider_list:
            i.valueChanged.connect(self.method_get_slider_value)
        #图像刷新按键
        self.pushButton_11.clicked.connect(self.method_emit_fresh)

    def setParam(self):
        '''
        预设的各类参数
        '''
        self.operate_param_list = []
        self.operate_index = -1
        self.operate_name_list = ['灰度化', '高斯滤波','二值化','膨胀','腐蚀','开运算','闭运算','边缘检测','轮廓查找']
        self.operate_method_list = [self.slot_gray_param, self.slot_gauss_blur_param, self.slot_threshold_param,self.slot_dilate_param,self.slot_erode_param,self.slot_opening_param,self.slot_closing_param,self.slot_canny_param,self.slot_fincontours_param]
        #滑块
        self.slider_list = [self.horizontalSlider, self.horizontalSlider_2, self.horizontalSlider_3, self.horizontalSlider_4, self.horizontalSlider_5, self.horizontalSlider_6, self.horizontalSlider_7, self.horizontalSlider_8]
        #滑块值显示
        self.label_list = [self.label,self.label_2,self.label_3, self.label_4, self.label_5, self.label_6, self.label_7, self.label_8]
        #提示信息box
        self.groupBox_list = [self.groupBox_6, self.groupBox_7, self.groupBox_8, self.groupBox_11, self.groupBox_13, self.groupBox_14, self.groupBox_15, self.groupBox_9]
        
        for i in self.groupBox_list:
            i.setEnabled(False)


    def method_auto_fresh(self):
        '''
        参数修改时 自动刷新图像判定函数
        '''
        if self.checkBox.isChecked() == True:
            self.method_emit_fresh()


    def method_get_slider_value(self):
        
        '''
        获取滑块的值并写入参数list
        滑块参数变更时修改参数list的值
        '''
        value = self.sender().value()
        param_index = self.slider_list.index(self.sender())
        #print(self.operate_index,param_index+1)
        #print(self.operate_param_list)
        self.operate_param_list[self.operate_index][param_index+1] = value

        (self.label_list[param_index]).setText(str(value))
        self.method_auto_fresh()

    def method_add_item(self):
        '''
        添加操作到item列表中
        '''
        method_index = self.listWidget_2.currentRow() #操作方法类型
        opt_index = self.listWidget.currentRow() #操作序列位置
        #初始化添加值
        if self.checkBox_2.isChecked() == True and opt_index != -1 and self.listWidget.count()!=0:#插入模式
            self.operate_param_list.insert(opt_index,[method_index,0,0,0,0,0,0,0,0,0])
            method_name = self.sender().currentItem().text()
            self.listWidget.insertItem(opt_index,method_name)

        else:
            self.operate_param_list.append([method_index,0,0,0,0,0,0,0,0,0])
            method_name = self.sender().currentItem().text()
            self.listWidget.addItem(method_name)


            

    def method_remove_item(self):
        '''
        移除item中的指定项
        '''
        remove_index = self.listWidget.currentRow()
        #print('remove', remove_index) 
        self.listWidget.takeItem(remove_index)
        del self.operate_param_list[remove_index] #移除指定位置的元素
        self.method_set_ui()

    def method_set_param(self):
        '''
        函数操作参数设置 总控方法
        '''
        item_index = self.sender().currentRow()
        self.operate_index = item_index #设置当前图像处理操作的序号
        item_name = self.sender().item(item_index).text()
        self.groupBox_2.setTitle('序号 '+str(item_index)+'  操作名 '+item_name)
        if item_name in self.operate_name_list:
            operate_method_index = self.operate_name_list.index(item_name) #获取序号
            (self.operate_method_list[operate_method_index])() #执行对应的方法函数
            self.method_emit_fresh()#刷新界面

    def method_set_ui(self,enabled_list:list[bool]=[False,False,False,False,False,False,False,False],name_list:list[str]=[' ',' ',' ',' ',' ',' ',' ',' '],value_list:list[int]=[0,0,0,0,0,0,0,0],lowlimit_list:list[int]=[0,0,0,0,0,0,0,0],uplimit_list:list[int]=[0,0,0,0,0,0,0,0]):
        '''
        ui界面设置
        '''
        ###
        #由于改变拉杆上下限时如果当前拉杆值不在范围内，会自行移动至上下限范围内，导致触发拉杆值变化的槽函数，导致参数list内的值被异常修改。所以先解除关联
 
        #取消关联信号 拉杆变化返回
        for i in self.slider_list:
            i.valueChanged.disconnect(self.method_get_slider_value)
        groupBox_list = self.groupBox_list
        param_value_list = self.slider_list
        label_list = self.label_list
        for i in param_value_list:
            index = param_value_list.index(i)
            groupBox_list[index].setEnabled(enabled_list[index])
            groupBox_list[index].setTitle(name_list[index])
            param_value_list[index].setMinimum(lowlimit_list[index])
            param_value_list[index].setMaximum(uplimit_list[index])
            label_list[index].setText(str(value_list[index]))
            #if value_list[index]>=param_value_list[index].minimum() and value_list[index]<=param_value_list[index].maximum():
            param_value_list[index].setValue(value_list[index])
        #关联信号 拉杆变化返回
        for i in self.slider_list:
            i.valueChanged.connect(self.method_get_slider_value)
            

    def slot_gray_param(self):
        '''
        灰度化有关的ui修改操作
        '''
        #print('gray')
        self.method_set_ui()
        
    def slot_gauss_blur_param(self):
        '''
        高斯模糊有关的ui修改操作
        '''
        #print('gauss blur')
        name_list = ['卷积核宽','卷积核长','X向标准差','Y向标准差',' ',' ',' ',' ']
        enabled_list = [True,True,True,True,False,False,False,False]
        value_list = self.operate_param_list[self.operate_index][1:]
        lowlimit_list = [0]*8
        uplimit_list = [100]*8
        self.method_set_ui(enabled_list,name_list,value_list,lowlimit_list,uplimit_list)
        
    def slot_threshold_param(self):
        '''
        二值化有关的ui修改操作
        '''
        #print('threshold')
        name_list = ['阈值','最大值','二值化算法类型',' ',' ',' ',' ',' ']
        enabled_list = [True,True,True,False,False,False,False,False]
        value_list = self.operate_param_list[self.operate_index][1:]
        lowlimit_list = [0]*8
        uplimit_list = [255,255,4,0,0,0,0,0]
        self.method_set_ui(enabled_list,name_list,value_list,lowlimit_list,uplimit_list)

    def slot_dilate_param(self):
        '''
        膨胀
        '''
        #print('dilate')
        name_list = ['卷积核宽','卷积核长','膨胀次数',' ',' ',' ',' ',' ']
        enabled_list = [True,True,True,False,False,False,False,False]
        value_list = self.operate_param_list[self.operate_index][1:]
        lowlimit_list = [0]*8
        uplimit_list = [200,200,200,0,0,0,0,0]
        self.method_set_ui(enabled_list,name_list,value_list,lowlimit_list,uplimit_list)

    def slot_erode_param(self):
        '''
        腐蚀
        '''
        #print('erode')
        name_list = ['卷积核宽','卷积核长','腐蚀次数',' ',' ',' ',' ',' ']
        enabled_list = [True,True,True,False,False,False,False,False]
        value_list = self.operate_param_list[self.operate_index][1:]
        lowlimit_list = [0]*8
        uplimit_list = [200,200,200,0,0,0,0,0]
        self.method_set_ui(enabled_list,name_list,value_list,lowlimit_list,uplimit_list)

    def slot_opening_param(self):
        '''
        开运算
        先腐蚀后膨胀
        '''
        #print('opening')
        name_list = ['卷积核宽','卷积核长',' ',' ',' ',' ',' ',' ']
        enabled_list = [True,True,False,False,False,False,False,False]
        value_list = self.operate_param_list[self.operate_index][1:]
        lowlimit_list = [0]*8
        uplimit_list = [200,200,0,0,0,0,0,0]
        self.method_set_ui(enabled_list,name_list,value_list,lowlimit_list,uplimit_list)

    def slot_closing_param(self):
        '''
        闭运算
        先膨胀后腐蚀
        '''
        #print('closing')
        name_list = ['卷积核宽','卷积核长',' ',' ',' ',' ',' ',' ']
        enabled_list = [True,True,False,False,False,False,False,False]
        value_list = self.operate_param_list[self.operate_index][1:]
        lowlimit_list = [0]*8
        uplimit_list = [200,200,0,0,0,0,0,0]
        self.method_set_ui(enabled_list,name_list,value_list,lowlimit_list,uplimit_list)
    def slot_canny_param(self):
        '''
        边缘检测
        '''
        #print('canny')
        name_list = ['低阈值','高阈值',' ',' ',' ',' ',' ',' ']
        enabled_list = [True,True,False,False,False,False,False,False]
        value_list = self.operate_param_list[self.operate_index][1:]
        lowlimit_list = [0]*8
        uplimit_list = [255,255,0,0,0,0,0,0]
        self.method_set_ui(enabled_list,name_list,value_list,lowlimit_list,uplimit_list)

    def slot_fincontours_param(self):
        '''
        轮廓查找
        '''
        #print('fincontours')
        name_list = ['轮廓检索模式','轮廓逼近模式',' ',' ',' ',' ',' ',' ']
        enabled_list = [True,True,False,False,False,False,False,False]
        value_list = self.operate_param_list[self.operate_index][1:]
        lowlimit_list = [0]*8
        uplimit_list = [3,1,0,0,0,0,0,0]
        self.method_set_ui(enabled_list,name_list,value_list,lowlimit_list,uplimit_list)


    def method_emit_fresh(self):
        '''
        向主类发送图像刷新信号 按键
        '''
        print(self.listWidget.currentRow())
        if self.checkBox_3.isChecked() == True and self.listWidget.currentRow()>=0:
            param_list = self.operate_param_list[0:self.listWidget.currentRow()+1]
        else:
            param_list = self.operate_param_list
        self.signal_img_fresh.emit(param_list)

class MyMainWindow(QMainWindow, Ui_Main.Ui_MainWindow):
    
    def __init__(self) -> None:
        super().__init__()#执行QMainWindow的__init__()方法
        self.setupUi(self)#初始化Ui组件
        self.iniChiled()#初始化子窗口
        self.setSign()#设置槽和信号
        self.default_out_dir = ''
        self.default_input_dir = ''
    def iniChiled(self):
        '''
        创建子类
        '''
        self.testerwindow = ChildParamWindow()#子窗口
        self.qtopencv = QtOpencv()#opencv函数
        

    def setSign(self):
        '''
        关联信号
        '''
        self.action_3.triggered.connect(self.slot_show_paramtester) #显示子窗口
        self.action.triggered.connect(self.slot_open_img) #选择文件
        self.action_4.triggered.connect(self.slot_param_list_test) #参数数组输出测试

        self.testerwindow.signal_img_fresh.connect(self.slot_fresh_label_img) #子窗口参数调整完成修改图像信号

    def slot_fresh_label_img(self,param_list:list[int]):
        '''
        接收刷新的paramlist
        '''
        res, img, tips = self.qtopencv.method_deal_img(param_list)
        if res == 0:
            tips = '操作成功\n' + tips
            self.method_label_img(img)
        else:
            tips = '操作失败\n'+tips
        self.testerwindow.textBrowser.append(tips)

    def slot_param_list_test(self):
        print('---------------------------------')
        print(self.testerwindow.operate_param_list)
        print('---------------------------------')

    def slot_open_img(self):
        self.default_input_dir = self.__method_chose_file() #获取图像路径
        if self.default_input_dir != '':
            img_rgb = self.qtopencv.method_open_img(self.default_input_dir)
            self.method_label_img(img_rgb)
        else:
            print('路径为空')


    def slot_show_paramtester(self):
        '''
        弹出参数调整子窗口
        '''
        self.testerwindow.show()



    def method_label_img(self,img_rgb):
        '''
        在label里显示图片
        '''
        image = np.array(img_rgb)
        #判断图像是否为单通道图像
        if len(image.shape) == 3:
            #print('多通道图像')
            image = QImage(img_rgb,img_rgb.shape[1],img_rgb.shape[0],QImage.Format_RGB888)
        else:
            #print('单通道图像')
            image = QImage(img_rgb,img_rgb.shape[1],img_rgb.shape[0],QImage.Format_Indexed8)
        image = QPixmap(image) #加载图片
        self.label.setScaledContents(True) #图片自适应label的大小
        self.label.setPixmap(image) #显示图片

    def paintEvent(self, QPaintEvent) -> None:
        '''
        窗口重绘事件
        '''
        self.label.resize(self.widget.size())#修改label的尺寸和widget的尺寸保持一致

    def __method_chose_file(self):
        '''
        选择文件 获取文件地址
        '''
        self.default_input_dir = self.default_input_dir or os.getcwd()
        fileInfo = QFileDialog.getOpenFileName(self, "选择文件", self.default_input_dir, "Image Files(*.png;*.jpg;*.jpeg;*.gif)")
        # fileInfo = QFileDialog.getOpenFileName(self, "选择文件", self.default_input_dir, "txt files(*.txt);png Files(*.png)") #多个时用分号分开
        filename = fileInfo[0]
        if filename != "":
            print('图像地址获取成功')
            #self.default_input_dir = filename #设置默认输入图像的地址
            return filename 
        else:
            print('路径为空')
            return ''

    def debug(self):
        print('action_3')

    def doc(self,tips):
        print(tips)

    def closeEvent(self, event) -> None:
        reply = QMessageBox.question(self, '提示',
                    "退出主程序?",
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCoreApplication.instance().quit
            event.accept()
            sys.exit(0)
        else:
            event.ignore()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywin = MyMainWindow()
    mywin.show()
    sys.exit(app.exec_())
