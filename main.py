import config
import mail

reciever = ['astakhovfilat@gmail.com']

if mail.send_mail(config.smtp.server, config.smtp.port, config.smtp.user, config.smtp.password,
                  config.smtp.sender, reciever, mail.messages['not found']):
    print('Mail sent')
else:
    print('Mail not sent')

