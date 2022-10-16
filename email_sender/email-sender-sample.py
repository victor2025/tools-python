import sys
from handlers import mailHander
# create mail sender
sender = mailHander.getMailSender(sys.path[0])
# send email
# sender.sendMail(content="test-01",toaddrs=["1045899571@qq.com"])
# send email (load toaddrs from config file)
# sender.sendMail(content="test-02",subject="TEST-02")