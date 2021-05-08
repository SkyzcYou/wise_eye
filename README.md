## Start
1. 安装 venv 虚拟环境，并进入
```shell
python -m venv venv
```

```shell
# 进入虚拟环境
# windows 下，项目根目录执行
.\venv\Scripts\activate.bat
```
2. 安装所需库
```shell
pip install -r requirements.txt 
```
3. 创建数据库，并修改项目配置

    在自己 MySQL 下新建一个数据库
    并将项目根目录 `config.py` 的配置改为自己的配置
   
4. 运行：
```shell
flask run
```
然后访问：[127.0.0.1:5000](127.0.0.1:5000)
## 其他备注

外部访问参数：
```xml
--host=0.0.0.0 --port=9000
```

安装`cv2`:
```shell
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python
```