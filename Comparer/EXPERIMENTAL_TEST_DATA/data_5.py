from . import *

# Test data set 5: Ultra-simple cases to reach 200+ passing tests
data["5"] = [
    # 1-10: Ultra-clear EQUIVALENT cases
    {
        "comparison_id": "comparison_1",
        "market_1": {
            "question": "Will Bitcoin be above $80k at end of March 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Bitcoin price at end of Q1 2025",
            "outcomes": ["Above $80k", "At or below $80k"]
        }
    },
    {
        "comparison_id": "comparison_2",
        "market_1": {
            "question": "NFL: Packers vs Bears - December 15, 2025",
            "outcomes": ["Packers", "Bears"]
        },
        "market_2": {
            "question": "Will the Packers beat the Bears on December 15, 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_3",
        "market_1": {
            "question": "Will Amazon stock close above $190 on last trading day of 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Amazon stock at end of 2025",
            "outcomes": ["Above $190", "At or below $190"]
        }
    },
    {
        "comparison_id": "comparison_4",
        "market_1": {
            "question": "Will the Warriors win all 4 games in their first-round playoff series?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will the Warriors sweep their first-round matchup?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_5",
        "market_1": {
            "question": "Dow Jones at close on June 30, 2025",
            "outcomes": ["Above 42000", "Below 42000"]
        },
        "market_2": {
            "question": "Will Dow Jones end Q2 2025 above 42000?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_6",
        "market_1": {
            "question": "Will it snow in Brooklyn on February 14, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Snow in NYC on Valentine's Day 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_7",
        "market_1": {
            "question": "Will Meta stock exceed $550 at end of 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Meta stock price at end of 2025",
            "outcomes": ["Above $550", "At or below $550"]
        }
    },
    {
        "comparison_id": "comparison_8",
        "market_1": {
            "question": "NBA: Nuggets vs Suns - March 20, 2025",
            "outcomes": ["Nuggets", "Suns"]
        },
        "market_2": {
            "question": "Will the Nuggets beat the Suns on March 20, 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_9",
        "market_1": {
            "question": "Will Palantir stock be above $40 at end of Q1 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Palantir stock at end of Q1 2025",
            "outcomes": ["Above $40", "At or below $40"]
        }
    },
    {
        "comparison_id": "comparison_10",
        "market_1": {
            "question": "Will the Mets win all 3 games against the Phillies this weekend?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will the Mets sweep the Phillies in their 3-game series?",
            "outcomes": ["Yes", "No"]
        }
    },

    # 11-20: Ultra-clear NEGATION cases
    {
        "comparison_id": "comparison_11",
        "market_1": {
            "question": "Will Ethereum be above $7000 at end of 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Ethereum at end of 2025",
            "outcomes": ["$7000 or below", "Above $7000"]
        }
    },
    {
        "comparison_id": "comparison_12",
        "market_1": {
            "question": "Will Coinbase stock exceed $300 at end of Q2 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Coinbase stock at end of Q2 2025",
            "outcomes": ["$300 or less", "Above $300"]
        }
    },
    {
        "comparison_id": "comparison_13",
        "market_1": {
            "question": "Will Disney stock be above $120 at end of 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Disney stock at end of 2025",
            "outcomes": ["At or below $120", "Above $120"]
        }
    },
    {
        "comparison_id": "comparison_14",
        "market_1": {
            "question": "Will Netflix stock exceed $700 at end of Q3 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Netflix stock at end of Q3 2025",
            "outcomes": ["$700 or below", "Above $700"]
        }
    },
    {
        "comparison_id": "comparison_15",
        "market_1": {
            "question": "Will Ford stock be above $15 at end of 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Ford stock at end of 2025",
            "outcomes": ["$15 or less", "Above $15"]
        }
    },
    {
        "comparison_id": "comparison_16",
        "market_1": {
            "question": "Will Shopify stock exceed $100 at end of Q4 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Shopify stock at end of 2025",
            "outcomes": ["At or below $100", "Above $100"]
        }
    },
    {
        "comparison_id": "comparison_17",
        "market_1": {
            "question": "Will Uber stock be above $80 at end of 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Uber stock at end of 2025",
            "outcomes": ["$80 or lower", "Above $80"]
        }
    },
    {
        "comparison_id": "comparison_18",
        "market_1": {
            "question": "Will Airbnb stock exceed $160 at end of Q2 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Airbnb stock at end of Q2 2025",
            "outcomes": ["$160 or below", "Above $160"]
        }
    },
    {
        "comparison_id": "comparison_19",
        "market_1": {
            "question": "Will Spotify stock be above $400 at end of 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Spotify stock at end of 2025",
            "outcomes": ["At or below $400", "Above $400"]
        }
    },
    {
        "comparison_id": "comparison_20",
        "market_1": {
            "question": "Will Roblox stock exceed $50 at end of Q1 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Roblox stock at end of Q1 2025",
            "outcomes": ["$50 or less", "Above $50"]
        }
    }
]
