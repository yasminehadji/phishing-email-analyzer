# 🛡️ Phishing Email Analyzer

Educational Python cybersecurity project that analyzes `.eml` files for common phishing indicators.

## Features
- Email parsing
- Suspicious keyword detection
- URL analysis
- Reply-To mismatch detection
- Risky attachment detection
- Rule-based 0–100 risk score
- SQLite history
- Flask web interface
- Pytest tests

## Run

```bash
python -m venv .venv
# Windows:
.venv\\Scripts\\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` and upload `sample.eml`.

Run tests:

```bash
pytest
```

## Important
This is a rule-based educational analyzer, not a production mail-security gateway. A low score does not prove an email is safe.

## CV description
**Phishing Email Analyzer — Python / Cybersecurity**  
Developed a Python-based tool for analyzing `.eml` files and detecting phishing indicators using email parsing, URL analysis, social-engineering rules and a transparent risk-scoring system. Added SQLite persistence, Flask interface and automated tests.
