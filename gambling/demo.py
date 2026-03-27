#!/usr/bin/env python3
"""
Kalshi Trading Skill Demo Script

This script demonstrates how to use the Kalshi trading OpenClaw skill
with both real API tokens and mock data for testing.

Usage:
    python demo.py --mode=mock    # Run with mock data
    python demo.py --mode=real    # Run with real API (requires token)
    python demo.py --test         # Run comprehensive tests
"""

import asyncio
import argparse
import json
import os
from kalshi_trading import kalshi_trade, KalshiAPI, TradingStrategy


async def demo_with_mock_data():
    """
    Demonstrate skill functionality using mock data
    Perfect for testing without a real API token
    """
    print("🎭 Running Kalshi Trading Demo with Mock Data")
    print("=" * 50)
    
    # Mock context (OpenClaw provides this automatically)
    class MockContext:
        def __init__(self):
            self.user_id = "demo_user"
            self.session_id = "demo_session"
    
    ctx = MockContext()
    
    # Use a dummy token for demonstration
    dummy_token = "demo_token_12345_not_real"
    
    # Mock the API responses using patches
    from unittest.mock import patch, Mock
    
    print("\n1. 📊 Getting Market Data...")
    with patch('kalshi_trading.KalshiAPI') as mock_api_class:
        mock_api = Mock()
        mock_api.get_markets.return_value = {
            \"markets\": [
                {
                    \"ticker\": \"DEMO-ELECTION-2024\",
                    \"title\": \"Will the Democrat candidate win the 2024 election?\",
                    \"last_price\": 55,
                    \"volume\": 15420,
                    \"status\": \"active\"
                },
                {
                    \"ticker\": \"DEMO-TECH-RALLY\",
                    \"title\": \"Will tech stocks rally 10% this month?\",
                    \"last_price\": 34,
                    \"volume\": 8940,
                    \"status\": \"active\"
                }
            ],
            \"count\": 2
        }
        mock_api_class.return_value = mock_api
        
        result = await kalshi_trade(ctx, dummy_token, \"get_markets\")
        markets_data = json.loads(result)
        
        print(f\"✅ Found {len(markets_data['markets'])} active markets:\")
        for market in markets_data['markets']:
            print(f\"   • {market['ticker']}: {market['last_price']}¢ (Vol: {market['volume']:,})\")
    
    print(\"\n2. 🔍 Analyzing a Specific Market...\")
    with patch('kalshi_trading.KalshiAPI') as mock_api_class:
        mock_api = Mock()
        mock_api.get_market.return_value = {
            \"market\": {
                \"ticker\": \"DEMO-ELECTION-2024\",
                \"last_price\": 55,
                \"volume\": 15420,
                \"title\": \"Will the Democrat candidate win the 2024 election?\"
            }
        }
        mock_api.get_orderbook.return_value = {
            \"orderbook\": {
                \"yes\": {
                    \"bids\": [[54, 200], [53, 150], [52, 300]],
                    \"asks\": [[56, 180], [57, 220], [58, 100]]
                },
                \"no\": {
                    \"bids\": [[44, 180], [43, 200]],
                    \"asks\": [[46, 150], [47, 180]]
                }
            }
        }
        mock_api_class.return_value = mock_api
        
        result = await kalshi_trade(ctx, dummy_token, \"analyze\", market_id=\"DEMO-ELECTION-2024\")
        analysis = json.loads(result)
        
        print(f\"✅ Market Analysis for {analysis['market']}:\")
        print(f\"   📈 Current Price: {analysis['current_price']}¢\")
        print(f\"   📊 Volume: {analysis['volume']:,} contracts\")
        print(f\"   💰 Spread: {analysis['spread']}¢\")
        print(f\"   🌊 Liquidity: {analysis['liquidity']}\")
        print(f\"   🎯 Recommendation: {analysis['recommendation']}\")
    
    print(\"\n3. 💼 Checking Portfolio...\")
    with patch('kalshi_trading.KalshiAPI') as mock_api_class:
        mock_api = Mock()
        mock_api.get_portfolio.return_value = {
            \"portfolio\": {
                \"balance\": 5000,
                \"pnl\": 125,
                \"positions\": [
                    {
                        \"market_ticker\": \"DEMO-ELECTION-2024\",
                        \"side\": \"yes\",
                        \"position\": 25,
                        \"avg_price\": 52,
                        \"unrealized_pnl\": 75
                    }
                ]
            }
        }
        mock_api_class.return_value = mock_api
        
        result = await kalshi_trade(ctx, dummy_token, \"portfolio\")
        portfolio = json.loads(result)
        
        print(f\"✅ Portfolio Summary:\")
        print(f\"   💵 Balance: ${portfolio['portfolio']['balance']/100:.2f}\")
        print(f\"   📈 P&L: ${portfolio['portfolio']['pnl']/100:+.2f}\")
        print(f\"   📊 Positions: {len(portfolio['portfolio']['positions'])}\")
        
        for pos in portfolio['portfolio']['positions']:
            print(f\"     • {pos['market_ticker']}: {pos['position']} contracts @ {pos['avg_price']}¢ ({pos['side']})\")
    
    print(\"\n4. 🛒 Placing a Demo Order...\")
    with patch('kalshi_trading.KalshiAPI') as mock_api_class:
        mock_api = Mock()
        mock_api.get_market.return_value = {\"market\": {\"last_price\": 55}}
        mock_api.place_order.return_value = {
            \"order\": {
                \"id\": \"demo_order_789\",
                \"status\": \"open\",
                \"market_ticker\": \"DEMO-ELECTION-2024\",
                \"side\": \"yes\",
                \"action\": \"buy\",
                \"count\": 5,
                \"price\": 55,
                \"created_at\": \"2024-03-26T12:00:00Z\"
            }
        }
        mock_api_class.return_value = mock_api
        
        result = await kalshi_trade(\n            ctx, dummy_token, \"buy\",\n            market_id=\"DEMO-ELECTION-2024\",\n            amount=5,\n            side=\"yes\"\n        )
        order = json.loads(result)
        
        print(f\"✅ Order placed successfully:\")
        print(f\"   🆔 Order ID: {order['order']['id']}\")
        print(f\"   📊 Market: {order['order']['market_ticker']}\")
        print(f\"   🎯 Side: {order['order']['side']} ({order['order']['action']})\")
        print(f\"   💰 Amount: {order['order']['count']} contracts @ {order['order']['price']}¢\")
        print(f\"   📋 Status: {order['order']['status']}\")
    
    print(\"\n🎉 Demo completed successfully!\")
    print(\"\\n💡 Next steps:\")
    print(\"   1. Get a real Kalshi API token from https://kalshi.com\")
    print(\"   2. Set KALSHI_API_TOKEN environment variable\")
    print(\"   3. Run: python demo.py --mode=real\")


async def demo_with_real_api():
    """
    Demonstrate skill with real Kalshi API
    Requires KALSHI_API_TOKEN environment variable
    """
    print(\"🚀 Running Kalshi Trading Demo with Real API\")
    print(\"=\" * 50)
    
    # Get token from environment
    token = os.getenv(\"KALSHI_API_TOKEN\")
    if not token:
        print(\"❌ Error: KALSHI_API_TOKEN environment variable not set\")
        print(\"\\nTo get a token:\")
        print(\"   1. Sign up at https://kalshi.com\")
        print(\"   2. Generate API token in account settings\")
        print(\"   3. Set environment variable: export KALSHI_API_TOKEN=your_token\")
        return
    
    # Mock context
    class MockContext:
        pass
    
    ctx = MockContext()
    
    print(\"\\n1. 📊 Getting Real Market Data...\")
    try:
        result = await kalshi_trade(ctx, token, \"get_markets\")
        markets_data = json.loads(result)
        
        if \"error\" in markets_data:
            print(f\"❌ API Error: {markets_data['error']}\")
            return
        
        print(f\"✅ Found {len(markets_data.get('markets', []))} markets\")
        
        # Show first few markets
        for i, market in enumerate(markets_data.get(\"markets\", [])[:3]):
            print(f\"   {i+1}. {market.get('ticker', 'N/A')}: {market.get('last_price', 0)}¢\")
            
    except Exception as e:
        print(f\"❌ Error accessing API: {e}\")
        return
    
    print(\"\\n2. 💼 Getting Account Balance...\")
    try:
        result = await kalshi_trade(ctx, token, \"balance\")
        balance_data = json.loads(result)
        
        if \"error\" in balance_data:
            print(f\"❌ Error: {balance_data['error']}\")
        else:
            print(f\"✅ Account balance retrieved successfully\")
            # Note: Don't print actual balance for privacy
            
    except Exception as e:
        print(f\"❌ Error: {e}\")
    
    print(\"\\n✅ Real API demo completed!\")
    print(\"\\n⚠️  Remember: This uses real money. Trade responsibly!\")


def run_comprehensive_tests():
    \"\"\"Run the test suite\"\"\"
    print(\"🧪 Running Comprehensive Test Suite\")
    print(\"=\" * 50)
    
    try:
        # Run the demo tests from test file
        from test_kalshi_trading import run_demo_tests
        run_demo_tests()
        
        print(\"\\n✅ All tests passed! The skill is working correctly.\")
        
    except ImportError:
        print(\"❌ Test file not found. Make sure test_kalshi_trading.py is in the same directory.\")
    except Exception as e:
        print(f\"❌ Test error: {e}\")


def main():
    \"\"\"Main demo function with command line arguments\"\"\"
    parser = argparse.ArgumentParser(description=\"Kalshi Trading OpenClaw Skill Demo\")
    parser.add_argument(\n        \"--mode\", \n        choices=[\"mock\", \"real\"], \n        default=\"mock\",\n        help=\"Demo mode: 'mock' for fake data, 'real' for actual API\"\n    )\n    parser.add_argument(\n        \"--test\", \n        action=\"store_true\",\n        help=\"Run comprehensive test suite\"\n    )\n    \n    args = parser.parse_args()\n    \n    if args.test:\n        run_comprehensive_tests()\n    elif args.mode == \"mock\":\n        asyncio.run(demo_with_mock_data())\n    elif args.mode == \"real\":\n        asyncio.run(demo_with_real_api())\n    \n    print(\"\\n\" + \"=\" * 50)\n    print(\"📚 For more information, see README.md\")\n    print(\"🐛 Report issues at: https://github.com/your-repo/issues\")\n    print(\"📖 Kalshi API docs: https://kalshi.com/docs\")\n\n\nif __name__ == \"__main__\":\n    main()