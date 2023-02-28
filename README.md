# MainControler.py
## 常用opencv算法的参数测试器
    排列组合不同的图像处理方法来调整参数
## 常用的opencv函数备忘
* 灰度化 `cv2.cvtColor(...)`
* 滤波
    * 高斯滤波 `cv2.GaussianBlur(...)`
    * **均值滤波** `cv2.blur(...)`
* 阈值化 <font color=#FF0000>**该类函数的返回值包括两个参数！**</font>
    * func: **`cv2.threshold(...)`** 全局阈值化
    * func: `cv2.adaptiveThreshold(...)` 自适应阈值化
* 形态学变换 **`cv2.morphologyEx(...)`**
    * param: `op = cv2.MORPH_OPEN` 开运算,先腐蚀再膨胀
    * param: `op = cv2.MORPH_CLOSE ` 闭运算,先膨胀再腐蚀
* 查找轮廓 **`cv2.findContours(...)`**
    * param: **`mode = cv2.RETR_EXTERNAL`** 只检测外轮廓
    * param: `mode = cv2.RETR_LIST` 检测的轮廓不建立等级关系
    * param: `mode = cv2.RETR_CCOMP` 建立两个等级的轮廓，上一层为外边界，内层为内孔的边界。如果内孔内还有连通物体，则这个物体的边界也在顶层
    * param: **`mode = cv2.RETR_TREE`** 建立一个等级树结构的轮廓
* 计算点包围的面积 **`cv2.contourArea(...)`**
* 计算点包围的长度 `cv2.arcLength(...)`
* 拟合类型
    * 以多边形拟合轮廓 `cv2.approxPolyDP(...)`
    * 以凸多边形拟合轮廓 `cv2.convexHull(...)`
    * 以矩形拟合轮廓 **`cv2.boundingRect(...)`**
* 查找点包围区域的重心 `cv2.moments(...)`
* 图像绘制
    * 绘制轮廓线 `cv2.drawContours(...)` 
    * 绘制多线段 `cv2.polylines(...)`
    * 绘制矩形 `cv2.rectangle(...)`
    * 绘制圆 `cv2.circle(...)`
    * 绘制文字 `cv2.putText(...)`


