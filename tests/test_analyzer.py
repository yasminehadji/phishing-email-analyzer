from analyzer.detector import analyze_email

def base():
    return {"sender":"a@example.com","reply_to":"a@example.com","subject":"Hello","body":"Normal message","urls":[],"attachments":[]}

def test_normal_is_low():
    assert analyze_email(base())["level"] == "LOW"

def test_phishing_scores_higher():
    e=base(); e["subject"]="URGENT verify your password"; e["body"]="Click here to login immediately"
    assert analyze_email(e)["score"] >= 30

def test_reply_mismatch():
    e=base(); e["reply_to"]="evil@example.net"
    assert any("Reply-To" in x["message"] for x in analyze_email(e)["indicators"])

def test_dangerous_attachment():
    e=base(); e["attachments"]=["invoice.exe"]
    assert any("Attachment" in x["message"] for x in analyze_email(e)["indicators"])
