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

# parse configure file 
def parse(basepath, filename) -> ConfigParser:
    print("Loading Configurations from {}...".format(filename))
    parser = ConfigParser()
    filepath = os.path.join(os.path.abspath(basepath), filename)
    # 判断文件是否存在
    if not os.path.exists(filepath):
        raise Exception("Configure file not exist {} !!!".format(filename))
    # 读取配置
    parser.read(filepath)
    return parser

# load sender config
class TemperLoader:

    def __init__(self, basepath, filename = "temper.conf"):
        # 设置属性
        self.config_path = basepath
        self.level_warn = 60.0
        self.level_reboot = 90.0
        # log
        self.log_file = False
        self.log_path = "/var/log/temper-monitor.log"
        # other param
        self.peroid = 2
        self.mode = "base"
        # 调用函数读取配置文件
        self._readConfig(basepath,filename)
        # 配置读取完成
        print("Configure load completed...")

    def _readConfig(self, basepath, filename):
        # 初始化
        parser = parse(basepath,filename)
        # 开始逐个读取
        try:
            # read warn temperature
            tempWarn = parser.getfloat("level","warn")
            if(tempWarn<=0):
                print("Warn temperature is too low, use default!")
            else:
                self.level_warn = tempWarn
            # read reboot temperature
            tempReboot = parser.getfloat("level","reboot")
            if(tempReboot<=0):
                print("Reboot temperature is too low, use default!")
            else:
                self.level_reboot = tempReboot
            # read log conf
            if(parser.has_option("global","log_file")):
                self.log_file = parser.getboolean("global","log_file")
            if(parser.has_option("global","log_path")):
                self.log_path = parser.get("global","log_path")
            # read other params
            if(parser.has_option("global","peroid")):
                self.peroid = parser.getint("global","peroid")
            if(parser.has_option("global","mode")):
                self.mode = parser.get("global","mode")
        except:
            raise Exception("There are some error in the configure file: {} !!!".format(filename))