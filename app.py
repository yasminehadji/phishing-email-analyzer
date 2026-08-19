from flask import Flask, render_template, request
from analyzer.email_parser import parse_email
from analyzer.detector import analyze_email
from database.database import init_db, save_analysis, get_recent_analyses

app = Flask(__name__)
init_db()

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/analyze")
def analyze():
    f = request.files.get("email_file")
    if not f or not f.filename:
        return render_template("index.html", error="Select an .eml file.")
    if not f.filename.lower().endswith(".eml"):
        return render_template("index.html", error="Only .eml files are accepted.")
    try:
        data = parse_email(f.read())
        result = analyze_email(data)
        save_analysis(data, result)
        return render_template("result.html", email=data, result=result)
    except Exception as exc:
        return render_template("index.html", error=f"Analysis failed: {exc}")

@app.get("/history")
def history():
    return render_template("history.html", analyses=get_recent_analyses())

if __name__ == "__main__":
    app.run(debug=True)
