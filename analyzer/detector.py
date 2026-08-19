from analyzer.url_analyzer import analyze_url

WORDS = {
    "urgent":8, "immediately":8, "verify":7, "verification":7,
    "password":8, "suspended":10, "suspend":10, "account":4,
    "security alert":8, "click here":8, "login":6, "confirm":5, "payment":5
}
DANGEROUS = (".exe",".scr",".bat",".cmd",".js",".vbs",".ps1",".msi")

def analyze_email(e):
    text = (e.get("subject","") + "\n" + e.get("body","")).lower()
    indicators, score = [], 0

    for word, points in WORDS.items():
        if word in text:
            indicators.append({"severity":"medium","message":f"Suspicious keyword/phrase: '{word}'","points":points})
            score += points

    sender, reply = e.get("sender",""), e.get("reply_to","")
    if sender and reply and sender.split("@")[-1].lower() != reply.split("@")[-1].lower():
        indicators.append({"severity":"high","message":"Reply-To domain differs from sender domain","points":20})
        score += 20

    for url in e.get("urls", []):
        for msg in analyze_url(url):
            pts = 12 if "raw IP" in msg else 8
            indicators.append({"severity":"high" if pts >= 12 else "medium","message":f"{msg}: {url}","points":pts})
            score += pts

    for name in e.get("attachments", []):
        pts = 25 if name.lower().endswith(DANGEROUS) else 3
        sev = "critical" if pts == 25 else "low"
        indicators.append({"severity":sev,"message":f"Attachment detected: {name}","points":pts})
        score += pts

    score = min(score, 100)
    level = "CRITICAL" if score >= 80 else "HIGH" if score >= 60 else "MEDIUM" if score >= 30 else "LOW"
    return {"score":score, "level":level, "indicators":indicators,
            "summary":f"{len(indicators)} suspicious indicator(s) detected." if indicators else "No obvious phishing indicators detected."}
