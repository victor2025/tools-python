# -*- encoding: utf-8 -*-
'''
@File    :   propLoader
@Time    :   2022/10/16 00:40:31
@Author  :   victor2022 
@Version :   1.0
@Desc    :   config loader
'''
from configparser import ConfigParser
import os
from log_helper import log

# logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%Y-%m-%d %I:%M:%S %p')
# parse configure file 
def parse(basepath, filename) -> ConfigParser:
    log.info("Loading Configurations from {}...".format(filename))
    parser = ConfigParser()
    filepath = os.path.join(os.path.abspath(basepath), filename)
    # 判断文件是否存在
    if not os.path.exists(filepath):
        raise Exception("Configure file not exist {} !!!".format(filename))
    # 读取配置
    parser.read(filepath)
    return parser

# load sender config
class SenderLoader:

    def __init__(self, basepath = ".", filename = "email-sender.conf"):
        # 设置属性
        self.host = ""
        self.port = 0
        self.username = ""
        self.password = ""
        self.fromaddr = ""
        # 调用函数读取配置文件
        self._readConfig(basepath,filename)
        # 配置读取完成
        log.info("Configure load completed...")

    def _readConfig(self, basepath, filename):
        # 初始化
        parser = parse(basepath,filename)
        group = 'global'
        # 开始逐个读取
        try:
            self.host = parser.get(group,"host")
            self.port = parser.get(group,"port")
            self.username = parser.get(group,"username")
            self.password = parser.get(group,"password")
            self.fromaddr = parser.get(group,"fromaddr")
        except:
            raise Exception("There are some error in the configure file: {} !!!".format(filename))

# load receiver config
class ReceiverLoader:
    def __init__(self, basepath = ".", filename = "email-receiver.conf"):
        # 设置属性
        self.toaddrs = []
        # 调用函数读取配置文件
        self._readConfig(basepath,filename)
        # 配置读取完成
        log.info("Configure load completed...")

    def _readConfig(self, basepath, filename):
        # 初始化
        parser = parse(basepath,filename)
        group = 'global'
        # 开始逐个读取
        try:
            addrStr = parser.get(group,"toaddrs")
            self.toaddrs = addrStr.split(",")
        except:
            raise Exception("There are some error in the configure file: {} !!!".format(filename))