from . import *

# Answer key for data_4
# True = arbitrageable (EQUIVALENT or NEGATION)
# False = not arbitrageable
data_answers["4"] = [
    # 1-15: Clear EQUIVALENT cases
    True,   # 1: Bitcoin end of 2025, EQUIVALENT
    True,   # 2: Ethereum end of 2025, EQUIVALENT
    True,   # 3: Chiefs vs 49ers Super Bowl, EQUIVALENT
    True,   # 4: Manhattan = NYC snow, EQUIVALENT
    True,   # 5: Lakers sweep = win all 4 games, EQUIVALENT
    True,   # 6: AMD Q2 close = end of Q2, NEGATION
    True,   # 7: Starship landing Q1, EQUIVALENT
    True,   # 8: GDP growth Q1, EQUIVALENT
    True,   # 9: Unemployment end of 2025, NEGATION
    True,   # 10: Gold end of 2025, EQUIVALENT
    True,   # 11: iPhone release = announcement, EQUIVALENT
    True,   # 12: Celtics vs Heat, EQUIVALENT
    True,   # 13: Tesla Q2 close = end of Q2, NEGATION
    True,   # 14: S&P 500 end of 2025, EQUIVALENT
    True,   # 15: Yankees sweep = beat in all 3 games, EQUIVALENT

    # 16-30: Clear NEGATION cases
    True,   # 16: Bitcoin end of 2025, NEGATION
    True,   # 17: Fed rates Q2, NEGATION
    True,   # 18: Inflation June 2025, NEGATION
    True,   # 19: Oil prices 2025, NEGATION
    True,   # 20: Apple Q1 2025, NEGATION
    True,   # 21: Unemployment 2025, NEGATION
    True,   # 22: Google end of 2025, NEGATION
    True,   # 23: GDP Q3 2025, NEGATION
    True,   # 24: Home prices 2025, NEGATION
    True,   # 25: EUR/USD H1 2025, NEGATION
    True,   # 26: Nvidia end of 2025, NEGATION
    True,   # 27: Gold H1 2025, NEGATION
    True,   # 28: Market correction 2025, NEGATION
    True,   # 29: Bitcoin H1 2025, NEGATION
    True,   # 30: Microsoft Q2 2025, NEGATION

    # 31-40: Clear SUBSET cases
    False,  # 31: LeBron ⊂ NBA player, SUBSET
    False,  # 32: GPT-5 ⊂ new OpenAI model, SUBSET
    False,  # 33: iPhone 17 ⊂ new Apple product, SUBSET
    False,  # 34: Cybertruck Gen 2 ⊂ new Tesla vehicle, SUBSET
    False,  # 35: Taylor Swift ⊂ woman, SUBSET
    False,  # 36: Amazon/Whole Foods ⊂ major grocery acquisition, SUBSET/UNRELATED
    False,  # 37: Starship ⊂ any rocket, SUBSET
    False,  # 38: ChatGPT ⊂ AI chatbot, SUBSET
    False,  # 39: Elon Musk ⊂ tech CEO, SUBSET
    False,  # 40: Yankees ⊂ AL East team, SUBSET

    # 41-50: Clear UNRELATED cases
    False,  # 41: London rain vs Bitcoin, UNRELATED
    False,  # 42: Lakers playoffs vs Tesla stock split, UNRELATED
    False,  # 43: Government shutdown vs Apple VR, UNRELATED
    False,  # 44: Super Bowl vs SpaceX Mars, UNRELATED
    False,  # 45: Q2 recession vs Q3 oil prices, UNRELATED/UNCERTAIN
    False,  # 46: Fed vs ECB (different central banks), UNRELATED
    False,  # 47: Amazon stock vs Google stock, UNRELATED
    False,  # 48: Boston snow vs Celtics game, UNRELATED
    False,  # 49: Yankees AL East vs Dodgers NL West, UNRELATED
    False,  # 50: Unemployment vs inflation (related but not arbitrageable), UNRELATED
]
