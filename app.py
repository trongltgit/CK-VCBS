import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Only import heavy stuff when the route is actually called
    # Or keep this simple so the app boots fast
    market_summary = {
        "tang": ["VCB", "FPT", "MWG"],
        "giam": ["VIC", "VHM", "GAS"],
        "nhan_dinh": "Thị trường đang có xu hướng hồi phục nhẹ tại nhóm VN30."
    }
    return render_template('index.html', summary=market_summary)

@app.route('/analyze', methods=['POST'])
def analyze():
    # Import here to delay loading until needed
    import pandas as pd
    from vnstock3 import Vnstock
    
    symbol = request.form.get('symbol').upper()
    return render_template('index.html', symbol=symbol, show_chart=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
