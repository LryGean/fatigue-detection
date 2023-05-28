# 导入cv图片
import cv2 as cv
import dlib  # 人脸识别的库dlib
from imutils import face_utils

# 使用人脸检测器get_frontal_face_detector
detector = dlib.get_frontal_face_detector()

# dlib的68点模型，使用作者训练好的特征预测器
predictor = dlib.shape_predictor("../model/shape_predictor_68_face_landmarks.dat")
print('模型加载成功')

# 读取图片
img = cv.imread('图片路径')
cv.imshow('img', img)

# 灰度转换
# 参数：读取的图片
# 参数：更改图片颜色
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# # 显示灰度
# cv.imshow('gray', gray_img)
# # 保存灰度图片
# cv.imwrite('gray/gray_face11.png', gray_img)
# 显示图片
# cv.imshow('read_img', img)

# 使用人脸检测器检测每一帧图像中的人脸。并返回人脸数faces
faces = detector(gray_img, 0)
if len(faces) != 0:
    # 用红色矩形框出人脸
    # enumerate方法同时返回数据对象的索引和数据，k为索引，d为faces中的对象
    for k, d in enumerate(faces):
        # 用红色矩形框出人脸
        cv.rectangle(img, (d.left(), d.top()), (d.right(), d.bottom()), (0, 0, 255), 1)
        # 使用预测器得到68点数据的坐标
        shape = predictor(img, d)
        # 圆圈显示每个特征点
        for i in range(68):
            cv.circle(img, (shape.part(i).x, shape.part(i).y), 2, (0, 255, 0), -1, 8)
        # 将脸部特征信息转换为数组array的格式
        shape = face_utils.shape_to_np(shape)
# 显示
cv.imshow('re_img', img)

# 等待
# 键盘输入q可退出运行
while True:
    if ord('q') == cv.waitKey(0):
        break
# 释放内容
cv.destroyAllWindows()
