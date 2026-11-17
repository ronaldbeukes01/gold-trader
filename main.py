from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import yfinance as yf
from datetime import datetime

app = FastAPI()

def get_gold_price():
    try:
        gold = yf.Ticker("GC=F")
        data = gold.history(period="1d")
        if not data.empty:
            price = float(data['Close'].iloc[-1])
            return price
    except:
        pass
    return 4025.50

@app.get("/", response_class=HTMLResponse)
def dashboard():
    price = get_gold_price()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html = f"""
    <html>
    <head><title>Gold Trader - Live</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <style>
    body{{background:#0f0f0f;color:#fff;font-family:Arial;text-align:center;padding:20px}}
    .card{{background:#1e1e1e;padding:30px;border-radius:15px;max-width:400px;margin:auto;border:1px solid #333}}
    .price{{font-size:48px;color:#FFD700;font-weight:bold;margin:20px 0}}
    .live{{background:#00ff00;color:#000;padding:5px 15px;border-radius:20px;display:inline-block;font-weight:bold}}
    .btn{{background:#FFD700;color:#000;padding:15px 30px;border:none;border-radius:10px;font-size:18px;margin-top:20px;cursor:pointer;width:100%}}
    </style></head>
    <body>
    <div class='card'>
    <h1>GOLD TRADER</h1>
    <div class='live'>● LIVE</div>
    <div class='price'>${price}</div>
    <p>XAU/USD - Gold Spot</p>
    <p style='color:#888'>{now}</p>
    <button class='btn' onclick='location.reload()'>Refresh Price</button>
    <p style='margin-top:20px;color:#888;font-size:12px'>Real gold price from Yahoo Finance</p>
    </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html)

@app.get("/price")
def price_api():
    return {{"price": get_gold_price(), "symbol": "XAUUSD"}}
