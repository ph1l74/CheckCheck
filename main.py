import config
import mail

recievers = ['astakhovfilat@gmail.com']

mail.send_mail(config.smtp.server, config.smtp.port, config.smtp.user, config.smtp.password,
                  config.smtp.sender, recievers, mail.messages['not found'])
