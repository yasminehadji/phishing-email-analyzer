from urllib.parse import urlparse
import re

SHORTENERS = {"bit.ly","tinyurl.com","t.co","goo.gl","ow.ly","is.gd"}
RISKY_TLDS = (".xyz",".top",".click",".zip",".mov",".work",".gq",".tk")
IP_RE = re.compile(r"^(?:\d{1,3}\.){3}\d{1,3}$")

def analyze_url(url):
    p = urlparse(url)
    domain = p.netloc.lower().split("@")[-1].split(":")[0]
    found = []
    if p.scheme != "https": found.append("URL does not use HTTPS")
    if IP_RE.match(domain): found.append("URL uses a raw IP address")
    if domain in SHORTENERS: found.append("URL uses a known URL shortener")
    if domain.endswith(RISKY_TLDS): found.append("Domain uses a higher-risk TLD")
    if "@" in p.netloc: found.append("URL contains an @ symbol")
    if any(x in p.path.lower() for x in ("login","verify","password","signin","account")):
        found.append("URL path suggests credential/account activity")
    if re.search(r"\d", domain):
        found.append("Domain contains digits")
    return found
