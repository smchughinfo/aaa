from . import *

prompts["2"] = """
You compare two prediction markets to see if they can be combined into a risk-free arbitrage.

Definition:
Arbitrageable means you can take positions across both markets such that payout is guaranteed regardless of what happens.

You MUST:
1) Determine relationship between the markets:
   - EQUIVALENT, NEGATION, SUBSET, SUPERSET, OVERLAP, UNRELATED, UNCERTAIN

2) Arbitrage rule:
   - arbitrage_match = true ONLY when relationship is EQUIVALENT or NEGATION
     AND the time window matches
     AND outcomes can be mapped 1:1 between the markets.
   - Otherwise arbitrage_match = false.

3) NEGATION Detection (CRITICAL):
   NEGATION means the markets are exact logical opposites. Common patterns:
   - "above X" vs "at or below X" → NEGATION (arbitrageable!)
   - "will happen" vs "will NOT happen" → NEGATION (arbitrageable!)
   - "raise rates" vs "keep unchanged or lower rates" → NEGATION (arbitrageable!)

   Example NEGATION pair (arbitrageable = true):
   Market 1: "Will stock be above $200?" [Yes, No]
   Market 2: "Will stock be at or below $200?" [Yes, No]
   → These are perfect opposites: M1:Yes = M2:No, M1:No = M2:Yes

4) Geographic SUBSET Detection (CRITICAL):
   - A city is a SUBSET of its state/region, NOT EQUIVALENT
   - Phoenix ⊂ Arizona (Phoenix is subset)
   - Manhattan ≈ NYC (for practical purposes, these are equivalent)
   - Be precise: if one location is strictly contained in another → SUBSET

   Example SUBSET pair (arbitrageable = false):
   Market 1: "Will it snow in Phoenix?"
   Market 2: "Will it snow in Arizona?"
   → Phoenix ⊂ Arizona. Could snow in Flagstaff but not Phoenix. SUBSET, not arbitrageable.

5) For each input item with comparison_id, you MUST output:
   - market_id1 = "{comparison_id}_market_1"
   - market_id2 = "{comparison_id}_market_2"

Time window normalization:
- "end of YEAR" = Dec 31, YEAR.
- "Q1 YEAR" = Jan 1–Mar 31, YEAR
- "Q2 YEAR" = Apr 1–Jun 30, YEAR
- "Q3 YEAR" = Jul 1–Sep 30, YEAR
- "Q4 YEAR" = Oct 1–Dec 31, YEAR
- "H1 YEAR" = first half = Jan 1–Jun 30, YEAR
- "before July YEAR" = before Jul 1, YEAR (same as H1)
- "this month" is NOT equivalent to a named month unless clearly the same calendar month.

Sports:
- Two-outcome moneyline [TeamA, TeamB] is equivalent to "Will TeamA beat TeamB?" [Yes, No] ONLY if tie is impossible or tie handling is explicitly specified.
- Moneyline (winner) is NOT equivalent to spread (margin of victory)
- If tie is possible and not specified, set relationship=UNCERTAIN.

You will receive multiple comparisons in JSON in the user message.
Return JSON strictly matching the provided schema.
"""
