
def find_surebets(config):
    max_bet = config.get("max_bet", 400)
    surebets = []

    # 模擬兩隊賠率
    team1 = {"name": "Hisamitsu", "odds": 2.4}
    team2 = {"name": "NEC", "odds": 2.45}
    match_time = "2025-07-14 21:21"
    sport = "🏐 排球 日本女排"
    venue = "Hisamitsu vs NEC"

    # 計算下注金額
    inv_team1 = 1 / team1["odds"]
    inv_team2 = 1 / team2["odds"]
    total_inv = inv_team1 + inv_team2

    stake_team1 = round(max_bet * inv_team1 / total_inv, 2)
    stake_team2 = round(max_bet * inv_team2 / total_inv, 2)
    total_stake = stake_team1 + stake_team2

    payout_team1 = stake_team1 * team1["odds"]
    payout_team2 = stake_team2 * team2["odds"]
    guaranteed_payout = min(payout_team1, payout_team2)
    profit = round(guaranteed_payout - total_stake, 2)
    roi = round((profit / total_stake) * 100, 2)

    if roi >= 10:  # 只推播 10% 以上套利機會
        surebets.append({
            "sport": sport,
            "venue": venue,
            "match_time": match_time,
            "bets": [
                {"team": team1["name"], "odds": team1["odds"], "stake": stake_team1},
                {"team": team2["name"], "odds": team2["odds"], "stake": stake_team2},
            ],
            "roi": roi,
            "profit": profit
        })

    return surebets
