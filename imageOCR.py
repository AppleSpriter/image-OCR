# -*- coding: UTF-8 -*-
from aip import AipOcr
import os
import re
import time
 
# 定义常量
APP_ID = '11111111'
API_KEY = 'xxxxxx'
SECRET_KEY = 'xxxxxx'
global_number = 0

# 初始化AipFace对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 遍历图片
def list_image(images_path):
    fileList = os.listdir(images_path)
    fileList.sort()
    for file in fileList:
        chinese = baiduOCR(images_path + str(file))
        rename_image(images_path, file, chinese, file)
        time.sleep(1)

# 通过文件路径读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
 
# 调用百度文字识别
def baiduOCR(filePath):
    # 定义参数变量
    options = {
        'detect_direction': 'true',
        'language_type': 'CHN_ENG',
        'probability': 'true',
    } 
    # 调用通用文字识别接口
    # result = aipOcr.basicGeneral(get_file_content(filePath), options)
    # 调用高精度文字识别接口
    result = aipOcr.basicAccurate(get_file_content(filePath), options)
    chinese = ""
    # print(result)
    words_result=result['words_result']
    for i in range(len(words_result)):
        # print(words_result[i]['words'])
        chinese += words_result[i]['words']
    global global_number
    global_number += 1
    # 去除特殊符号
    chinese = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])","",chinese)
    # 输出到控制台查看进度
    print(str(global_number) + " : " + chinese)

    return chinese + ".jpg"

# 修改图片文件名
def rename_image(path, oldname, newname, mark):
    Olddir = os.path.join(path, oldname)
    Newdir = os.path.join(path, newname)
    # 解决重命名冲突
    try:
        os.rename(Olddir, Newdir)
    except Exception as e:
        # 重命名标识
        if e.args[0] ==17: 
            fname, fename = os.path.splitext(Newdir)
            rename_number = os.path.splitext(mark)[0]
            os.rename(Olddir, fname + rename_number + fename)


# 批量通过OCR读取图片文字并改名图片
list_image("image/")