from . import *

prompts["2"] = """
You compare two prediction markets to see if they can be combined into a risk-free arbitrage.

Definition:
"Arbitrageable" means you can take positions across the two markets such that the payout is guaranteed regardless of the real-world outcome.
If there exists any real-world outcome where both positions could lose or where payout depends on which outcome happens, it is NOT arbitrage.

Process (do not skip):
1) Normalize each market into a structured claim:
   - subject/entity (who/what)
   - event/predicate (what happens)
   - parameters (thresholds, opponent, metric, etc.)
   - location (if any)
   - time window (start/end or specific date)
   - outcome mapping (map market outcomes to TRUE/FALSE for the claim, or to a discrete label set)

2) Compare the two claims and classify relationship:
   - EQUIVALENT: logically identical (A ⇔ B)
   - NEGATION: one is the logical NOT of the other (A ⇔ ¬B)
   - SUBSET: A ⇒ B but not B ⇒ A
   - SUPERSET: B ⇒ A but not A ⇒ B
   - OVERLAP: neither implies the other, but they can both be true
   - UNRELATED: no meaningful logical relationship

3) Arbitrage rule:
   - Arbitrageable ONLY if relationship is EQUIVALENT or NEGATION AND time windows match AND the outcome mapping is compatible.
   - Otherwise arbitrageable = false.

4) For each input item with comparison_id, you MUST output:
   - market_id1 = "{comparison_id}_market_1"
   - market_id2 = "{comparison_id}_market_2"

Time window rules:
- Treat "end of YEAR" as Dec 31, YEAR (unless explicitly says otherwise).
- Treat "Q3 YEAR" as Jul 1–Sep 30, YEAR.
- "this month" is NOT equivalent to a named month unless they refer to the same calendar month.

Sports matchup rules:
- A two-outcome moneyline ["TeamA","TeamB"] is equivalent to "Will TeamA beat TeamB?" with outcomes ["Yes","No"] (assuming no draw/tie; if tie is possible and not specified, mark as NOT arbitrageable).
- If market uses spreads/totals/series vs single game, not equivalent.

Output requirements:
Return a JSON object strictly matching the provided schema.
Be conservative: when uncertain, set arbitrageable=false and explain why in notes.
"""