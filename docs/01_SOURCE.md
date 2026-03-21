# SKILL: SOURCE — Lead Sourcing Engine

## Purpose
Find 200-300 raw companies per batch that match Holdex venture studio ICP. Tool-agnostic — works with web scraping, APIs, manual research, or AI-assisted search.

## Input
- **Vertical** (optional): RWA Tokenization | Institutional DeFi | Payments/Stablecoins | AI x Crypto | Fintech On-Chain | ALL
- **Batch size**: Target number of companies (default: 300)
- **Geo bias** (optional): APAC | EU | US | Global

## Output
CSV file with these columns:
```
company_name, website, vertical, description, founding_year, employee_count, funding_stage, funding_amount, last_funding_date, hq_location, source, source_url
```

## ICP Filter (must match ALL three)

### Filter 1: Build Problem
Company is building a financial product on blockchain and needs technical co-building. At least ONE of:
- No live product yet (landing page, waitlist, "coming soon")
- Pre-product or MVP stage
- Hiring engineers/product/design (signal they can't build alone)
- Participating in accelerator/incubator
- Founder bio mentions "building" / "launching" / "developing"

### Filter 2: Company Stage
- Employee count: 1-50 (sweet spot: 1-20)
- NOT exchanges, NOT pure advisory, NOT marketing agencies, NOT companies >100 people

### Filter 3: Funding / Ability to Pay
At least ONE of:
- Raised seed/pre-seed/Series A in last 18 months
- Token launch (TGE) planned or completed
- Ecosystem grant received
- Backed by known crypto VCs
- Revenue-generating protocol (TVL, fees)
- Serial founder with exit history

## Exclude
- Memecoins, NFT-only projects, GameFi with no financial product
- Pure advisory firms, exchanges, marketing agencies
- Companies >100 employees
- Projects with no funding signal AND no product signal

## Vertical Search Terms

### RWA Tokenization
RWA tokenization, real world assets, asset tokenization, security token, tokenized securities, digital securities, on-chain treasuries, tokenized real estate, tokenized private credit

### Institutional DeFi / CeDeFi
institutional DeFi, permissioned DeFi, on-chain lending, credit protocol, compliant yield, CeDeFi, regulated DeFi, institutional lending protocol

### Payments / Stablecoins
stablecoin infrastructure, crypto payments, cross-border settlement, on-chain payments, B2B crypto rails, remittance blockchain, payment protocol, stablecoin issuance

### AI x Crypto
decentralized AI, AI blockchain, on-chain AI, AI DeFi, DePIN AI, AI crypto infrastructure, decentralized compute, AI agents crypto, AI x web3

### Fintech Going On-Chain
fintech blockchain integration, fintech tokenization, fintech DeFi, on-chain fintech, blockchain fintech infrastructure, regulated fintech crypto

## Data Sources (in order of quality)

### Tier 1: Structured Databases (fastest)
1. **RootData** (rootdata.com) — Best Web3 project database. Has funding, team, category. Scrape or manual export.
2. **Crunchbase** — Filter: category = (fintech OR blockchain OR crypto OR DeFi) + funding stage = (seed OR Series A) + last funding < 18 months + employee count 1-50. Exclude "SaaS" tag for better results.
3. **DeFiLlama** — Protocols with TVL but small teams = active product, need builders. API: api.llama.fi
4. **CoinGecko** — Recently listed tokens with small market cap = early stage. Filter by category.

### Tier 2: Ecosystem Sources (higher quality, needs scraping)
5. **Accelerator cohort pages**: Outlier Ventures Base Camp, Alliance, Longhash, Techstars Crypto, a16z Crypto Startup School, Encode Club
6. **Ecosystem grant recipients**: Ethereum Foundation, Solana Foundation, Optimism, Arbitrum, Base, Polygon
7. **VC portfolio pages**: a16z crypto, Polychain, Paradigm, HashKey, Animoca, Dragonfly, Pantera
8. **Conference speaker lists**: Token2049, ETHDenver, Consensus, Next Block Expo, Devcon

### Tier 3: Intent Signals (highest quality, manual/AI-monitored)
9. **X/Twitter**: Founders posting about needing technical co-founders or build partners
10. **Job boards**: Crypto-specific roles on LinkedIn, crypto job boards (web3.career, cryptocurrencyjobs.co)
11. **Community**: Telegram groups, Discord servers, Farcaster where founders ask for dev recommendations

## Execution Workflow

### Step 1: Pull from Tier 1 sources
Use web search, API calls, or manual browsing to extract companies from RootData, Crunchbase, DeFiLlama. Target 60% of batch from here.

### Step 2: Pull from Tier 2 sources
Scrape or manually extract from accelerator pages, grant lists, VC portfolios. Target 30% of batch from here.

### Step 3: Fill gaps from Tier 3
Use AI-assisted search (Perplexity, Claude web search) to find recently announced projects, funded startups, founders posting about building. Target 10% of batch.

### Step 4: Deduplicate
Remove duplicate companies across sources. Keep the entry with the most complete data.

### Step 5: Tag verticals
For each company, assign one primary vertical from: RWA_TOKENIZATION, INSTITUTIONAL_DEFI, PAYMENTS_STABLECOINS, AI_CRYPTO, FINTECH_ONCHAIN, OTHER_DEFI

### Step 6: Export
Output as CSV with all columns populated. Mark any missing fields as "NEEDS_ENRICHMENT" rather than leaving blank.

## Quality Check
Before exporting, verify:
- [ ] Every company has a website or LinkedIn page
- [ ] Every company fits at least 1 of 3 filters (build problem, stage, funding)
- [ ] No excluded categories (memecoins, NFT-only, exchanges, >100 employees)
- [ ] Vertical tag is assigned
- [ ] No duplicates
- [ ] Source URL is recorded for each entry

## Notes
- Web3 databases (RootData, DeFiLlama) have better crypto coverage than Apollo/LinkedIn
- Crunchbase is good for funded startups but weak on pure-crypto projects
- Always cross-reference: a company on RootData may also be on Crunchbase with more funding data
- For AI-assisted research: ask "list 50 recently funded [vertical] startups with fewer than 50 employees" — then verify each one
- This skill produces COMPANIES, not PEOPLE. The ENRICH skill finds decision makers.
