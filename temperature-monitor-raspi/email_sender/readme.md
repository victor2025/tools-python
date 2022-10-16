# Email Sender based on Python

### Environment
- python3.7
- smtplib

### Usage
- Complete configure files: sender.conf receiver.conf in `default-configs/`.
- Create mailSender from handlers.mailHandler by `getMailSender(configpath)`.
- Send mail with mailSender by `sendMail(content,...)`，the receiver's addresses will be read from receiver.conf if this parameter is not specified.
- Logs will be printed out and saved to $HOME/.log/python/email-sender.log. If you want to write log to logfile, please call `loghelper.logger.turnLogFile(True)` at first.