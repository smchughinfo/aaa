from . import *

# Test data set 2: More edge cases and challenging scenarios
data["2"] = [
    # 1-5: Stock market edge cases with different time phrasings
    {
        "comparison_id": "comparison_1",
        "market_1": {
            "question": "Apple stock at market close on final trading day of Q1 2025",
            "outcomes": ["Above $180", "Below $180"]
        },
        "market_2": {
            "question": "Will Apple stock end Q1 2025 above $180?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_2",
        "market_1": {
            "question": "Google stock price at EOD March 31, 2025",
            "outcomes": ["$150+", "Under $150"]
        },
        "market_2": {
            "question": "Google stock price at end of Q1 2025",
            "outcomes": ["$150 or above", "Below $150"]
        }
    },
    {
        "comparison_id": "comparison_3",
        "market_1": {
            "question": "Will Microsoft close above $400 on the last trading day of 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Microsoft stock price at end of 2025",
            "outcomes": ["Over $400", "At or below $400"]
        }
    },
    {
        "comparison_id": "comparison_4",
        "market_1": {
            "question": "Amazon stock on Dec 30, 2025 (if last trading day)",
            "outcomes": ["Above $200", "Below $200"]
        },
        "market_2": {
            "question": "Amazon stock at end of 2025",
            "outcomes": ["Above $200", "At or below $200"]
        }
    },
    {
        "comparison_id": "comparison_5",
        "market_1": {
            "question": "Tesla stock at market open on Jan 2, 2025",
            "outcomes": ["Above $250", "Below $250"]
        },
        "market_2": {
            "question": "Tesla stock at market close on Dec 31, 2024",
            "outcomes": ["Above $250", "Below $250"]
        }
    },

    # 6-10: Geographic edge cases
    {
        "comparison_id": "comparison_6",
        "market_1": {
            "question": "Will it snow in Brooklyn on Christmas Day 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will NYC see snow on December 25, 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_7",
        "market_1": {
            "question": "Temperature in San Francisco above 90°F on July 4, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will the Bay Area exceed 90°F on July 4, 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_8",
        "market_1": {
            "question": "Will Miami experience a hurricane in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Florida experience a hurricane in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_9",
        "market_1": {
            "question": "Earthquake magnitude 5+ in Los Angeles in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will there be a magnitude 5+ earthquake in LA metro area in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_10",
        "market_1": {
            "question": "Will Seattle get more than 50 inches of rain in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Washington state get more than 50 inches of rain in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },

    # 11-15: Person vs Category edge cases
    {
        "comparison_id": "comparison_11",
        "market_1": {
            "question": "Will Elon Musk step down as CEO of Tesla in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will a tech billionaire step down as CEO in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_12",
        "market_1": {
            "question": "Will Taylor Swift win a Grammy in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will a female pop artist win a Grammy in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_13",
        "market_1": {
            "question": "Will LeBron James retire in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will LeBron James retire in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_14",
        "market_1": {
            "question": "Will Mark Zuckerberg launch a new product in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Meta launch a new product in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_15",
        "market_1": {
            "question": "Will Satya Nadella remain Microsoft CEO through 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Microsoft have the same CEO at end of 2025?",
            "outcomes": ["Yes", "No"]
        }
    },

    # 16-20: Negation edge cases
    {
        "comparison_id": "comparison_16",
        "market_1": {
            "question": "Will Bitcoin be above $100k on Dec 31, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Bitcoin price at end of 2025",
            "outcomes": ["$100k or below", "Above $100k"]
        }
    },
    {
        "comparison_id": "comparison_17",
        "market_1": {
            "question": "Will the Fed raise rates in Q1 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Federal Reserve action on rates in Q1 2025",
            "outcomes": ["Keep same or lower", "Raise"]
        }
    },
    {
        "comparison_id": "comparison_18",
        "market_1": {
            "question": "Will unemployment be under 4% in June 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "US unemployment rate in June 2025",
            "outcomes": ["4% or higher", "Under 4%"]
        }
    },
    {
        "comparison_id": "comparison_19",
        "market_1": {
            "question": "Will oil prices exceed $100/barrel in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Oil price peak in 2025",
            "outcomes": ["$100 or less", "Above $100"]
        }
    },
    {
        "comparison_id": "comparison_20",
        "market_1": {
            "question": "Will inflation be above 3% in December 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Inflation rate December 2025",
            "outcomes": ["At or below 3%", "Above 3%"]
        }
    },

    # 21-25: Sports edge cases
    {
        "comparison_id": "comparison_21",
        "market_1": {
            "question": "NBA Finals 2025 winner",
            "outcomes": ["Lakers", "Celtics"]
        },
        "market_2": {
            "question": "Will the Lakers win the 2025 NBA Finals?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_22",
        "market_1": {
            "question": "Will the Yankees win the World Series in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "2025 World Series champion",
            "outcomes": ["Yankees", "Not Yankees"]
        }
    },
    {
        "comparison_id": "comparison_23",
        "market_1": {
            "question": "Super Bowl LX winner",
            "outcomes": ["Chiefs", "49ers", "Other"]
        },
        "market_2": {
            "question": "Will the Chiefs win Super Bowl LX?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_24",
        "market_1": {
            "question": "Will Tom Brady come out of retirement in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Tom Brady play an NFL game in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_25",
        "market_1": {
            "question": "Will the Dodgers make the playoffs in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will the Dodgers win the division in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },

    # 26-30: Overlap vs Subset edge cases
    {
        "comparison_id": "comparison_26",
        "market_1": {
            "question": "Will GPT-5 be released in H1 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will OpenAI release a new model in H1 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_27",
        "market_1": {
            "question": "Will iPhone 17 Pro be announced in September 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Apple announce a new iPhone in September 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_28",
        "market_1": {
            "question": "Will SpaceX launch Starship to Mars in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will any company launch to Mars in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_29",
        "market_1": {
            "question": "Will Amazon acquire a company for over $10B in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will there be a tech acquisition over $10B in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_30",
        "market_1": {
            "question": "Will ChatGPT-5 be released in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will GPT-5 be released in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },

    # 31-35: Uncertain/Unrelated edge cases
    {
        "comparison_id": "comparison_31",
        "market_1": {
            "question": "Will there be a recession in the US in Q1 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will there be a recession in the US in Q2 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_32",
        "market_1": {
            "question": "Will Bitcoin hit $100k before end of Q1 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Ethereum hit $10k before end of Q1 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_33",
        "market_1": {
            "question": "Will SpaceX go public in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will SpaceX stock price be above $100 in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_34",
        "market_1": {
            "question": "Will Trump win the 2024 election?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Trump run in 2028?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_35",
        "market_1": {
            "question": "Will there be a major earthquake in California in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will there be a tsunami warning in California in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },

    # 36-40: Complex EQUIVALENT cases
    {
        "comparison_id": "comparison_36",
        "market_1": {
            "question": "S&P 500 at close on last day of June 2025",
            "outcomes": ["Above 5000", "Below 5000"]
        },
        "market_2": {
            "question": "Will S&P 500 end Q2 2025 above 5000?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_37",
        "market_1": {
            "question": "Dow Jones at EOD December 31, 2025",
            "outcomes": ["40000+", "Under 40000"]
        },
        "market_2": {
            "question": "Dow Jones at end of 2025",
            "outcomes": ["At or above 40000", "Below 40000"]
        }
    },
    {
        "comparison_id": "comparison_38",
        "market_1": {
            "question": "Nasdaq close on final trading day of 2025",
            "outcomes": ["Above 18000", "At or below 18000"]
        },
        "market_2": {
            "question": "Will Nasdaq end 2025 above 18000?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_39",
        "market_1": {
            "question": "NBA: Warriors vs Lakers - March 15, 2025",
            "outcomes": ["Warriors", "Lakers"]
        },
        "market_2": {
            "question": "Will the Warriors beat the Lakers on March 15, 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_40",
        "market_1": {
            "question": "Will the Celtics sweep their first-round playoff series?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will the Celtics win all 4 games in round 1 of the playoffs?",
            "outcomes": ["Yes", "No"]
        }
    },

    # 41-45: More NEGATION cases
    {
        "comparison_id": "comparison_41",
        "market_1": {
            "question": "Will gold be above $2500/oz on Dec 31, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Gold price at end of 2025",
            "outcomes": ["At or below $2500/oz", "Above $2500/oz"]
        }
    },
    {
        "comparison_id": "comparison_42",
        "market_1": {
            "question": "Will the Fed cut rates in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Fed rate action in 2025",
            "outcomes": ["Keep same or raise", "Cut"]
        }
    },
    {
        "comparison_id": "comparison_43",
        "market_1": {
            "question": "Will GDP growth exceed 3% in Q1 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Q1 2025 GDP growth rate",
            "outcomes": ["3% or less", "Above 3%"]
        }
    },
    {
        "comparison_id": "comparison_44",
        "market_1": {
            "question": "Will Apple stock be above $200 on June 30, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Apple stock at end of Q2 2025",
            "outcomes": ["$200 or below", "Above $200"]
        }
    },
    {
        "comparison_id": "comparison_45",
        "market_1": {
            "question": "Will Tesla stock exceed $300 at end of 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Tesla at market close on last trading day of 2025",
            "outcomes": ["At or below $300", "Above $300"]
        }
    },

    # 46-50: Mixed challenging cases
    {
        "comparison_id": "comparison_46",
        "market_1": {
            "question": "Will there be a government shutdown in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "US government shutdown lasting more than 1 day in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_47",
        "market_1": {
            "question": "Will the Supreme Court overturn a major precedent in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will the Supreme Court issue a landmark ruling in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_48",
        "market_1": {
            "question": "Will AI regulations pass Congress in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will any tech regulation pass Congress in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_49",
        "market_1": {
            "question": "Will Netflix stock close above $500 on Dec 31, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Netflix stock price at end of 2025",
            "outcomes": ["Above $500", "At or below $500"]
        }
    },
    {
        "comparison_id": "comparison_50",
        "market_1": {
            "question": "Will China's GDP growth exceed 5% in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "China 2025 annual GDP growth rate",
            "outcomes": ["Over 5%", "5% or under"]
        }
    }
]
