# Azure Arbitrage Analyzer (AAA)

A real-time arbitrage detection system for prediction markets across Kalshi and Polymarket platforms.

## What It Does

AAA automatically identifies risk-free arbitrage opportunities by:
1. Fetching prediction markets from Kalshi and Polymarket APIs
2. Using AI embeddings to find semantically similar markets across platforms
3. Using LLM to determine which markets are truly equivalent
4. Alerting users to guaranteed profit opportunities

## How It Works

### Architecture

**Backend:**
- **Azure Functions** (serverless, timer-triggered every 15 minutes)
- **Neon PostgreSQL** with pgvector extension for similarity search
- **OpenAI API** for embeddings and market comparison
- **Azure Service Bus** for async message processing

**Frontend:**
- Container App displaying arbitrage opportunities (coming soon)

### The Pipeline
```
┌─────────────────────────────────────────────────────────────┐
│ 1. MARKET INGESTION (Azure Function: market-getter)        │
│    - Fetch markets from Kalshi & Polymarket APIs           │
│    - Store in PostgreSQL database                           │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. EVENT PROCESSING                                          │
│    - Group markets by event                                  │
│    - Generate canonical questions using GPT-4o-mini          │
│    - Create embeddings using OpenAI text-embedding-3-small   │
│    - Store embeddings as vectors in PostgreSQL               │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. SIMILARITY SEARCH                                         │
│    - Use pgvector cosine similarity (<=> operator)           │
│    - Find top 3 similar events across platforms              │
│    - Queue comparisons to Service Bus                        │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 4. LLM VERIFICATION (Azure Function: market-comparer)       │
│    - Analyze market pairs for logical equivalence           │
│    - Classify relationships: EQUIVALENT, NEGATION, SUBSET... │
│    - Confirm outcome mapping compatibility                   │
│    - Store verified arbitrage opportunities                  │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 5. FRONTEND DISPLAY                                          │
│    - Show arbitrage opportunities with:                      │
│      * Market questions & outcomes                           │
│      * Current odds from both platforms                      │
│      * Expected profit percentage                            │
│      * Direct links to place bets                            │
└─────────────────────────────────────────────────────────────┘
```

## Example Arbitrage Opportunity

**Kalshi Market:**
- Question: "Will Bitcoin close above $100,000 on Dec 31, 2025?"
- Outcomes: Yes ($0.45) / No ($0.55)

**Polymarket Market:**
- Question: "Bitcoin price at year end 2025"
- Outcomes: Over $100,000 ($0.52) / Under $100,000 ($0.48)

**Arbitrage:**
- Buy "Yes" on Kalshi for $0.45
- Buy "Under $100,000" on Polymarket for $0.48
- Total cost: $0.93
- Guaranteed payout: $1.00
- **Risk-free profit: $0.07 (7.5%)**

## Technical Highlights

### Vector Similarity Search
Uses OpenAI embeddings (1536 dimensions) and PostgreSQL's pgvector extension with cosine similarity:
```sql
WITH source AS (
    SELECT embedding 
    FROM events 
    WHERE id = 'polymarket-event-123'
)
SELECT 
    e.id,
    e.question,
    1 - (e.embedding <=> s.embedding) AS similarity
FROM events e
CROSS JOIN source s
WHERE e.platform = 'Kalshi'
  AND e.embedding IS NOT NULL
ORDER BY e.embedding <=> s.embedding
LIMIT 3;
```

### Database Schema
The database schema is determined by entity framework in the `/Data` project.

**Events Table:**
```sql
CREATE TABLE events (
    id TEXT PRIMARY KEY,
    platform TEXT NOT NULL,
    question TEXT,
    end_date TIMESTAMP,
    embedding vector(1536),  -- pgvector type
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

**Markets Table:**
```sql
CREATE TABLE markets (
    id TEXT PRIMARY KEY,
    event_id TEXT REFERENCES events(id),
    question TEXT,
    outcomes JSONB,  -- e.g., ["Yes", "No"]
    platform TEXT,
    end_date TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW()
);
```

