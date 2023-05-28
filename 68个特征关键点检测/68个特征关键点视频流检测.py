# 导入cv图片
import cv2 as cv
import dlib  # 人脸识别的库dlib
from imutils import face_utils


# 监测函数
def face_detect_demo(img, detector, predictor):
    # 灰度转换
    # 参数：读取的图片
    # 参数：更改图片颜色
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # 使用人脸检测器检测每一帧图像中的人脸。并返回人脸数faces
    faces = detector(gray_img, 0)
    # 如果检测到人脸
    if len(faces) != 0:
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
    # 窗口可自由缩放
    cv.namedWindow('result', 0)
    # cv.resizeWindow('result',600,600)
    cv.imshow('result', img)


# 使用人脸检测器get_frontal_face_detector
detector = dlib.get_frontal_face_detector()
# dlib的68点模型，使用作者训练好的特征预测器
predictor = dlib.shape_predictor("../model/shape_predictor_68_face_landmarks.dat")
print('模型加载成功')

# 打开摄像头
# 读取摄像头
# 参数说明：0：默认摄像头
cap = cv.VideoCapture(0)
# 设置像素
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)

# 获取cap的视频帧（帧：每秒多少张图片）
fps = cap.get(cv.CAP_PROP_FPS)
print(fps)
# 循环
while True:
    flag, frame = cap.read()
    # 如果播放不成立的时候，假设不成立
    if not flag:
        break
    face_detect_demo(frame, detector, predictor)

    # 保持画面持续：1
    # 保持静止持续：0
    if ord('q') == cv.waitKey(1):
        break

# 释放内容
cv.destroyAllWindows()
# 释放摄像头
cap.release()
