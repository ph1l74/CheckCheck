import os
import collections

_IMAP = collections.namedtuple('_IMAP', ['server', 'user', 'password'])
_SMTP = collections.namedtuple('_SMTP', ['server', 'port', 'user', 'password', 'sender'])

imap = _IMAP(server=os.environ['IMAP_HOST'],
             user=os.environ['IMAP_USER'],
             password=os.environ['IMAP_PASSWORD'])

smtp = _SMTP(server=os.environ['SMTP_HOST'],
             port=os.environ['SMTP_PORT'],
             user=os.environ['SMTP_USER'],
             password=os.environ['SMTP_PASSWORD'],
             sender=os.environ['SMTP_SENDER'])
