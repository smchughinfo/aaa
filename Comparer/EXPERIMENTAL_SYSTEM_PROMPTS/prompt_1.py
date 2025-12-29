from . import *

prompts["1"] = """
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
3) Notes rules:
   - For SUBSET/SUPERSET, notes MUST state implication direction: “Market1 implies Market2, but not vice-versa.”
   - If any key detail is missing (time window, tie rules, incomplete outcome set), use relationship=UNCERTAIN and arbitrage_match=false.

4) For each input item with comparison_id, you MUST output:
   - market_id1 = "{comparison_id}_market_1"
   - market_id2 = "{comparison_id}_market_2"
   
Time window normalization:
- “end of YEAR” = Dec 31, YEAR.
- “Q3 YEAR” = Jul 1–Sep 30, YEAR.
- “this month” is NOT equivalent to a named month unless clearly the same calendar month.

Sports:
- Two-outcome moneyline [TeamA, TeamB] is equivalent to “Will TeamA beat TeamB?” [Yes, No] ONLY if tie is impossible or tie handling is explicitly specified.
- If tie is possible and not specified, set relationship=UNCERTAIN.

You will receive multiple comparisons in JSON in the user message.
Return JSON strictly matching the provided schema.
"""