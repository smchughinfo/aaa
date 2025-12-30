from . import *

data_answers["1"] = [
    # 1-10 (original)
    False,  # 1: Mars ⊂ Space (SUBSET)
    True,   # 2: Bitcoin $100k equivalent
    False,  # 3: Championship ≠ Finals (different outcomes)
    True,   # 4: Rain = Precipitation
    False,  # 5: Trump ⊂ Republican (SUBSET)
    True,   # 6: EUR/USD 1.10 equivalent
    False,  # 7: iPhone ⊂ any product (SUBSET)
    False,  # 8: Week 17 ≠ Dec 25 (can't verify same game)
    False,  # 9: Oil ≠ Gas prices (correlated but different)
    False,  # 10: Starship ⊂ any rocket (SUBSET)
    
    # 11-20
    True,   # 11: Tesla $300 Q2 equivalent
    True,   # 12: Snow on Christmas equivalent
    True,   # 13: Yankees vs Red Sox July 4 equivalent
    True,   # 14: Unemployment 4% equivalent
    True,   # 15: Dow 40k equivalent
    True,   # 16: Amazon NEGATION (above $200 vs at/below $200)
    True,   # 17: Fed rates NEGATION (raise vs keep/lower)
    False,  # 18: Cat 5 ⊂ any hurricane (SUBSET)
    False,  # 19: Overturn Roe ⊂ any major ruling (SUBSET)
    False,  # 20: $500 ⊂ going up (OVERLAP)
    
    # 21-30
    False,  # 21: Tom Brady ⊂ any retired QB (SUBSET)
    False,  # 22: ChatGPT ⊂ any AI chatbot (SUBSET)
    False,  # 23: Q1 ≠ Q2 (different time windows)
    False,  # 24: Jan 1 ≠ Dec 31 (different dates)
    False,  # 25: Jan inflation ≠ Dec inflation (different times)
    False,  # 26: $2000 ≠ $2100 (different thresholds)
    False,  # 27: 90°F ≠ 95°F (different thresholds)
    False,  # 28: $500 ≠ $600 (different thresholds)
    False,  # 29: Recession ≠ unemployment 5% (OVERLAP)
    False,  # 30: Democrat wins ≠ Biden runs (OVERLAP)
    
    # 31-40
    False,  # 31: VR headset ≠ stock ATH (OVERLAP)
    False,  # 32: London rain ≠ Bitcoin (UNRELATED)
    False,  # 33: Lakers playoffs ≠ Tesla split (UNRELATED)
    False,  # 34: Unspecified year ≠ 2026 (UNCERTAIN)
    False,  # 35: "this year" ≠ 2025 (UNCERTAIN - depends on when asked)
    True,   # 36: Microsoft acquire Activision = deal close
    True,   # 37: COVID vaccine mandate equivalent
    True,   # 38: Fed cut rates H1 2025 = lower before July
    False,  # 39: 3-way outcome ≠ binary (incompatible outcomes)
    False,  # 40: Next Fed chair ≠ Powell remains (different questions)
    
    # 41-50
    False,  # 41: Moneyline ≠ spread (different bet types)
    False,  # 42: Winner ≠ cover spread (different outcomes)
    True,   # 43: NYC = Manhattan (for practical purposes, close enough)
    False,  # 44: Phoenix ⊂ Arizona (SUBSET - could snow in Flagstaff)
    True,   # 45: Ethereum $3000 equivalent (comma formatting)
    True,   # 46: Oil $85/barrel equivalent
    False,  # 47: Biden nominee ⊂ incumbent runs (SUBSET)
    False,  # 48: Newsom ⊂ any CA governor (SUBSET)
    False,  # 49: GDP 3% ⊂ expansion (SUBSET - could expand <3%)
    False,  # 50: CPI ≠ PCE (different inflation measures)
    
    # 51-60
    False,  # 51: GPT-5 ⊂ any new model (SUBSET)
    False,  # 52: iPhone 17 Sept ⊂ new iPhone fall (SUBSET - Sept ⊂ fall)
    False,  # 53: 2" rain ≠ "heavy" (subjective definition)
    False,  # 54: 50mph ⊂ tropical storm conditions (SUBSET)
    True,   # 55: Midnight UTC Jan 1 = start of 2025 equivalent
    True,   # 56: Tesla close Dec 31 = end of 2024 equivalent
    False,  # 57: Game 1 ≠ series winner (SUBSET)
    True,   # 58: Sweep 3-game = win all games this weekend (equivalent)
    True,   # 59: Exact same question (obvious EQUIVALENT)
    True,   # 60: Gold $2200 equivalent (formatting)
]