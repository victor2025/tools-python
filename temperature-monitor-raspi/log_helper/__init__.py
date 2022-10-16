from .logger import LoggerFactory
factory = LoggerFactory()
factory.turnLogFile(True)
# create logger
log = factory.getLogger(filename = 'python/temper-monitor.log',level='info')