import requests
import cv2
import time
import re

base = 'https://homework.cognitiveservices.azure.com/vision/v2.0'
recog_url = f'{base}/recognizeText?mode=Printed'  # 辨识请求路径#
key = '27dc2ad8406d414f8bfde08489b8b968'  # 秘钥#
headers = {'Ocp-Apim-Subscription-Key': key}
headers_stream = {'Ocp-Apim-Subscription-Key': key,
                  'Content-Type': 'application/octet-stream'}


def get_license(img):  # 建立自定义函数#
    img_encode = cv2.imencode('.jpg', img)[1]
    img_bytes = img_encode.tobytes()
    r1 = requests.post(recog_url,  # 发出post#
                       headers=headers_stream,
                       data=img_bytes)
    if r1.status_code != 202:  # 202 代表接受请求#
        print(r1.json())
        return '请求失败'

    result_url = r1.headers['Operation-Location']  # 查看结果的请求路径
    r2 = requests.get(result_url, headers=headers)  # get请求
    # print(r2.json())
    # 这里可以不需要写，如果考虑错误重试机制可改用递归
    # while r2.status_code == 200 and r2.json()['status'] != 'Succeeded':
    #     r2 = requests.get(result_url,headers = headers)             #继续get请求
    # print('status: ', r2.json()['status'])  # 显示辨识状态

    #
    # lines = r2.json()['recognitionResult']['lines']
    # for i in lines:
    #     resident_id = re.search('\d{18}|\d{15}', i['text'])
    #     if resident_id: return resident_id.group()
    return r2.json()


# try:
#     img = cv2.imread('shot.jpg')  # 读取图片
#     print('status: Start')
#     text = get_license(img)  # 辨识图片中的身份证号
#     print('身份证号:', text)
#     cv2.imshow('Frame', img)  # 显示图片
#     cv2.waitKey(0)  # 等待
#     cv2.destroyAllWindows()  # 关闭视窗
# except Exception as e:
#     print(e)
#     print('读取图片失败')
