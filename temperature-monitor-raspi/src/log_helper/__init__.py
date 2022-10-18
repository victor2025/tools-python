from .logger import LoggerFactory
from handlers import temperLoader
factory = LoggerFactory()
factory.turnLogFile(temperLoader.log_file)
# create logger
log = factory.getLogger(filename = temperLoader.log_path,level='info')