from email import policy
from email.parser import BytesParser
from email.utils import parseaddr
import re

URL_RE = re.compile(r"https?://[^\s<>\"]+", re.I)

def parse_email(raw):
    msg = BytesParser(policy=policy.default).parsebytes(raw)
    sender_name, sender = parseaddr(msg.get("From", ""))
    reply_name, reply_to = parseaddr(msg.get("Reply-To", ""))
    parts, attachments = [], []

    if msg.is_multipart():
        for part in msg.walk():
            if part.get_filename():
                attachments.append(part.get_filename())
                continue
            if part.get_content_type() in ("text/plain", "text/html"):
                try:
                    parts.append(part.get_content())
                except Exception:
                    pass
    else:
        try:
            parts.append(msg.get_content())
        except Exception:
            pass

    body = "\n".join(parts)
    urls = [u.rstrip(".,;:!?)]}>'\"") for u in URL_RE.findall(body)]
    return {
        "sender_name": sender_name, "sender": sender,
        "reply_name": reply_name, "reply_to": reply_to,
        "recipient": msg.get("To", ""), "subject": msg.get("Subject", ""),
        "date": msg.get("Date", ""), "body": body,
        "urls": urls, "attachments": attachments
    }
