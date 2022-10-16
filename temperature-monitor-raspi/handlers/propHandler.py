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
class TemperLoader:

    def __init__(self, basepath, filename = "temper.conf"):
        # 设置属性
        self.level_warn = 60.0
        self.level_reboot = 90.0
        # 调用函数读取配置文件
        self._readConfig(basepath,filename)
        # 配置读取完成
        log.info("Configure load completed...")

    def _readConfig(self, basepath, filename):
        # 初始化
        parser = parse(basepath,filename)
        group = 'level'
        # 开始逐个读取
        try:
            # read warn temperature
            tempWarn = float(parser.get(group,"warn"))
            if(tempWarn<=0):
                log.info("Warn temperature is too low, use default!")
            else:
                self.level_warn = tempWarn
            # read reboot temperature
            tempReboot = float(parser.get(group,"reboot"))
            if(tempReboot<=0):
                log.info("Reboot temperature is too low, use default!")
            else:
                self.level_reboot = tempReboot
        except:
            raise Exception("There are some error in the configure file: {} !!!".format(filename))