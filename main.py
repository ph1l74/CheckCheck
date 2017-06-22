import config
import mail
import os


files = mail.get_last_attachment(config.IMAP.server, config.IMAP.user, config.IMAP.password)

print("Files in letter: ")
for file in files:
    print("    {}".format(file[0]))

