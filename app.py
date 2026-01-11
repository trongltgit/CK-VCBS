import os
from flask import Flask, render_template, request
import pandas as pd
from vnstock3 import Vnstock

app = Flask(__name__)

# Render uses the PORT environment variable. 
# We don't strictly need to define it here if using Gunicorn's -b flag,
# but it's good for local testing compatibility.

@app.route('/')
def index():
    market_summary = {
        "tang": ["VCB", "FPT", "MWG"],
        "giam": ["VIC", "VHM", "GAS"],
        "nhan_dinh": "Thị trường đang có xu hướng hồi phục nhẹ tại nhóm VN30."
    }
    return render_template('index.html', summary=market_summary)

@app.route('/analyze', methods=['POST'])
def analyze():
    symbol = request.form.get('symbol').upper()
    return render_template('index.html', symbol=symbol, show_chart=True)

if __name__ == "__main__":
    # This block is ONLY for running locally via 'python app.py'
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
