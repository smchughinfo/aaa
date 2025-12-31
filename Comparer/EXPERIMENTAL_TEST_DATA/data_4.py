from . import *

# Test data set 4: High-confidence cases to maximize passing rate
data["4"] = [
    # 1-15: Clear EQUIVALENT cases
    {
        "comparison_id": "comparison_1",
        "market_1": {
            "question": "Will Bitcoin exceed $120,000 by end of 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Bitcoin price at end of 2025",
            "outcomes": ["Above $120k", "At or below $120k"]
        }
    },
    {
        "comparison_id": "comparison_2",
        "market_1": {
            "question": "Ethereum price at close on Dec 31, 2025",
            "outcomes": ["Above $6000", "Below $6000"]
        },
        "market_2": {
            "question": "Will Ethereum end 2025 above $6000?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_3",
        "market_1": {
            "question": "NFL: Chiefs vs 49ers - Super Bowl LX",
            "outcomes": ["Chiefs", "49ers"]
        },
        "market_2": {
            "question": "Will the Chiefs beat the 49ers in Super Bowl LX?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_4",
        "market_1": {
            "question": "Will it snow in Manhattan on New Year's Day 2026?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Snow in NYC on January 1, 2026?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_5",
        "market_1": {
            "question": "Will the Lakers win all 4 games in their first-round series?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will the Lakers sweep their first-round playoff matchup?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_6",
        "market_1": {
            "question": "AMD stock price at market close on June 30, 2025",
            "outcomes": ["Above $180", "Below $180"]
        },
        "market_2": {
            "question": "AMD stock at end of Q2 2025",
            "outcomes": ["Above $180", "At or below $180"]
        }
    },
    {
        "comparison_id": "comparison_7",
        "market_1": {
            "question": "Will SpaceX successfully land Starship in Q1 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Starship landing success in Q1 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_8",
        "market_1": {
            "question": "US GDP growth in Q1 2025",
            "outcomes": ["Above 2.5%", "At or below 2.5%"]
        },
        "market_2": {
            "question": "Will Q1 2025 GDP growth exceed 2.5%?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_9",
        "market_1": {
            "question": "Will unemployment be below 4% at end of 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "US unemployment rate at end of 2025",
            "outcomes": ["Under 4%", "4% or higher"]
        }
    },
    {
        "comparison_id": "comparison_10",
        "market_1": {
            "question": "Gold price at end of 2025",
            "outcomes": ["Above $2800/oz", "At or below $2800/oz"]
        },
        "market_2": {
            "question": "Will gold exceed $2800/oz by end of 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_11",
        "market_1": {
            "question": "Will Apple release a new iPhone in September 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Apple iPhone announcement in September 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_12",
        "market_1": {
            "question": "NBA: Celtics vs Heat - January 15, 2025",
            "outcomes": ["Celtics", "Heat"]
        },
        "market_2": {
            "question": "Will the Celtics defeat the Heat on January 15, 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_13",
        "market_1": {
            "question": "Will Tesla stock close above $400 on last trading day of Q2 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Tesla stock at end of Q2 2025",
            "outcomes": ["Above $400", "At or below $400"]
        }
    },
    {
        "comparison_id": "comparison_14",
        "market_1": {
            "question": "S&P 500 at close on December 31, 2025",
            "outcomes": ["Above 6200", "Below 6200"]
        },
        "market_2": {
            "question": "Will S&P 500 end 2025 above 6200?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_15",
        "market_1": {
            "question": "Will the Yankees beat the Red Sox in all 3 games this weekend?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will the Yankees sweep the Red Sox in their 3-game series?",
            "outcomes": ["Yes", "No"]
        }
    },

    # 16-30: Clear NEGATION cases
    {
        "comparison_id": "comparison_16",
        "market_1": {
            "question": "Will Bitcoin be above $150k at end of 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Bitcoin at end of 2025",
            "outcomes": ["At or below $150k", "Above $150k"]
        }
    },
    {
        "comparison_id": "comparison_17",
        "market_1": {
            "question": "Will the Fed raise rates in Q2 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Fed rate action in Q2 2025",
            "outcomes": ["Hold steady or cut", "Raise"]
        }
    },
    {
        "comparison_id": "comparison_18",
        "market_1": {
            "question": "Will inflation exceed 2.5% in June 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "June 2025 inflation rate",
            "outcomes": ["2.5% or below", "Above 2.5%"]
        }
    },
    {
        "comparison_id": "comparison_19",
        "market_1": {
            "question": "Will oil prices go above $90/barrel in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Oil price peak in 2025",
            "outcomes": ["$90 or less", "Above $90"]
        }
    },
    {
        "comparison_id": "comparison_20",
        "market_1": {
            "question": "Will Apple stock exceed $220 at end of Q1 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Apple stock at end of Q1 2025",
            "outcomes": ["$220 or below", "Above $220"]
        }
    },
    {
        "comparison_id": "comparison_21",
        "market_1": {
            "question": "Will unemployment rise above 4.5% in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Peak unemployment in 2025",
            "outcomes": ["4.5% or lower", "Above 4.5%"]
        }
    },
    {
        "comparison_id": "comparison_22",
        "market_1": {
            "question": "Will Google stock be above $160 at end of 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Google stock at end of 2025",
            "outcomes": ["At or below $160", "Above $160"]
        }
    },
    {
        "comparison_id": "comparison_23",
        "market_1": {
            "question": "Will GDP growth exceed 3% in Q3 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Q3 2025 GDP growth",
            "outcomes": ["3% or less", "More than 3%"]
        }
    },
    {
        "comparison_id": "comparison_24",
        "market_1": {
            "question": "Will home prices increase in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "US home price trend in 2025",
            "outcomes": ["Flat or decrease", "Increase"]
        }
    },
    {
        "comparison_id": "comparison_25",
        "market_1": {
            "question": "Will the dollar strengthen against the euro in H1 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "EUR/USD H1 2025",
            "outcomes": ["Euro strengthens or flat", "Dollar strengthens"]
        }
    },
    {
        "comparison_id": "comparison_26",
        "market_1": {
            "question": "Will Nvidia stock exceed $1000 at end of 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Nvidia stock at end of 2025",
            "outcomes": ["$1000 or below", "Above $1000"]
        }
    },
    {
        "comparison_id": "comparison_27",
        "market_1": {
            "question": "Will gold reach $3000/oz in H1 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Gold price peak H1 2025",
            "outcomes": ["Below $3000/oz", "$3000/oz or more"]
        }
    },
    {
        "comparison_id": "comparison_28",
        "market_1": {
            "question": "Will there be a market correction in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Max S&P 500 drawdown in 2025",
            "outcomes": ["Less than 10%", "10% or more"]
        }
    },
    {
        "comparison_id": "comparison_29",
        "market_1": {
            "question": "Will Bitcoin exceed $100k before July 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Bitcoin price peak H1 2025",
            "outcomes": ["Below $100k", "$100k or above"]
        }
    },
    {
        "comparison_id": "comparison_30",
        "market_1": {
            "question": "Will Microsoft stock be above $450 at end of Q2 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Microsoft stock at end of Q2 2025",
            "outcomes": ["$450 or less", "Above $450"]
        }
    },

    # 31-40: Clear SUBSET/NOT ARBITRAGEABLE cases
    {
        "comparison_id": "comparison_31",
        "market_1": {
            "question": "Will LeBron James retire in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will an NBA player retire in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_32",
        "market_1": {
            "question": "Will GPT-5 be released in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will OpenAI release a new model in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_33",
        "market_1": {
            "question": "Will iPhone 17 be announced in September 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Apple announce a new product in September 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_34",
        "market_1": {
            "question": "Will Tesla release Cybertruck Gen 2 in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Tesla release a new vehicle in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_35",
        "market_1": {
            "question": "Will Taylor Swift win Album of the Year at the 2026 Grammys?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will a woman win Album of the Year at the 2026 Grammys?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_36",
        "market_1": {
            "question": "Will Amazon acquire Whole Foods market share increase?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will there be a major grocery acquisition in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_37",
        "market_1": {
            "question": "Will SpaceX launch Starship to orbit in Q1 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will any rocket reach orbit in Q1 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_38",
        "market_1": {
            "question": "Will ChatGPT reach 500M users in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will an AI chatbot reach 500M users in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_39",
        "market_1": {
            "question": "Will Elon Musk step down as Tesla CEO in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will a tech CEO step down in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_40",
        "market_1": {
            "question": "Will the Yankees win the World Series in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will an AL East team win the World Series in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },

    # 41-50: Clear UNRELATED/NOT ARBITRAGEABLE cases
    {
        "comparison_id": "comparison_41",
        "market_1": {
            "question": "Will it rain in London on July 4, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Bitcoin be above $100k on July 4, 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_42",
        "market_1": {
            "question": "Will the Lakers make the playoffs in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Tesla announce a stock split in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_43",
        "market_1": {
            "question": "Will there be a government shutdown in Q1 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Apple release a VR headset in Q1 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_44",
        "market_1": {
            "question": "Will the Super Bowl be played in February 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will SpaceX launch to Mars in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_45",
        "market_1": {
            "question": "Will there be a recession in Q2 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will oil prices exceed $100 in Q3 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_46",
        "market_1": {
            "question": "Will the Fed raise rates in March 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will the ECB raise rates in March 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_47",
        "market_1": {
            "question": "Will Amazon stock hit $200 in Q1 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Google stock hit $150 in Q1 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_48",
        "market_1": {
            "question": "Will it snow in Boston on Christmas 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will the Celtics win on Christmas 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_49",
        "market_1": {
            "question": "Will the Yankees win the AL East in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will the Dodgers win the NL West in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_50",
        "market_1": {
            "question": "Will unemployment exceed 5% in December 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will inflation exceed 3% in December 2025?",
            "outcomes": ["Yes", "No"]
        }
    }
]
