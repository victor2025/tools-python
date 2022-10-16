# -*- encoding: utf-8 -*-
'''
@File    :   tempMonitorMain.py
@Time    :   2022/10/16 16:59:35
@Author  :   victor2022 
@Version :   1.0
@Desc    :   main function of temperature-monitor
'''

from temperMonitor import TemperMonitor

def main():
    # create monitor
    monitor = TemperMonitor("email")
    # start
    monitor.startMonitor()

if __name__=="__main__":
    main()