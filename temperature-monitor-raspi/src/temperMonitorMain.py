# -*- encoding: utf-8 -*-
'''
@File    :   tempMonitorMain.py
@Time    :   2022/10/16 16:59:35
@Author  :   victor2022 
@Version :   1.0
@Desc    :   main function of temperature-monitor
'''

from temperMonitor import TemperMonitor
from handlers.propHandler import TemperLoader
from handlers import temperLoader

def main():
    # create monitor
    monitor = TemperMonitor(temperLoader.mode,temperLoader.peroid)
    # start
    monitor.startMonitor()

if __name__=="__main__":
    main()