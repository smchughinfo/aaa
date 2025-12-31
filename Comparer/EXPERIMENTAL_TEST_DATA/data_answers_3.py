from . import *

# Answer key for data_3
# True = arbitrageable (EQUIVALENT or NEGATION with matching outcomes)
# False = not arbitrageable
data_answers["3"] = [
    # 1-10: Geographic precision tests
    True,   # 1: Manhattan ≈ NYC, EQUIVALENT
    False,  # 2: Dallas ⊂ Texas, SUBSET
    False,  # 3: Chicago ⊂ Illinois, SUBSET
    True,   # 4: Portland ≈ Portland metro, EQUIVALENT
    False,  # 5: Houston ⊂ Gulf Coast, SUBSET
    True,   # 6: San Jose ≈ Silicon Valley, EQUIVALENT (SJ is heart of SV)
    False,  # 7: Boston ⊂ Massachusetts, SUBSET
    True,   # 8: Atlanta ≈ Atlanta metro, EQUIVALENT
    False,  # 9: Oklahoma City ⊂ Oklahoma, SUBSET
    False,  # 10: Las Vegas ⊂ Nevada, SUBSET

    # 11-20: Outcome count mismatch tests
    False,  # 11: 4 outcomes vs 2, can't map 1:1
    False,  # 12: 3 outcomes vs 2, can't map 1:1
    True,   # 13: [Yankees, Dodgers] vs [Yes, No] for Yankees, EQUIVALENT (assuming Finals between these two)
    True,   # 14: [Chiefs, Not Chiefs] vs [Yes, No] for Chiefs, EQUIVALENT
    False,  # 15: 3 outcomes vs 2, can't map 1:1

    # 16-25: Product/Model/Company name precision
    False,  # 16: iPhone 17 ⊂ new phone, SUBSET
    True,   # 17: GPT-5 = GPT-5, EQUIVALENT
    False,  # 18: FSD v13 ⊂ new FSD version, SUBSET
    True,   # 19: Meta = Facebook (company renamed), EQUIVALENT
    False,  # 20: Claude 4 ⊂ new frontier model, SUBSET
    False,  # 21: Gemini 2.0 ⊂ new AI model, SUBSET
    False,  # 22: Windows 12 ⊂ new Windows version, SUBSET
    False,  # 23: PS6 ⊂ new gaming console, SUBSET
    False,  # 24: Starship ⊂ SpaceX vehicle, SUBSET (Falcon is also SpaceX)
    False,  # 25: ChatGPT Pro ⊂ new subscription tier, SUBSET

    # 26-35: Stock market time precision edge cases
    True,   # 26: 4pm ET March 31 = close on last trading day Q1, NEGATION (above vs at or below)
    True,   # 27: Market close Dec 31 = end of 2025, EQUIVALENT ($200+ maps to at least $200)
    True,   # 28: EOD June 30 = end Q2, NEGATION (at or below vs above)
    True,   # 29: 4pm Eastern final Q4 trading day = end of 2025, EQUIVALENT
    True,   # 30: Closing price last day 2025 = end of year, EQUIVALENT (Alphabet = Google parent)
    True,   # 31: Midnight UTC Jan 1, 2025 ≈ end of 2024, EQUIVALENT (cryptocurrencies trade 24/7)
    True,   # 32: 11:59pm Dec 31 ≈ end of 2025, NEGATION (above/below vs above/at or below)
    False,  # 33: Intraday high ≠ close price, different measurements
    False,  # 34: Opening bell Jan 2, 2026 ≠ close Dec 31, 2025, different times
    True,   # 35: Market close Dec 31 = end of year, NEGATION (above/below vs above/at or below)

    # 36-45: Subtle negation and equivalence cases
    True,   # 36: Exceed 2% vs 2% or less / More than 2%, NEGATION
    True,   # 37: Surpass 3% vs 3% or below / Above 3%, NEGATION
    True,   # 38: Hold steady vs Change / Keep unchanged, NEGATION
    True,   # 39: Positive year vs Negative or zero / Positive, NEGATION
    True,   # 40: Rise vs Stay same or fall / Increase, NEGATION
    True,   # 41: Increase vs Decrease or flat / Rise, NEGATION
    True,   # 42: Drop below $70 vs $70 or above / Below $70, NEGATION
    True,   # 43: Reach $3000 vs Under $3000 / $3000 or more, NEGATION
    True,   # 44: Dollar strengthen vs Euro strengthens or flat / Dollar strengthens, NEGATION
    True,   # 45: Correction (10%+ drop) vs Less than 10% / 10% or more, NEGATION

    # 46-50: Mixed challenging scenarios
    False,  # 46: Make playoffs ⊂ top 10 in conference (play-in tournament makes this subset)
    True,   # 47: Major tech IPO = company going public, EQUIVALENT
    True,   # 48: Trump nominee vs [Trump, Not Trump], EQUIVALENT
    True,   # 49: Net inflows vs Net outflows or neutral / Net inflows, NEGATION
    True,   # 50: Exceed 1M vs 1M or fewer / More than 1M, NEGATION
]
