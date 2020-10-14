# -*- coding: UTF-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models
import base64
import os
import json
import re
import time
 

# 遍历图片
def list_image(images_path):
    fileList = os.listdir(images_path)
    fileList.sort()
    tmp = 1
    for file in fileList:
        if tmp == 1:
            print(file)
            chinese = tencent_OCR(images_path + str(file))
            # rename_image(images_path, file, chinese)
            # time.sleep(1)
            tmp = 0

# 通过文件路径读取图片,返回base64
def get_file_base64(filePath):
    with open(filePath, 'rb') as fp:
        image = fp.read()
        base64_image = str(base64.b64encode(image))
        print(base64_image)
        return base64_image

 # 调用腾讯文字识别
def tencent_OCR(filePath):
    try: 
        cred = credential.Credential("xxxxx", "xxxxx") 
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ocr.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile) 

        req = models.GeneralBasicOCRRequest()
        params = {
            "ImageBase64": get_file_base64(filePath),
            "LanguageType": "zh"
        }
        req.from_json_string(json.dumps(params))

        resp = client.GeneralBasicOCR(req) 
        print(resp.to_json_string()) 

    except TencentCloudSDKException as err: 
        print(err)

# 修改图片文件名
def rename_image(path, oldname, newname):
    Olddir = os.path.join(path, oldname)
    Newdir = os.path.join(path, newname)
    os.rename(Olddir,Newdir)

# 批量通过OCR读取图片文字并改名图片
list_image("mekou/")