# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Code\Python\OpencvTester\ChildParam.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChildParam(object):
    def setupUi(self, ChildParam):
        ChildParam.setObjectName("ChildParam")
        ChildParam.resize(675, 664)
        self.gridLayout_13 = QtWidgets.QGridLayout(ChildParam)
        self.gridLayout_13.setVerticalSpacing(6)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.groupBox_10 = QtWidgets.QGroupBox(ChildParam)
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_10)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_10)
        self.listWidget.setDragEnabled(False)
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listWidget.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_10.addWidget(self.listWidget, 0, 0, 1, 3)
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_10.addWidget(self.pushButton_11, 2, 2, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_10.addWidget(self.pushButton_12, 1, 2, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_10)
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_10.addWidget(self.checkBox, 1, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_10)
        self.checkBox_3.setEnabled(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_10.addWidget(self.checkBox_3, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_10.addWidget(self.pushButton, 3, 0, 1, 3)
        self.gridLayout_13.addWidget(self.groupBox_10, 0, 2, 1, 1)
        self.groupBox_12 = QtWidgets.QGroupBox(ChildParam)
        self.groupBox_12.setObjectName("groupBox_12")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_12)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_12)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_3.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.gridLayout_13.addWidget(self.groupBox_12, 0, 3, 1, 3)
        self.groupBox_2 = QtWidgets.QGroupBox(ChildParam)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.groupBox_7)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_2.setTickInterval(1)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.gridLayout_8.addWidget(self.horizontalSlider_2, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_7)
        self.label_2.setObjectName("label_2")
        self.gridLayout_8.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_7, 1, 1, 1, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalSlider_3 = QtWidgets.QSlider(self.groupBox_8)
        self.horizontalSlider_3.setEnabled(True)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.gridLayout_7.addWidget(self.horizontalSlider_3, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_8)
        self.label_3.setObjectName("label_3")
        self.gridLayout_7.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_8, 2, 1, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_6.setEnabled(True)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_6)
        self.horizontalSlider.setAutoFillBackground(False)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_6.addWidget(self.horizontalSlider, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_6)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_6, 0, 1, 1, 1)
        self.groupBox_13 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_13.setTitle("")
        self.groupBox_13.setObjectName("groupBox_13")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_13)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.horizontalSlider_5 = QtWidgets.QSlider(self.groupBox_13)
        self.horizontalSlider_5.setEnabled(True)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.gridLayout_12.addWidget(self.horizontalSlider_5, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_13)
        self.label_5.setObjectName("label_5")
        self.gridLayout_12.addWidget(self.label_5, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_13, 4, 1, 1, 1)
        self.groupBox_11 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_11.setTitle("")
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_11)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_4 = QtWidgets.QLabel(self.groupBox_11)
        self.label_4.setObjectName("label_4")
        self.gridLayout_11.addWidget(self.label_4, 0, 0, 1, 1)
        self.horizontalSlider_4 = QtWidgets.QSlider(self.groupBox_11)
        self.horizontalSlider_4.setEnabled(True)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.gridLayout_11.addWidget(self.horizontalSlider_4, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_11, 3, 1, 1, 1)
        self.groupBox_15 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_15.setTitle("")
        self.groupBox_15.setObjectName("groupBox_15")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.groupBox_15)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.horizontalSlider_7 = QtWidgets.QSlider(self.groupBox_15)
        self.horizontalSlider_7.setEnabled(True)
        self.horizontalSlider_7.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_7.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_7.setObjectName("horizontalSlider_7")
        self.gridLayout_15.addWidget(self.horizontalSlider_7, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_15)
        self.label_7.setObjectName("label_7")
        self.gridLayout_15.addWidget(self.label_7, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_15, 6, 1, 1, 1)
        self.groupBox_14 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_14.setTitle("")
        self.groupBox_14.setObjectName("groupBox_14")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.groupBox_14)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.label_6 = QtWidgets.QLabel(self.groupBox_14)
        self.label_6.setObjectName("label_6")
        self.gridLayout_14.addWidget(self.label_6, 0, 0, 1, 1)
        self.horizontalSlider_6 = QtWidgets.QSlider(self.groupBox_14)
        self.horizontalSlider_6.setEnabled(True)
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.gridLayout_14.addWidget(self.horizontalSlider_6, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_14, 5, 1, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_9.setEnabled(True)
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.horizontalSlider_8 = QtWidgets.QSlider(self.groupBox_9)
        self.horizontalSlider_8.setAutoFillBackground(False)
        self.horizontalSlider_8.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_8.setInvertedAppearance(False)
        self.horizontalSlider_8.setInvertedControls(False)
        self.horizontalSlider_8.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_8.setObjectName("horizontalSlider_8")
        self.gridLayout_9.addWidget(self.horizontalSlider_8, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_9)
        self.label_8.setObjectName("label_8")
        self.gridLayout_9.addWidget(self.label_8, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_9, 7, 1, 1, 1)
        self.gridLayout_13.addWidget(self.groupBox_2, 1, 0, 1, 6)
        self.groupBox = QtWidgets.QGroupBox(ChildParam)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.listWidget_2.setDragEnabled(False)
        self.listWidget_2.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.gridLayout.addWidget(self.listWidget_2, 1, 2, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 0, 2, 1, 1)
        self.gridLayout_13.addWidget(self.groupBox, 0, 0, 1, 2)
        self.gridLayout_13.setColumnMinimumWidth(0, 1)
        self.gridLayout_13.setColumnMinimumWidth(1, 1)
        self.gridLayout_13.setColumnMinimumWidth(2, 1)
        self.gridLayout_13.setColumnMinimumWidth(3, 1)
        self.gridLayout_13.setColumnMinimumWidth(4, 1)
        self.gridLayout_13.setColumnMinimumWidth(5, 1)
        self.gridLayout_13.setRowMinimumHeight(0, 1)
        self.gridLayout_13.setRowMinimumHeight(1, 1)
        self.gridLayout_13.setColumnStretch(0, 1)
        self.gridLayout_13.setColumnStretch(1, 1)
        self.gridLayout_13.setColumnStretch(2, 1)
        self.gridLayout_13.setColumnStretch(3, 1)
        self.gridLayout_13.setColumnStretch(4, 1)
        self.gridLayout_13.setColumnStretch(5, 1)
        self.gridLayout_13.setRowStretch(0, 1)
        self.gridLayout_13.setRowStretch(1, 1)

        self.retranslateUi(ChildParam)
        QtCore.QMetaObject.connectSlotsByName(ChildParam)

    def retranslateUi(self, ChildParam):
        _translate = QtCore.QCoreApplication.translate
        ChildParam.setWindowTitle(_translate("ChildParam", "参数调整表"))
        self.groupBox_10.setTitle(_translate("ChildParam", "操作流程"))
        self.pushButton_11.setText(_translate("ChildParam", "刷新图像"))
        self.pushButton_12.setText(_translate("ChildParam", "参数说明"))
        self.checkBox.setText(_translate("ChildParam", "自动刷新"))
        self.checkBox_3.setText(_translate("ChildParam", "仅到选中项"))
        self.pushButton.setText(_translate("ChildParam", "导出操作代码"))
        self.groupBox_12.setTitle(_translate("ChildParam", "操作提示"))
        self.groupBox_2.setTitle(_translate("ChildParam", "当前选择"))
        self.label_2.setText(_translate("ChildParam", "0"))
        self.label_3.setText(_translate("ChildParam", "0"))
        self.label.setText(_translate("ChildParam", "0"))
        self.label_5.setText(_translate("ChildParam", "0"))
        self.label_4.setText(_translate("ChildParam", "0"))
        self.label_7.setText(_translate("ChildParam", "0"))
        self.label_6.setText(_translate("ChildParam", "0"))
        self.label_8.setText(_translate("ChildParam", "0"))
        self.groupBox.setTitle(_translate("ChildParam", "图像操作选项"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("ChildParam", "灰度化"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("ChildParam", "高斯滤波"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("ChildParam", "二值化"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("ChildParam", "膨胀"))
        item = self.listWidget_2.item(4)
        item.setText(_translate("ChildParam", "腐蚀"))
        item = self.listWidget_2.item(5)
        item.setText(_translate("ChildParam", "开运算"))
        item = self.listWidget_2.item(6)
        item.setText(_translate("ChildParam", "闭运算"))
        item = self.listWidget_2.item(7)
        item.setText(_translate("ChildParam", "边缘检测"))
        item = self.listWidget_2.item(8)
        item.setText(_translate("ChildParam", "轮廓查找"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.checkBox_2.setText(_translate("ChildParam", "插入模式"))
