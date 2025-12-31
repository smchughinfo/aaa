from . import *

# Answer key for data_2
# True = arbitrageable (EQUIVALENT or NEGATION with matching outcomes)
# False = not arbitrageable
data_answers["2"] = [
    # 1-5: Stock market edge cases
    True,   # 1: Q1 close = end of Q1, EQUIVALENT
    True,   # 2: EOD March 31 = end of Q1, EQUIVALENT
    True,   # 3: Last trading day close = end of 2025, NEGATION (above vs at or below)
    False,  # 4: "if last trading day" creates uncertainty, different outcomes
    False,  # 5: Market open Jan 2 ≠ market close Dec 31 (different times)

    # 6-10: Geographic edge cases
    True,   # 6: Brooklyn ≈ NYC, EQUIVALENT
    False,  # 7: San Francisco ⊂ Bay Area, SUBSET
    False,  # 8: Miami ⊂ Florida, SUBSET
    True,   # 9: LA ≈ LA metro area, EQUIVALENT
    False,  # 10: Seattle ⊂ Washington state, SUBSET

    # 11-15: Person vs Category
    False,  # 11: Elon Musk ⊂ tech billionaires, SUBSET
    False,  # 12: Taylor Swift ⊂ female pop artists, SUBSET
    True,   # 13: LeBron James = LeBron James, EQUIVALENT
    False,  # 14: Mark Zuckerberg ≠ Meta (person vs company), OVERLAP
    True,   # 15: Satya Nadella remaining = same CEO, EQUIVALENT

    # 16-20: Negation cases
    True,   # 16: above $100k vs $100k or below/above $100k, NEGATION
    True,   # 17: Raise vs Keep same or lower/Raise, NEGATION
    True,   # 18: Under 4% vs 4% or higher/Under 4%, NEGATION
    True,   # 19: Exceed $100 vs $100 or less/Above $100, NEGATION
    True,   # 20: Above 3% vs At or below 3%/Above 3%, NEGATION

    # 21-25: Sports
    True,   # 21: [Lakers, Celtics] vs [Yes, No] for Lakers, EQUIVALENT (assuming Finals between these two)
    True,   # 22: [Yes, No] vs [Yankees, Not Yankees], EQUIVALENT
    False,  # 23: 3 outcomes vs 2 outcomes, can't map 1:1
    True,   # 24: Come out of retirement ≈ play NFL game, EQUIVALENT
    False,  # 25: Make playoffs ⊂ win division, SUBSET

    # 26-30: Overlap vs Subset
    False,  # 26: GPT-5 ⊂ new model, SUBSET
    False,  # 27: iPhone 17 Pro ⊂ new iPhone, SUBSET
    False,  # 28: SpaceX ⊂ any company, SUBSET
    False,  # 29: Amazon ⊂ tech company, SUBSET
    False,  # 30: ChatGPT-5 vs GPT-5, UNCERTAIN (might be same or different)

    # 31-35: Uncertain/Unrelated
    False,  # 31: Q1 recession vs Q2 recession, different time periods
    False,  # 32: Bitcoin vs Ethereum, different assets
    False,  # 33: Going public vs stock price, can't have price without being public
    False,  # 34: 2024 election vs 2028 run, different events
    False,  # 35: Earthquake vs tsunami, related but not same

    # 36-40: Complex EQUIVALENT
    True,   # 36: S&P close last day June = end Q2, EQUIVALENT
    True,   # 37: EOD Dec 31 = end 2025, EQUIVALENT
    True,   # 38: Final trading day close = end 2025, NEGATION (above vs at or below)
    True,   # 39: [Warriors, Lakers] vs [Yes, No] for Warriors, EQUIVALENT
    True,   # 40: Sweep = win all 4 games, EQUIVALENT

    # 41-45: More NEGATION
    True,   # 41: Above $2500 vs At or below $2500/Above $2500, NEGATION
    True,   # 42: Cut vs Keep same or raise/Cut, NEGATION
    True,   # 43: Exceed 3% vs 3% or less/Above 3%, NEGATION
    True,   # 44: Above $200 vs $200 or below/Above $200, NEGATION
    True,   # 45: Exceed $300 vs At or below $300/Above $300, NEGATION

    # 46-50: Mixed
    False,  # 46: Government shutdown vs lasting more than 1 day, OVERLAP
    False,  # 47: Overturn precedent ⊂ landmark ruling, SUBSET/OVERLAP
    False,  # 48: AI regulations ⊂ tech regulation, SUBSET
    True,   # 49: Close above $500 vs Above $500/At or below $500, NEGATION
    True,   # 50: Exceed 5% vs Over 5%/5% or under, EQUIVALENT (exceed = over)
]
