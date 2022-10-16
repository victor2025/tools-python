import os
import sys
from datetime import datetime
import time


print(os.path.abspath(__file__))
print(sys.path[0])
def getRootPath():
    # 获取文件目录
    curPath = os.path.abspath(os.path.dirname(__file__))
    # 获取项目根路径，内容为当前项目的名字
    rootPath = curPath[:curPath.find("temperature-monitor")+len("temperature-monitor")]
    return  rootPath
print(getRootPath())