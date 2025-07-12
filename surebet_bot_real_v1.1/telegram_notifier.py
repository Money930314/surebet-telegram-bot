
import requests
from config import get_config

def send_message(surebet):
    config = get_config()
    token = config["telegram_token"]
    chat_id = config["chat_id"]

    bets_info = "\n".join([
        f"- {b['team']} @ {b['odds']} → 下注 ${b['stake']}" for b in surebet["bets"]
    ])

    message = f"""
{surebet['sport']}
🏟️ {surebet['venue']}
🕒 開賽時間：{surebet['match_time']}
📈 套利機會：
{bets_info}
💰 預估利潤：${surebet['profit']}（{surebet['roi']}%）
✅ 請盡快下單套利！
"""

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message.strip()}
    requests.post(url, data=data)
