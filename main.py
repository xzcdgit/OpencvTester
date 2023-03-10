from PyQt5.QtCore import pyqtSlot, pyqtSignal, QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QFileDialog, QMessageBox
from PyQt5.QtGui import QImage, QPixmap, QWheelEvent, QCursor
import sys
import os
import cv2
import numpy as np
import Ui_Main
import Ui_ChildParam
font = cv2.FONT_HERSHEY_TRIPLEX

class QtOpencv():
    '''opencv 图像操作的具体实现'''
    def __init__(self) -> None:
        #self.operate_name_list = ['灰度化', '高斯滤波','二值化','膨胀','腐蚀','开运算','闭运算','边缘检测','轮廓查找']
        pass

    def method_open_img(self, input_dir:str):
        '''
        载入图片
        param input_dir:图片的路径地址 字符串格式
        '''
        img_bgr = cv2.imread(input_dir)
        img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
        return img_rgb

    def method_deal_img(self,img ,param_list:list):
        tips = ''
        img_res = img.copy()
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
                    return 2,0,'错误步骤序号：'+str(opt_index)+' 图像通道错误，检查进行轮廓查找操作的图像是否为单通道图像\n'
        img_show = img_res #根据需要显示的位置截取显示部分传回
        return 0, img_show, tips

    def method_export_code(self,param_list:list):
        code_str = 'def func_opencv_demo(img):\n'
        for i in param_list:
            if i[0] == 0:
                code_str += "    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)\n"
            #图像高斯模糊
            elif i[0] == 1:
                if i[1]%2 == 0:
                    i[1] += 1
                if i[2]%2 == 0:
                    i[2] += 1
                code_str += "    img = cv2.GaussianBlur(img, (%d, %d, %d)\n" % (i[1],i[2],i[3])
            #图像二值化
            elif i[0] == 2:
                code_str += "    res, img = cv2.threshold(img, %d, %d, %d)\n" % (i[1],i[2],i[3])
            #膨胀
            elif i[0] == 3:
                if i[1] == 0:
                    i[1] += 1
                if i[2] == 0:
                    i[2] += 1
                code_str += "    kernel = np.ones((%d, %d), np.uint8)\n" % (i[1],i[2])
                code_str += "    img = cv2.dilate(img, kernel, %d)\n" % (i[3])
            #腐蚀
            elif i[0] == 4:
                if i[1] == 0:
                    i[1] += 1
                if i[2] == 0:
                    i[2] += 1
                code_str += "    kernel = np.ones((%d, %d), np.uint8)\n" % (i[1],i[2])
                code_str += "    img = cv2.erode(img, kernel, %d)\n" % (i[3])
            #开运算
            elif i[0] == 5:
                code_str += "    kernel = np.ones((%d, %d), np.uint8)\n" % (i[1],i[2])
                code_str += "    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)\n"
            #闭运算
            elif i[0] == 6:
                code_str += "    kernel = np.ones((%d, %d), np.uint8)\n" % (i[1],i[2])
                code_str += "    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)\n"
            #边缘检测
            elif i[0] == 7:
                code_str += "    img = cv2.Canny(img, %d, %d)\n" % (i[1],i[2])
            #轮廓查找
            elif i[0] == 8:
                code_str += "    contours, hierarchy = cv2.findContours(img, %d, %d)\n" % (i[1],i[2])
                code_str += "    model = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)\n"
                code_str += "    img = cv2.drawContours(model, contours, -1, (255, 255, 0), 1)\n"
        return code_str

            

class ChildParamWindow(QDialog, Ui_ChildParam.Ui_ChildParam):
    signal_img_fresh = pyqtSignal(list)#信号 发往主界面类 刷新主界面显示图像信号
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
        self.listWidget.itemClicked.connect(self.slot_set_param)
        #关联信号 双击后删除列表里的操作流程
        self.listWidget.itemDoubleClicked.connect(self.method_remove_item)
        #关联信号 拉杆变化 将变化后的值实时写入参数list
        for i in self.slider_list:
            i.valueChanged.connect(self.method_get_slider_value)
        #图像刷新按键
        self.pushButton_11.clicked.connect(self.method_emit_fresh)
        #参数说明
        self.pushButton_12.clicked.connect(self.method_opt_instruction)
        #导出操作代码
        self.pushButton.clicked.connect(self.method_opt_code_export)

    def setParam(self):
        '''
        预设的各类参数
        '''
        self.operate_param_list = []
        self.operate_index = -1
        #opencv操作字典
        self.opencv_opt_dict = {
            '灰度化':(self.slot_gray_param,'将RGB图像转化为灰度图像（3通道变为单通道）\n如果将单通道图像进行灰度化操作会报错\n无可设置参数\n'), \
            '高斯滤波':(self.slot_gauss_blur_param,'将图像进行高斯滤波操作\n参数说明\n卷积核高：高斯卷积核的高度，应为奇数\n卷积核长：高斯卷积核的宽度，应为奇数\n'), \
            '二值化':(self.slot_threshold_param,'将图像按照指定阈值处理为两种值，是轮廓查找的前提条件\n参数说明\n阈值：大于该值的值会被设置为设定值1，否则设置为设定值2\n最大值：通常是设定值1\n二值化算法类型：包括THRESH_BINARY(0) THRESH_BINARY_INV(1) THRESH_TRUNC(2) THRESH_TOZERO(3) THRESH_TOZERO_INV(4) 这五种类型，具体说明请自行查阅\n'), \
            '膨胀':(self.slot_dilate_param,'将图像的亮值部分扩大,可以用来消除黑色的噪点\n参数说明\n卷积核高：膨胀内核的高度\n卷积核长：膨胀内核的长度\n膨胀次数：膨胀操作的循环次数'), \
            '腐蚀':(self.slot_erode_param,'将图像的暗值部分扩大,可以用来消除白色的噪点\n参数说明\n卷积核高：腐蚀内核的高度\n卷积核长：腐蚀内核的长度\n腐蚀次数：腐蚀操作的循环次数'), \
            '开运算':(self.slot_opening_param,'先腐蚀再膨胀，该操作可以在保持图像整体大小不变的情况下消除白色噪点\n参数说明\n卷积核高：操作内核的高度\n卷积核长：操作内核的长度\n'), \
            '闭运算':(self.slot_closing_param,'先膨胀再腐蚀，该操作可以在保持图像整体大小不变的情况下消除黑色噪点\n参数说明\n卷积核高：操作内核的高度\n卷积核长：操作内核的长度\n'), \
            '边缘检测':(self.slot_canny_param,'特指Canny算法的边缘检测，请自行查阅该算法的说明'), \
            '轮廓查找':(self.slot_fincontours_param,'根据二值图描绘出图像轮廓，实际返回的是散点组，这里为了方便调试，使用drawContours将散点组绘制在空白画布上\n参数说明\n轮廓的检索模式：cv2.RETR_EXTERNAL(0)表示只检测外轮廓\ncv2.RETR_LIST(1)检测的轮廓不建立等级关系\ncv2.RETR_CCOMP(2)建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息。如果内孔内还有一个连通物体，这个物体的边界也在顶层。\ncv2.RETR_TREE(3)建立一个等级树结构的轮廓。\n轮廓的近似办法：cv2.CHAIN_APPROX_NONE(0)存储所有的轮廓点，相邻的两个点的像素位置差不超过1，即max（abs（x1-x2），abs（y2-y1））==1\ncv2.CHAIN_APPROX_SIMPLE(1)压缩水平方向，垂直方向，对角线方向的元素，只保留该方向的终点坐标，例如一个矩形轮廓只需4个点来保存轮廓信息\ncv2.CHAIN_APPROX_TC89_L1(2)，CV_CHAIN_APPROX_TC89_KCOS(3)使用teh-Chinl chain 近似算法\n')
        }  
        #滑块list
        self.slider_list = [self.horizontalSlider, self.horizontalSlider_2, self.horizontalSlider_3, self.horizontalSlider_4, self.horizontalSlider_5, self.horizontalSlider_6, self.horizontalSlider_7, self.horizontalSlider_8]
        #滑块值数值显示 lable list
        self.label_list = [self.label,self.label_2,self.label_3, self.label_4, self.label_5, self.label_6, self.label_7, self.label_8]
        #分组标题box list
        self.groupBox_list = [self.groupBox_6, self.groupBox_7, self.groupBox_8, self.groupBox_11, self.groupBox_13, self.groupBox_14, self.groupBox_15, self.groupBox_9]
        #初始禁用box list中所有的groupBox
        for i in self.groupBox_list:
            i.setEnabled(False)

    def method_opt_code_export(self):
        self.textBrowser.clear() #清空文本框
        tmp = QtOpencv()
        self.textBrowser.setText(tmp.method_export_code(self.operate_param_list))
        

    def method_auto_fresh(self):
        '''
        参数修改时 自动刷新图像判定函数
        如果自动刷新选项勾选则调用界面刷新函数
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
        self.listWidget.takeItem(remove_index)
        del self.operate_param_list[remove_index] #移除指定位置的元素
        self.method_set_ui() #刷新ui界面

    def slot_set_param(self):
        '''
        点击listwidget中的任意项后触发该槽函数
        该槽函数会根据点击项的类型和它在list中的位置获取它的参数并重新写入ui界面
        '''
        item_index = self.sender().currentRow()
        item_name = self.sender().currentItem().text()
        self.operate_index = item_index #设置实例参数的当前操作位置
        self.groupBox_2.setTitle('序号 '+str(item_index)+'  操作名 '+item_name)
        #如果键值存在于字典中
        if item_name in self.opencv_opt_dict.keys():
            (self.opencv_opt_dict[item_name][0])() #执行对应的方法函数
            self.method_auto_fresh()#刷新界面

    def method_set_ui(self,enabled_list:list[bool]=[False,False,False,False,False,False,False,False],name_list:list[str]=[' ',' ',' ',' ',' ',' ',' ',' '],value_list:list[int]=[0,0,0,0,0,0,0,0],lowlimit_list:list[int]=[0,0,0,0,0,0,0,0],uplimit_list:list[int]=[0,0,0,0,0,0,0,0]):
        '''
        ui界面设置
        '''
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
            param_value_list[index].setValue(value_list[index])

        #重新关联信号
        for i in self.slider_list:
            i.valueChanged.connect(self.method_get_slider_value)
            

    def slot_gray_param(self):
        '''
        灰度化有关的ui修改操作
        '''
        self.method_set_ui()
        
    def slot_gauss_blur_param(self):
        '''
        高斯模糊有关的ui修改操作
        '''
        name_list = ['卷积核高','卷积核长','X向标准差','Y向标准差',' ',' ',' ',' ']
        enabled_list = [True,True,True,True,False,False,False,False]
        value_list = self.operate_param_list[self.operate_index][1:]
        lowlimit_list = [0]*8
        uplimit_list = [100]*8
        self.method_set_ui(enabled_list,name_list,value_list,lowlimit_list,uplimit_list)
        
    def slot_threshold_param(self):
        '''
        二值化有关的ui修改操作
        '''
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
        name_list = ['卷积核高','卷积核长','膨胀次数',' ',' ',' ',' ',' ']
        enabled_list = [True,True,True,False,False,False,False,False]
        value_list = self.operate_param_list[self.operate_index][1:]
        lowlimit_list = [0]*8
        uplimit_list = [200,200,200,0,0,0,0,0]
        self.method_set_ui(enabled_list,name_list,value_list,lowlimit_list,uplimit_list)

    def slot_erode_param(self):
        '''
        腐蚀
        '''
        name_list = ['卷积核高','卷积核长','腐蚀次数',' ',' ',' ',' ',' ']
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
        name_list = ['卷积核高','卷积核长',' ',' ',' ',' ',' ',' ']
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
        name_list = ['卷积核高','卷积核长',' ',' ',' ',' ',' ',' ']
        enabled_list = [True,True,False,False,False,False,False,False]
        value_list = self.operate_param_list[self.operate_index][1:]
        lowlimit_list = [0]*8
        uplimit_list = [200,200,0,0,0,0,0,0]
        self.method_set_ui(enabled_list,name_list,value_list,lowlimit_list,uplimit_list)
    def slot_canny_param(self):
        '''
        边缘检测
        '''
        name_list = ['最小阈值','最大阈值',' ',' ',' ',' ',' ',' ']
        enabled_list = [True,True,False,False,False,False,False,False]
        value_list = self.operate_param_list[self.operate_index][1:]
        lowlimit_list = [0]*8
        uplimit_list = [255,255,0,0,0,0,0,0]
        self.method_set_ui(enabled_list,name_list,value_list,lowlimit_list,uplimit_list)

    def slot_fincontours_param(self):
        '''
        轮廓查找
        '''
        name_list = ['轮廓检索模式','轮廓逼近模式',' ',' ',' ',' ',' ',' ']
        enabled_list = [True,True,False,False,False,False,False,False]
        value_list = self.operate_param_list[self.operate_index][1:]
        lowlimit_list = [0]*8
        uplimit_list = [3,3,0,0,0,0,0,0]
        self.method_set_ui(enabled_list,name_list,value_list,lowlimit_list,uplimit_list)


    def method_emit_fresh(self):
        '''
        向主类发送图像刷新信号 按键
        '''
        if self.checkBox_3.isChecked() == True and self.listWidget.currentRow()>=0:
            param_list = self.operate_param_list[0:self.listWidget.currentRow()+1]
        else:
            param_list = self.operate_param_list
        self.signal_img_fresh.emit(param_list)

    def method_opt_instruction(self):
        '''
        opencv各类操作的说明
        '''
        #只有list中有项目时才能调用参数说明
        if self.listWidget.currentRow()>=0:
            #判定选择的选项是否是存在的操作（正常情况下一定是，除非出现未知bug）
            if self.listWidget.currentItem().text() in self.opencv_opt_dict.keys():
                #查询字典 获取对应的参数说明字符串
                opt_instruction_str = self.opencv_opt_dict[self.listWidget.currentItem().text()][1]
                QMessageBox.information(self,'参数说明',opt_instruction_str,QMessageBox.Ok)

class MyMainWindow(QMainWindow, Ui_Main.Ui_MainWindow):
    
    def __init__(self) -> None:
        super().__init__()#执行QMainWindow的__init__()方法
        self.setupUi(self)#初始化Ui组件
        self.iniChiled()#初始化子窗口
        self.setSign()#设置槽和信号
        self.default_out_dir = ''
        self.default_input_dir = ''
        self.enlarge_num = 0
        self.label.setScaledContents(True) #图片自适应label的大小
        self.img = None
        self.img_xstart_index = 0
        self.img_xend_index = 0
        self.img_ystart_index = 0
        self.img_yend_index = 0
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
        子窗口修改参数时会触发该槽函数，该槽函数会调用opencv处理类处理图像再重新显示在label上
        '''
        res, img, tips = self.qtopencv.method_deal_img(self.img,param_list)
        if res == 0:
            tips = '操作成功\n' + tips
            self.method_label_show_img(img)
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
            read_img = self.qtopencv.method_open_img(self.default_input_dir)
            self.img = np.array(read_img)
            self.img_xstart_index = 0
            self.img_xend_index = self.img.shape[1]
            self.img_ystart_index = 0
            self.img_yend_index = self.img.shape[0]
            self.method_label_show_img(self.img)
        else:
            print('路径为空')

    def slot_show_paramtester(self):
        '''
        弹出参数调整子窗口
        '''
        self.testerwindow.show()

    def method_label_show_img(self,img):
        '''
        在label里显示图片
        '''
        img = np.array(img)
        #判断图像是否为单通道图像
        if len(img.shape) == 3:
            #print('多通道图像')
            print()
            img = img[self.img_ystart_index:self.img_yend_index,self.img_xstart_index:self.img_xend_index,:]
            
            img = np.array(img)
            img = QImage(img.data,img.shape[1],img.shape[0],img.shape[1]*3,QImage.Format_RGB888)
        else:
            #print('单通道图像')
            img = img[self.img_ystart_index:self.img_yend_index,self.img_xstart_index:self.img_xend_index]
            img = np.array(img)
            img = QImage(img.data,img.shape[1],img.shape[0],img.shape[1],QImage.Format_Indexed8)
        img = QPixmap(img) #加载图片
        self.label.setPixmap(img) #显示图片

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
        pass
        #print(tips)

    def closeEvent(self, event) -> None:
        reply = QMessageBox.question(self, '提示',
                    "退出主程序?",
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.No)
        if reply == QMessageBox.Yes:
            #退出所有尚未关闭的子窗口
            QCoreApplication.instance().quit
            event.accept()
            sys.exit(0)
        else:
            event.ignore()

    def wheelEvent(self, a0:QWheelEvent) -> None:
        '''
        通过滚轮可以放大或者缩小图像
        '''
        #判定鼠标位置是否在滚轮内（只有鼠标位于控件内滚动滚轮事件才有效）
        is_contain = self.label.geometry().contains(self.mapFromGlobal(QCursor.pos()))
        if is_contain:
            #获取滚轮的滚动方向
            angle = a0.angleDelta()
            angle_y = angle.y()
            #计算放大或者缩小的倍率
            xp = self.mapFromGlobal(QCursor.pos()).x()/self.label.geometry().width()
            yp = self.mapFromGlobal(QCursor.pos()).y()/self.label.geometry().height()
            wsp = 0.1*xp
            wep = 0.1*(1.0-xp)
            hsp = 0.1*yp
            hep = 0.1*(1.0-yp)
            #放大操作
            if angle_y>0:
                w0 = self.img_xend_index - self.img_xstart_index
                h0 = self.img_yend_index - self.img_ystart_index
                if w0>3 and h0 >3:
                    self.img_xstart_index = int(self.img_xstart_index + w0*wsp)
                    self.img_xend_index = int(self.img_xend_index -w0*wep)
                    self.img_ystart_index = int(self.img_ystart_index + h0*hsp)
                    self.img_yend_index = int(self.img_yend_index - h0*hep)
            #缩小操作
            elif angle_y<0:
                w0 = self.img_xend_index - self.img_xstart_index
                h0 = self.img_yend_index - self.img_ystart_index
                self.img_xstart_index = int(self.img_xstart_index - w0*wsp)
                self.img_xend_index = int(self.img_xend_index + w0*wep)
                self.img_ystart_index = int(self.img_ystart_index -h0*hsp)
                self.img_yend_index = int(self.img_yend_index + h0*hep)
                if self.img_xstart_index<0 or self.img_ystart_index<0 or self.img_xend_index >self.img.shape[1] or self.img_yend_index>self.img.shape[0]:
                    self.img_xstart_index = 0
                    self.img_xend_index = self.img.shape[1]
                    self.img_ystart_index = 0
                    self.img_yend_index = self.img.shape[0]
            #调用子窗口的图片刷新图像 间接向主窗口发送刷新图像信号（因为子窗口才有图像的处理参数数据）
            self.testerwindow.method_emit_fresh()
        return super().wheelEvent(a0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywin = MyMainWindow()
    mywin.show()
    sys.exit(app.exec_())
