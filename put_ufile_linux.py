# -*- coding: utf-8 -*-
 
import os
from ucloud.ufile import putufile
from ucloud.compact import b
from ucloud.logger import logger, set_log_file
import ucloud.ufile.config as config
from ucloud.compact import BytesIO
from config import *
 
set_log_file()


def putfile(dir,file):
    # 构造上传对象，并设置公私钥
    handler = putufile.PutUFile(public_key, private_key)
 
    # upload small file to public bucket
    logger.info('start upload file to public bucket')
    # 要上传的目标空间
    bucket = bucketname
    # 上传到目标空间后保存的文件名
    key = file
    # 要上传文件的本地路径
    local_file = dir +'/'+ file
    print(local_file)
    # 请求上传
    ret, resp = handler.putfile(bucket, key, local_file)
    assert resp.status_code == 200
