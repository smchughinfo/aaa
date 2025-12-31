from . import *

# Test data set 3: Focus on tricky edge cases revealed by previous experiments
data["3"] = [
    # 1-10: Geographic precision tests
    {
        "comparison_id": "comparison_1",
        "market_1": {
            "question": "Will it rain in Manhattan on July 4, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will it rain in New York City on July 4, 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_2",
        "market_1": {
            "question": "Will Dallas hit 100°F on August 1, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Texas hit 100°F on August 1, 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_3",
        "market_1": {
            "question": "Snowfall in Chicago on Christmas 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Snowfall in Illinois on Christmas 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_4",
        "market_1": {
            "question": "Will Portland, Oregon see rain on March 15, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Portland metro area see rain on March 15, 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_5",
        "market_1": {
            "question": "Hurricane in Houston in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Hurricane in Gulf Coast in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_6",
        "market_1": {
            "question": "Will San Jose experience an earthquake magnitude 4+ in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Silicon Valley experience an earthquake magnitude 4+ in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_7",
        "market_1": {
            "question": "Temperature in Boston above 95°F on July 4, 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Temperature in Massachusetts above 95°F on July 4, 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_8",
        "market_1": {
            "question": "Will Atlanta get more than 3 inches of snow in January 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Atlanta metro get more than 3 inches of snow in January 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_9",
        "market_1": {
            "question": "Tornado in Oklahoma City in spring 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Tornado in Oklahoma in spring 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_10",
        "market_1": {
            "question": "Will Las Vegas hit 115°F in summer 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Nevada hit 115°F in summer 2025?",
            "outcomes": ["Yes", "No"]
        }
    },

    # 11-20: Outcome count mismatch tests
    {
        "comparison_id": "comparison_11",
        "market_1": {
            "question": "2025 NBA MVP",
            "outcomes": ["Curry", "Jokic", "Giannis", "Other"]
        },
        "market_2": {
            "question": "Will Curry win 2025 NBA MVP?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_12",
        "market_1": {
            "question": "Next Fed chair (if Powell leaves)",
            "outcomes": ["Brainard", "Williams", "Other"]
        },
        "market_2": {
            "question": "Will Brainard be the next Fed chair?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_13",
        "market_1": {
            "question": "2025 World Series winner",
            "outcomes": ["Yankees", "Dodgers"]
        },
        "market_2": {
            "question": "Will the Yankees win the 2025 World Series?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_14",
        "market_1": {
            "question": "Super Bowl LX winner",
            "outcomes": ["Chiefs", "Not Chiefs"]
        },
        "market_2": {
            "question": "Will the Chiefs win Super Bowl LX?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_15",
        "market_1": {
            "question": "2028 Presidential election winner",
            "outcomes": ["Democrat", "Republican", "Third Party"]
        },
        "market_2": {
            "question": "Will a Democrat win the 2028 Presidential election?",
            "outcomes": ["Yes", "No"]
        }
    },

    # 16-25: Product/Model/Company name precision
    {
        "comparison_id": "comparison_16",
        "market_1": {
            "question": "Will iPhone 17 be released in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Apple release a new phone in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_17",
        "market_1": {
            "question": "Will GPT-5 launch in H1 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will GPT-5 launch in H1 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_18",
        "market_1": {
            "question": "Will Tesla release Full Self-Driving v13 in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Tesla release a new FSD version in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_19",
        "market_1": {
            "question": "Will Meta release Llama 4 in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Facebook release Llama 4 in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_20",
        "market_1": {
            "question": "Will Anthropic release Claude 4 in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will an AI lab release a new frontier model in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_21",
        "market_1": {
            "question": "Will Google release Gemini 2.0 in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Google release a new AI model in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_22",
        "market_1": {
            "question": "Will Windows 12 launch in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Microsoft launch a new Windows version in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_23",
        "market_1": {
            "question": "Will PlayStation 6 be announced in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will Sony announce a new gaming console in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_24",
        "market_1": {
            "question": "Will Starship reach orbit in Q1 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will a SpaceX vehicle reach orbit in Q1 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_25",
        "market_1": {
            "question": "Will ChatGPT Pro subscription launch in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will OpenAI launch a new subscription tier in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },

    # 26-35: Stock market time precision edge cases
    {
        "comparison_id": "comparison_26",
        "market_1": {
            "question": "NVIDIA stock at 4pm ET on March 31, 2025",
            "outcomes": ["Above $900", "Below $900"]
        },
        "market_2": {
            "question": "NVIDIA at close on last trading day of Q1 2025",
            "outcomes": ["Above $900", "At or below $900"]
        }
    },
    {
        "comparison_id": "comparison_27",
        "market_1": {
            "question": "AMD stock price at market close December 31, 2025",
            "outcomes": ["$200+", "Under $200"]
        },
        "market_2": {
            "question": "AMD stock price at end of 2025",
            "outcomes": ["At least $200", "Below $200"]
        }
    },
    {
        "comparison_id": "comparison_28",
        "market_1": {
            "question": "Intel stock at EOD June 30, 2025",
            "outcomes": ["Above $50", "At or below $50"]
        },
        "market_2": {
            "question": "Will Intel stock end Q2 2025 above $50?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_29",
        "market_1": {
            "question": "Meta stock at 4pm Eastern on final Q4 2025 trading day",
            "outcomes": ["$500+", "Under $500"]
        },
        "market_2": {
            "question": "Meta stock at end of 2025",
            "outcomes": ["$500 or more", "Less than $500"]
        }
    },
    {
        "comparison_id": "comparison_30",
        "market_1": {
            "question": "Alphabet closing price on last day of trading in 2025",
            "outcomes": ["Above $180", "At or below $180"]
        },
        "market_2": {
            "question": "Google parent company stock at end of year 2025",
            "outcomes": ["Above $180", "Below or equal $180"]
        }
    },
    {
        "comparison_id": "comparison_31",
        "market_1": {
            "question": "Bitcoin price at midnight UTC on Jan 1, 2025",
            "outcomes": ["Above $100k", "Below $100k"]
        },
        "market_2": {
            "question": "Bitcoin price at end of 2024",
            "outcomes": ["Above $100k", "At or below $100k"]
        }
    },
    {
        "comparison_id": "comparison_32",
        "market_1": {
            "question": "Ethereum at 11:59pm on December 31, 2025",
            "outcomes": ["Above $5000", "Below $5000"]
        },
        "market_2": {
            "question": "Ethereum at end of 2025",
            "outcomes": ["Above $5000", "At or below $5000"]
        }
    },
    {
        "comparison_id": "comparison_33",
        "market_1": {
            "question": "S&P 500 intraday high on Dec 31, 2025",
            "outcomes": ["Above 6000", "Below 6000"]
        },
        "market_2": {
            "question": "S&P 500 at close on Dec 31, 2025",
            "outcomes": ["Above 6000", "At or below 6000"]
        }
    },
    {
        "comparison_id": "comparison_34",
        "market_1": {
            "question": "Dow Jones at opening bell on Jan 2, 2026",
            "outcomes": ["Above 45000", "Below 45000"]
        },
        "market_2": {
            "question": "Dow Jones at end of 2025",
            "outcomes": ["Above 45000", "At or below 45000"]
        }
    },
    {
        "comparison_id": "comparison_35",
        "market_1": {
            "question": "Tesla stock price at market close on trading day Dec 31, 2025",
            "outcomes": ["Above $350", "Below $350"]
        },
        "market_2": {
            "question": "Tesla stock price at end of year 2025",
            "outcomes": ["Above $350", "At or below $350"]
        }
    },

    # 36-45: Subtle negation and equivalence cases
    {
        "comparison_id": "comparison_36",
        "market_1": {
            "question": "Will inflation exceed 2% in December 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "December 2025 inflation rate",
            "outcomes": ["2% or less", "More than 2%"]
        }
    },
    {
        "comparison_id": "comparison_37",
        "market_1": {
            "question": "Will GDP growth surpass 3% in Q2 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Q2 2025 GDP growth",
            "outcomes": ["3% or below", "Above 3%"]
        }
    },
    {
        "comparison_id": "comparison_38",
        "market_1": {
            "question": "Will the Fed hold rates steady in March 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Fed rate action in March 2025",
            "outcomes": ["Change rates", "Keep unchanged"]
        }
    },
    {
        "comparison_id": "comparison_39",
        "market_1": {
            "question": "Will the S&P 500 have a positive year in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "S&P 500 annual return for 2025",
            "outcomes": ["Negative or zero", "Positive"]
        }
    },
    {
        "comparison_id": "comparison_40",
        "market_1": {
            "question": "Will unemployment rise in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Unemployment change in 2025",
            "outcomes": ["Stay same or fall", "Increase"]
        }
    },
    {
        "comparison_id": "comparison_41",
        "market_1": {
            "question": "Will home prices increase in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "US median home price change in 2025",
            "outcomes": ["Decrease or flat", "Rise"]
        }
    },
    {
        "comparison_id": "comparison_42",
        "market_1": {
            "question": "Will oil prices drop below $70 in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Oil price minimum in 2025",
            "outcomes": ["$70 or above", "Below $70"]
        }
    },
    {
        "comparison_id": "comparison_43",
        "market_1": {
            "question": "Will gold reach $3000/oz in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Gold price peak in 2025",
            "outcomes": ["Under $3000/oz", "$3000/oz or more"]
        }
    },
    {
        "comparison_id": "comparison_44",
        "market_1": {
            "question": "Will the dollar strengthen against the euro in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "EUR/USD exchange rate trend in 2025",
            "outcomes": ["Euro strengthens or flat", "Dollar strengthens"]
        }
    },
    {
        "comparison_id": "comparison_45",
        "market_1": {
            "question": "Will there be a stock market correction (10%+ drop) in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Maximum S&P 500 drawdown in 2025",
            "outcomes": ["Less than 10%", "10% or more"]
        }
    },

    # 46-50: Mixed challenging scenarios
    {
        "comparison_id": "comparison_46",
        "market_1": {
            "question": "Will the Lakers make the NBA playoffs in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will the Lakers finish in the top 10 in the Western Conference?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_47",
        "market_1": {
            "question": "Will there be a major tech IPO (valuation $10B+) in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Will a company go public at $10B+ valuation in 2025?",
            "outcomes": ["Yes", "No"]
        }
    },
    {
        "comparison_id": "comparison_48",
        "market_1": {
            "question": "Will Trump be the Republican nominee in 2024?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Republican nominee for 2024 presidential election",
            "outcomes": ["Trump", "Not Trump"]
        }
    },
    {
        "comparison_id": "comparison_49",
        "market_1": {
            "question": "Will Bitcoin ETF see net inflows in Q1 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Bitcoin ETF flows in Q1 2025",
            "outcomes": ["Net outflows or neutral", "Net inflows"]
        }
    },
    {
        "comparison_id": "comparison_50",
        "market_1": {
            "question": "Will Apple Vision Pro sales exceed 1 million units in 2025?",
            "outcomes": ["Yes", "No"]
        },
        "market_2": {
            "question": "Apple Vision Pro 2025 sales",
            "outcomes": ["1 million or fewer", "More than 1 million"]
        }
    }
]
