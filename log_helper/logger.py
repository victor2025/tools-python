# -*- encoding: utf-8 -*-
'''
@File    :   logger.py
@Time    :   2022/10/16 14:47:34
@Author  :   victor2022 
@Version :   1.0
@Desc    :   None
'''

import os
import sys
import logging
from logging import handlers

class LoggerFactory:
    # 日志级别关系映射
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }
    
    def __init__(self):
        self.logFileOn=False
        # logger cache
        self._loggerMap = {}

    # write log to file?
    def turnLogFile(self,flag:bool):
        self.logFileOn = flag

    def _get_logger(self, filename, level='info'):
        # 创建日志对象
        log = logging.getLogger(filename)
        # 设置日志级别
        log.setLevel(self.level_relations.get(level))
        # 日志输出格式
        # format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%Y-%m-%d %I:%M:%S %p'
        # fmt = logging.Formatter('%(asctime)s %(thread)d %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        fmt = logging.Formatter(fmt='%(asctime)s | %(filename)s | %(levelname)s | %(message)s',datefmt='%Y-%m-%d %I:%M:%S %p')
        # 输出到控制台
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(fmt)
        # add Handler
        log.addHandler(console_handler)
        # 输出到文件
        if(self.logFileOn):
            # complete file path
            absFilename = ""
            try:
                if os.path.isabs(filename):
                    absFilename = filename
                else:
                    filename = os.environ.get("HOME")+"/.log/"+filename
                    absFilename = os.path.abspath(filename)
                # check and create file
                if not os.path.exists(absFilename):
                    os.makedirs(os.path.dirname(absFilename))
                    os.mknod(absFilename)
            except:
                pass
            # 日志文件按天进行保存，每天一个日志文件
            file_handler = handlers.TimedRotatingFileHandler(filename=filename, when='D', backupCount=1, encoding='utf-8')
            # 按照大小自动分割日志文件，一旦达到指定的大小重新生成文件
            # file_handler = handlers.RotatingFileHandler(filename=filename, maxBytes=1*1024*1024*1024, backupCount=1, encoding='utf-8')
            file_handler.setFormatter(fmt)
            log.addHandler(file_handler)
        return log

    # 明确指定日志输出的文件路径和日志级别
    def getLogger(self, filename = 'python/default.log',level='info')->logging.log:
        logger = None
        try:
            logger = self._loggerMap[filename]
        except:
            logger = self._get_logger(filename, level)
            self._loggerMap[filename] = logger  
        return logger