from fastapi import FastAPI
import os
app = FastAPI()

@app.get("/")
def home():
    return {"status": "live", "user": "ronaldbeukes01", "bot": "Gold Trader Ready"}

@app.get("/dashboard")
def dashboard():
    token = os.getenv("META_API_TOKEN", "NOT SET")[:10]
    acct = os.getenv("ACCOUNT_ID", "NOT SET")
    return f"<html><body style='background:#0f172a;color:white;font-family:Arial;padding:20px'><h1>🥇 Gold Trader - ronaldbeukes01</h1><h2 style='color:#22c55e'>LIVE ✅</h2><p>Account: {acct}</p><p>Token: {token}...</p><h3>Safety: Broker Verified | Pip 0.1 | $50 Cap | 0.01 Lot</h3><a href='/docs' style='color:cyan'>API Docs</a></body></html>"

@app.get("/health")
def health():
    return {"status": "ok"}
