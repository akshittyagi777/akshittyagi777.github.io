# Kalshi Trading OpenClaw Skill

An OpenClaw skill for opportunistic trading on Kalshi prediction markets with secure API authentication.

## Features

- **Kalshi API Integration**: Full integration with Kalshi's trading API
- **Authentication**: Secure token-based authentication
- **Market Analysis**: Real-time market data and analysis tools
- **Order Management**: Place buy/sell orders with risk management
- **Portfolio Tracking**: Monitor positions, balance, and P&L
- **Opportunistic Trading**: Built for automated trading strategies

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your Kalshi API token
```

3. Configure your Kalshi API token in the `.env` file

## Usage

### As OpenClaw Skill

The skill is automatically registered with OpenClaw and can be called using:

```python
await kalshi_trade(ctx, 
    auth_token="your_token",
    action="get_markets"
)
```

### Standalone Usage

```python
from kalshi_trading import kalshi_trade

# Get available markets
result = await kalshi_trade(None, token, "get_markets")

# Analyze a specific market
result = await kalshi_trade(None, token, "analyze", market_id="PRES-2024")

# Place a buy order
result = await kalshi_trade(None, token, "buy", 
    market_id="PRES-2024", 
    amount=10, 
    side="yes"
)
```

## Available Actions

- `get_markets`: Retrieve all available markets
- `get_market`: Get specific market details
- `portfolio`: View current portfolio
- `balance`: Check account balance
- `positions`: View current positions
- `analyze`: Analyze market for trading opportunities
- `buy`: Place buy order
- `sell`: Place sell order

## Parameters

- `auth_token` (required): Your Kalshi API authentication token
- `action` (required): The action to perform
- `market_id` (optional): Market ticker for market-specific actions
- `amount` (optional): Number of contracts to trade
- `side` (optional): "yes" or "no" for market outcome
- `strategy` (optional): Trading strategy to use

## Security

- Store API tokens as environment variables
- Never commit tokens to version control
- Use secure token rotation practices
- Monitor API usage and rate limits

## Trading Strategies

The skill includes basic market analysis capabilities:

- Spread calculation
- Liquidity assessment
- Volume analysis
- Basic recommendations

Extend the `TradingStrategy` class to implement custom strategies.

## Error Handling

The skill includes comprehensive error handling for:
- API authentication failures
- Network errors
- Invalid parameters
- Rate limiting

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

MIT License - see LICENSE file for details

## Disclaimer

This tool is for educational and research purposes. Trading involves risk. Always do your own research and never risk more than you can afford to lose.