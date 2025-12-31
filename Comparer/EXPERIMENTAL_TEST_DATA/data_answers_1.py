from . import *

data_answers["1"] = [
    # 1-10
    True,   # 1: Tesla $300 Q2 equivalent
    True,   # 2: Snow on Christmas equivalent
    True,   # 3: Yankees vs Red Sox July 4 equivalent
    True,   # 4: Unemployment 4% equivalent
    True,   # 5: Dow 40k equivalent
    True,   # 6: Amazon NEGATION (above $200 vs at/below $200)
    True,   # 7: Fed rates NEGATION (raise vs keep/lower)
    False,  # 8: Cat 5 ⊂ any hurricane (SUBSET)
    False,  # 9: Overturn Roe ⊂ any major ruling (SUBSET)
    False,  # 10: $500 ⊂ going up (OVERLAP)
    
    # 11-20
    False,  # 11: Tom Brady ⊂ any retired QB (SUBSET)
    False,  # 12: ChatGPT ⊂ any AI chatbot (SUBSET)
    False,  # 13: Q1 ≠ Q2 (different time windows)
    False,  # 14: Jan 1 ≠ Dec 31 (different dates)
    False,  # 15: Jan inflation ≠ Dec inflation (different times)
    False,  # 16: $2000 ≠ $2100 (different thresholds)
    False,  # 17: 90°F ≠ 95°F (different thresholds)
    False,  # 18: $500 ≠ $600 (different thresholds)
    False,  # 19: Recession ≠ unemployment 5% (OVERLAP)
    False,  # 20: Democrat wins ≠ Biden runs (OVERLAP)

    # 21-30
    False,  # 21: VR headset ≠ stock ATH (OVERLAP)
    False,  # 22: London rain ≠ Bitcoin (UNRELATED)
    False,  # 23: Lakers playoffs ≠ Tesla split (UNRELATED)
    False,  # 24: Unspecified year ≠ 2026 (UNCERTAIN)
    False,  # 25: "this year" ≠ 2025 (UNCERTAIN - depends on when asked)
    True,   # 26: Microsoft acquire Activision = deal close
    True,   # 27: COVID vaccine mandate equivalent
    True,   # 28: Fed cut rates H1 2025 = lower before July
    False,  # 29: 3-way outcome ≠ binary (incompatible outcomes)
    False,  # 30: Next Fed chair ≠ Powell remains (different questions)

    # 31-40
    False,  # 31: Moneyline ≠ spread (different bet types)
    False,  # 32: Winner ≠ cover spread (different outcomes)
    True,   # 33: NYC = Manhattan (for practical purposes, close enough)
    False,  # 34: Phoenix ⊂ Arizona (SUBSET - could snow in Flagstaff)
    True,   # 35: Ethereum $3000 equivalent (comma formatting)
    True,   # 36: Oil $85/barrel equivalent
    False,  # 37: Biden nominee ⊂ incumbent runs (SUBSET)
    False,  # 38: Newsom ⊂ any CA governor (SUBSET)
    False,  # 39: GDP 3% ⊂ expansion (SUBSET - could expand <3%)
    False,  # 40: CPI ≠ PCE (different inflation measures)

    # 41-50
    False,  # 41: GPT-5 ⊂ any new model (SUBSET)
    False,  # 42: iPhone 17 Sept ⊂ new iPhone fall (SUBSET - Sept ⊂ fall)
    False,  # 43: 2" rain ≠ "heavy" (subjective definition)
    False,  # 44: 50mph ⊂ tropical storm conditions (SUBSET)
    True,   # 45: Midnight UTC Jan 1 = start of 2025 equivalent
    True,   # 46: Tesla close Dec 31 = end of 2024 equivalent
    False,  # 47: Game 1 ≠ series winner (SUBSET)
    True,   # 48: Sweep 3-game = win all games this weekend (equivalent)
    True,   # 49: Exact same question (obvious EQUIVALENT)
    True,   # 50: Gold $2200 equivalent (formatting)
]