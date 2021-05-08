import numpy as np
from flask import Flask, render_template, Response, jsonify
import picture_recognition as m  # 匿入自定模组
import cv2
import time, datetime
import config
import re
from camera import VideoCamera
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory
from flask_sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["SECRET_KEY"] = 'TPmi4aLWRbyVq8zu9v82dWYW1'
app.config.from_object(config)
db = SQLAlchemy(app)


# 身份信息表
class AllInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image = db.Column(db.String(255))
    code = db.Column(db.String(255))
    indate = db.Column(db.DateTime, default=datetime.datetime.now)

    # 模型的资源序列化函数（方法）
    # 在该函数中所返回的dict的keys，将是我们从test表里所序列化的字段
    def info_schema(self):
        return {
            'id': self.id,
            'image': self.image,
            'code': self.code,
            'indate': self.indate
        }


def create_all():
    db.create_all()


# 测试数据库
@app.route('/db_test')
def db_test():
    create_all()
    # 增加：
    # 现在时间：
    info = AllInfo(image="image2123", code="522734198312270846")
    db.session.add(info)
    db.session.commit()
    return "Hello"


# 查询数据库
@app.route('/get_all_info')
def get_all_info():
    info_list = []
    result = AllInfo.query.all()
    for info_item in result:
        info_list.append(info_item.info_schema())
    return jsonify(info_list)


# 当前实时相机画面
@app.route('/cur_camera')
def cur_camera():
    return render_template('cur_camer.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/uploads_view', methods=['GET', 'POST'])
def upload_file_view():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'photo' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['photo']

        print(file)


        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # 如果文件正常，并且在允许的文件格式范围内：

            print("开始处理图片")
            # FileStorage -> numpy.ndarray
            cv_img = file.read()
            nparr = np.fromstring(cv_img, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)  # Type: numpy.ndarray
            # cv2.imwrite('static/uploads/1.jpg', img)

            print("进行身份证辨识")
            jsondata = m.get_license(img=img)  # 进行身份证辨识
            print('JsonData：', jsondata)
            lines = jsondata['recognitionResult']['lines']

            for i in lines:
                resident_id = re.search('\d{18}|\d{15}', i['text'])
                if resident_id:
                    code = resident_id.group()
                    print('Succeeded 身份证号：', code)
                    # 识别成功后，保存图片
                    millis = int(round(time.time() * 1000))
                    print('时间戳：', millis)
                    filename = str(millis) + '-' + file.filename
                    full_path = 'static/uploads/' + filename + '.jpg'  # 该文件完整路径
                    cv2.imwrite(full_path, img)

                    # 保存信息到数据库
                    info = AllInfo(image='<img onclick="clike_img(this.src)" class="table_in_image" src="../' + full_path + '"alt="">', code=code)
                    db.session.add(info)
                    db.session.commit()

                    # 识别成功，返回 Json 数据
                    final_data = {'status': 'Succeeded', 'code': code}
                    return jsonify(final_data)
            else:
                print('未识别到身份证号码')
                final_data = {'status': 'out', 'code': 0}
                return jsonify(final_data)
    return redirect(request.url)


@app.route('/')
def upload_file():
    return render_template('index.html')


@app.route('/history')
def all_code():
    info_list = []
    result = AllInfo.query.all()
    for info_item in result:
        info_list.append(info_item.info_schema())
    return render_template("history.html", data=jsonify(info_list))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=9000)
