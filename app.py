from flask import Flask, render_template, request
import pandas as pd
# Sử dụng thư viện vnstock2 để lấy dữ liệu chứng khoán
from vnstock3 import Vnstock

app = Flask(__name__)

@app.route('/')
def index():
    # Chức năng 1 & 2: Hiển thị bảng giá và tóm tắt
    # Ở đây chúng ta sẽ giả lập dữ liệu tóm tắt hoặc gọi từ API
    market_summary = {
        "tang": ["VCB", "FPT", "MWG"],
        "giam": ["VIC", "VHM", "GAS"],
        "nhan_dinh": "Thị trường đang có xu hướng hồi phục nhẹ tại nhóm VN30."
    }
    return render_template('index.html', summary=market_summary)

@app.route('/analyze', methods=['POST'])
def analyze():
    symbol = request.form.get('symbol').upper()
    # Chức năng 3: Phân tích mã (Gửi mã sang TradingView Widget để hiển thị đồ thị)
    return render_template('index.html', symbol=symbol, show_chart=True)

if __name__ == '__main__':
    app.run(debug=True)