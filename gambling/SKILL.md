# Kalshi Trading Skill

## Overview
A comprehensive OpenClaw skill for opportunistic trading on Kalshi prediction markets using API authentication. This skill enables automated trading strategies based on market analysis and real-time data.

## Features
- Kalshi API integration with secure authentication
- Market data retrieval and analysis
- Order placement and portfolio management
- Real-time position monitoring
- Risk management and profit/loss tracking
- Opportunistic trading strategies

## Parameters
- `auth_token`: Kalshi API authentication token (required)
- `action`: Trading action to perform (required)
- `market_id`: Specific market identifier (optional)
- `amount`: Trade amount in cents (optional)
- `side`: Buy/sell direction (optional)
- `strategy`: Trading strategy to execute (optional)

## Environment Variables
- `KALSHI_API_TOKEN`: Your Kalshi API authentication token
- `KALSHI_API_BASE_URL`: Base URL for Kalshi API (default: https://trading-api.kalshi.com/trade-api/v2)

## Installation Requirements
```
requests>=2.28.0
pandas>=1.5.0
python-dotenv>=0.19.0
```

## Security Notes
- Store API tokens as environment variables
- Never commit tokens to version control
- Use secure token rotation practices
- Monitor API usage and rate limits

## Usage Examples
```python
# Get market data
await kalshi_trade(ctx, auth_token=token, action="get_markets")

# Place a buy order
await kalshi_trade(ctx, auth_token=token, action="buy", market_id="PRES-2024", amount=100, side="yes")

# Check portfolio
await kalshi_trade(ctx, auth_token=token, action="portfolio")
```

## Author
OpenClaw Kalshi Trading Skill v1.0