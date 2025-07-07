
def calculate_value_bets(bets):
    filtered = []
    for b in bets:
        value_percent = (b['odds'] / b['estimated_prob'] - 1) * 100
        if value_percent > 3:
            filtered.append(f"📢 Value Bet\nPartita: {b['match']}\nMercato: {b['market']}\nQuota: {b['odds']}\nProbabilità stimata: {b['estimated_prob']}\nValue stimato: +{round(value_percent,1)}%\nBookmaker: {b['bookmaker']}")
    return filtered
