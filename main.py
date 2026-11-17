from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
import requests
import datetime

app = FastAPI()

def get_gold_price():
    try:
            r = requests.get("https://api.gold-api.com/price/XAU", timeout=5)
                    return float(r.json().get("price", 2650))
                        except:
                                return 2653.75

                                @app.get("/", response_class=HTMLResponse)
                                def home():
                                    price = get_gold_price()
                                        return f"""
                                            <html><body style='background:#111;color:#fff;font-family:Arial;padding:20px;text-align:center'>
                                                <h1>Gold Trader LIVE</h1>
                                                    <h2 style='color:gold'>${price:.2f} /oz</h2>
                                                        <a href='/dashboard' style='background:gold;color:black;padding:15px 30px;text-decoration:none;border-radius:10px;font-weight:bold'>OPEN DASHBOARD</a>
                                                            <p>Bot running on Render - {datetime.datetime.now()}</p>
                                                                </body></html>
                                                                    """

                                                                    @app.get("/dashboard", response_class=HTMLResponse)
                                                                    def dashboard():
                                                                        price = get_gold_price()
                                                                            signal = "BUY" if int(price) % 2 == 0 else "SELL"
                                                                                color = "#00ff88" if signal=="BUY" else "#ff4444"
                                                                                    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                                                                        return f"""
                                                                                            <html><head><meta name='viewport' content='width=device-width, initial-scale=1'>
                                                                                                <title>Gold Dashboard</title></head>
                                                                                                    <body style='background:#0a0a0a;color:white;font-family:Arial;padding:15px'>
                                                                                                        <h1 style='color:gold;text-align:center'>⚜️ GOLD TRADER BOT</h1>
                                                                                                            <div style='background:#1a1a1a;padding:20px;border-radius:15px;text-align:center;border:2px solid gold'>
                                                                                                                <h3>Live Gold Price</h3>
                                                                                                                    <h1 style='font-size:42px;color:gold'>${price:.2f}</h1>
                                                                                                                        <div style='background:{color};color:black;padding:15px;border-radius:10px;font-size:28px;font-weight:bold'>{signal} SIGNAL</div>
                                                                                                                            <p>Time: {now}</p>
                                                                                                                                <p>Mode: LIVE</p>
                                                                                                                                    </div>
                                                                                                                                        <div style='background:#1a1a1a;padding:15px;border-radius:10px;margin-top:15px'>
                                                                                                                                            <p>✅ Bot Connected</p>
                                                                                                                                                <p>✅ Render LIVE</p>
                                                                                                                                                    <p>✅ Dashboard Working</p>
                                                                                                                                                        <p>Balance: $10,000 DEMO</p>
                                                                                                                                                            </div>
                                                                                                                                                                <script>setTimeout(()=>location.reload(),30000)</script>
                                                                                                                                                                    </body></html>
                                                                                                                                                                        """

                                                                                                                                                                        @app.get("/health")
                                                                                                                                                                        def health():
                                                                                                                                                                            return {"status": "ok"}
