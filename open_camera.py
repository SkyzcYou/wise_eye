import picture_recognition as m   #匿入自定模组
import cv2


capture = cv2.VideoCapture(0)   #建立摄影机物件
if capture.isOpened():
    while True:
     sucess, img = capture.read()   #读取影像
     if sucess:
         cv2.imshow('Frame',img)     #显示影像
     k = cv2.waitKey(100)      #等待按键输入
     if k == ord('s') or k == ord('S'):  #按下s键
         # cv2.imwrite('shot.jpg', img)    #储存影像
         text = m.get_license(img)    #进行身份证辨识
         print('身份证号：',text)

     if k == ord('q') or k == ord('Q'):  #按下q键结束
         print('exit')
         cv2.destroyAllWindows()   #关闭视窗
         capture.release()   #关闭摄影机
         break
else:
     print('开启摄q影机失败')