import config
import mail
import ocr
import db


def check(count=1):

    # get attachments from number of files
    attachments = mail.get_attachments(config.imap, count)
    recognized_text = []
    if attachments:
        for attachment in attachments:
            # get sender and batch of files
            sender = attachment[0][0]
            files =  attachment[1]
            print("Checking letter from {}. Number of attachments: {}".format(sender, len(files)))
            if files:
                for file in files:
                    text = ocr.image_to_text(file)
                    recognized_text.append(text)
            else:
                mail.send_mail(config.smtp, sender, mail.messages['not found'])
                print("No files in mail. Email sent to {}". format(sender))

            if len(recognized_text) == len(files):
                for text in recognized_text:
                    # new_reciept = db.Reciept()
                    # new_reciept.id = text
                    # new_reciept.add()
                    print("Got some text:\n{}".format(text))
            else:
                mail.send_mail(config.smtp, sender, mail.messages['undefined'])
    else:
        print("No mails")

check()