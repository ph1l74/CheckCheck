import os
import collections

_Imap = collections.namedtuple('_Imap', ['server', 'user', 'password'])
_Smtp = collections.namedtuple('_Smtp', ['server', 'port', 'sender'])

imap = _Imap(server=os.environ['IMAP_HOST'],
             user=os.environ['IMAP_USER'],
             password=os.environ['IMAP_PASSWORD'])

smtp = _Smtp (server = os.environ['SMTP_HOST'],
              port = os.environ['SMTP_PORT'],
              sender = os.environ['SMTP_SENDER'])
