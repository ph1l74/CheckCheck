import config
import mail
import os


files = mail.get_last_attachment(config.server, config.user, config.password)

print("Files in letter: ")
for file in files:
    print("    {}".format(file[0]))

