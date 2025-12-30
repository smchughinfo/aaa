from . import *

data["1"] = [
    {
        "comparison_id": "comparison_1",
        "market_1": {
            "question": "Will Tesla stock close above $300 on June 30, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Tesla share price at end of Q2 2025",
            "outcomes": ["Above $300", "Below $300"]
        }
    },
    {
        "comparison_id": "comparison_2",
        "market_1": {
            "question": "Will it snow in Denver on Christmas Day 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Denver weather on Dec 25, 2025",
            "outcomes": ["Snow", "No Snow"]
        }
    },
    {
        "comparison_id": "comparison_3",
        "market_1": {
            "question": "MLB: Yankees vs Red Sox - July 4, 2025",
            "outcomes": ["Yankees", "Red Sox"]
        },
        "market_2": {
            "question": "Will the Yankees beat the Red Sox on July 4, 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_4",
        "market_1": {
            "question": "Will unemployment rate be below 4% in December 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "US unemployment rate at end of 2025",
            "outcomes": ["Under 4%", "4% or higher"]
        }
    },
    {
        "comparison_id": "comparison_5",
        "market_1": {
            "question": "Will the Dow Jones close above 40,000 on Jan 31, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Dow Jones end of January 2025",
            "outcomes": ["Over 40,000", "Under 40,000"]
        }
    },
    
    # NEGATION (should also be arbitrageable = True)
    {
        "comparison_id": "comparison_6",
        "market_1": {
            "question": "Will Amazon stock be above $200 on March 15, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Amazon stock be at or below $200 on March 15, 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_7",
        "market_1": {
            "question": "Will the Fed raise rates in Q1 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will the Fed keep rates unchanged or lower them in Q1 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    
    # SUBSET relationships (should be arbitrageable = False)
    {
        "comparison_id": "comparison_8",
        "market_1": {
            "question": "Will a Category 5 hurricane hit Florida in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will any hurricane hit Florida in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_9",
        "market_1": {
            "question": "Will the Supreme Court overturn Roe v Wade in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will the Supreme Court issue any major ruling in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_10",
        "market_1": {
            "question": "Will Netflix stock hit $500 by June 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Netflix stock go up in first half of 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_11",
        "market_1": {
            "question": "Will Tom Brady return to NFL in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will any retired QB return to NFL in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_12",
        "market_1": {
            "question": "Will ChatGPT reach 200M users by end of 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will any AI chatbot reach 200M users by end of 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    
    # Different time windows (should be arbitrageable = False)
    {
        "comparison_id": "comparison_13",
        "market_1": {
            "question": "Will Bitcoin hit $150,000 by end of Q1 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Bitcoin hit $150,000 by end of Q2 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_14",
        "market_1": {
            "question": "Will the S&P 500 be above 5000 on Jan 1, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will the S&P 500 be above 5000 on Dec 31, 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_15",
        "market_1": {
            "question": "Will inflation be below 2% in January 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will inflation be below 2% in December 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    
    # Different thresholds (should be arbitrageable = False)
    {
        "comparison_id": "comparison_16",
        "market_1": {
            "question": "Will gold close above $2000/oz on Feb 1, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will gold close above $2100/oz on Feb 1, 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_17",
        "market_1": {
            "question": "Will temperature in NYC exceed 90°F on July 15, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will temperature in NYC exceed 95°F on July 15, 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_18",
        "market_1": {
            "question": "Will Nvidia stock be above $500 on March 1, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Nvidia stock be above $600 on March 1, 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    
    # OVERLAP (correlated but not equivalent)
    {
        "comparison_id": "comparison_19",
        "market_1": {
            "question": "Will the US enter a recession in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will unemployment rise above 5% in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_20",
        "market_1": {
            "question": "Will a Democrat win the 2028 presidential election?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Biden run for reelection in 2028?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_21",
        "market_1": {
            "question": "Will Apple release VR headset in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Apple stock hit all-time high in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    
    # UNRELATED
    {
        "comparison_id": "comparison_22",
        "market_1": {
            "question": "Will it rain in London on May 1, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Bitcoin be above $50,000 on May 1, 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_23",
        "market_1": {
            "question": "Will the Lakers make the playoffs in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Tesla stock split in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    
    # Edge cases - missing information
    {
        "comparison_id": "comparison_24",
        "market_1": {
            "question": "Will the Chiefs win the Super Bowl?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will the Chiefs win the 2026 Super Bowl?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_25",
        "market_1": {
            "question": "Will there be a government shutdown this year?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will there be a government shutdown in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    
    # Tricky wording - same event, different phrasing
    {
        "comparison_id": "comparison_26",
        "market_1": {
            "question": "Will Microsoft acquire Activision by June 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will the Microsoft-Activision deal close by June 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_27",
        "market_1": {
            "question": "Will COVID-19 vaccines be required for air travel in US in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will US mandate COVID vaccines for domestic flights in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_28",
        "market_1": {
            "question": "Will interest rates be cut by the Fed in H1 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will the Federal Reserve lower rates before July 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    
    # Multiple outcomes - compatibility testing
    {
        "comparison_id": "comparison_29",
        "market_1": {
            "question": "2025 World Series winner",
            "outcomes": ["Yankees", "Dodgers", "Other"]
        },
        "market_2": {
            "question": "Will the Yankees win the 2025 World Series?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_30",
        "market_1": {
            "question": "Next Fed chair",
            "outcomes": ["Powell", "Yellen", "Other"]
        },
        "market_2": {
            "question": "Will Powell remain Fed chair through 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    
    # Sports - team vs spread
    {
        "comparison_id": "comparison_31",
        "market_1": {
            "question": "NBA: Warriors vs Lakers - Jan 20, 2025",
            "outcomes": ["Warriors", "Lakers"]
        },
        "market_2": {
            "question": "Will Warriors beat Lakers by 5+ points on Jan 20, 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_32",
        "market_1": {
            "question": "NFL: Chiefs vs Bills - AFC Championship",
            "outcomes": ["Chiefs", "Bills"]
        },
        "market_2": {
            "question": "Will Chiefs cover -3.5 spread vs Bills in AFC Championship?",
            "outcomes": ["Yes", "No"]
        }
    },
    
    # Geography variations
    {
        "comparison_id": "comparison_33",
        "market_1": {
            "question": "Will it snow in NYC on Feb 1, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will it snow in Manhattan on Feb 1, 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_34",
        "market_1": {
            "question": "Will temperature exceed 100°F in Phoenix on July 4, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will temperature exceed 100°F in Arizona on July 4, 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    
    # Measurement unit differences
    {
        "comparison_id": "comparison_35",
        "market_1": {
            "question": "Will Ethereum be above $3000 on April 1, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Ethereum price on April 1, 2025",
            "outcomes": ["Above $3,000", "Below $3,000"]
        }
    },
    {
        "comparison_id": "comparison_36",
        "market_1": {
            "question": "Will oil price be above $85 per barrel on May 15, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "WTI crude price on May 15, 2025",
            "outcomes": ["Over $85/bbl", "Under $85/bbl"]
        }
    },
    
    # Political - specific vs general
    {
        "comparison_id": "comparison_37",
        "market_1": {
            "question": "Will Biden be the 2024 Democratic nominee?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will an incumbent president run in 2024?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_38",
        "market_1": {
            "question": "Will Newsom run for president in 2028?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will a California governor run for president in 2028?",
            "outcomes": ["Yes", "No"]
        }
    },
    
    # Economic indicators - related but different
    {
        "comparison_id": "comparison_39",
        "market_1": {
            "question": "Will GDP growth exceed 3% in Q1 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will the economy be in expansion in Q1 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_40",
        "market_1": {
            "question": "Will CPI inflation be below 2% in March 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will PCE inflation be below 2% in March 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    
    # Tech - version/release specificity
    {
        "comparison_id": "comparison_41",
        "market_1": {
            "question": "Will GPT-5 be released by end of 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will OpenAI release a new model by end of 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_42",
        "market_1": {
            "question": "Will iPhone 17 launch in September 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Apple announce new iPhone in fall 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    
    # Weather - different metrics
    {
        "comparison_id": "comparison_43",
        "market_1": {
            "question": "Will there be more than 2 inches of rain in Seattle on Jan 10, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will it rain heavily in Seattle on Jan 10, 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_44",
        "market_1": {
            "question": "Will wind speed exceed 50mph in Miami on Aug 15, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will there be tropical storm conditions in Miami on Aug 15, 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    
    # Market hours/timing edge cases
    {
        "comparison_id": "comparison_45",
        "market_1": {
            "question": "Will Bitcoin be above $75,000 at midnight UTC on Jan 1, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Bitcoin be above $75,000 at start of 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_46",
        "market_1": {
            "question": "Will Tesla close above $250 on trading day Dec 31, 2024?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Tesla stock price at end of 2024",
            "outcomes": ["Above $250", "Below $250"]
        }
    },
    
    # Series vs single game
    {
        "comparison_id": "comparison_47",
        "market_1": {
            "question": "Will the Celtics win Game 1 of the NBA Finals?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will the Celtics win the NBA Finals series?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_48",
        "market_1": {
            "question": "Will the Yankees sweep the Red Sox in their 3-game series?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will the Yankees win all games against the Red Sox this weekend?",
            "outcomes": ["Yes", "No"]
        }
    },
    
    # Exact same question - obvious match
    {
        "comparison_id": "comparison_49",
        "market_1": {
            "question": "Will SpaceX launch Starship to orbit in Q2 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will SpaceX launch Starship to orbit in Q2 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_50",
        "market_1": {
            "question": "Gold price on June 30, 2025",
            "outcomes": ["Above $2200", "Below $2200"]
        },
        "market_2": {
            "question": "Will gold be above $2200 on June 30, 2025?",
            "outcomes": ["Yes", "No"]
        }
    }
]