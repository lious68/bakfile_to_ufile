#-*- coding:utf-8 -*-

import os,time,sys,datetime
import put_ufile
from config import *


def localFile(base_path):
	for path,dirs,files in os.walk(base_path):
		for f in files:
			FileTimestamp = os.path.getmtime(path + r'\{}'.format(f))
			#fileTime = datetime.datetime.fromtimestamp(FileTimestamp).strftime('%Y-%m-%d')
			curtime = time.time()
			times = (curtime - FileTimestamp)/60/60/24 #备份时长，如果是要备份1个小时的，则/60/60/24/24.

			if times >= 1:
				try:
					put_ufile.putfile(path,f) #调用putufile函数，上传到UFILE。
					print(path,f)
				except Exception as e:
					print(e)
			else:
				print('no file is far')




if __name__ == '__main__':
	localFile(dirs)