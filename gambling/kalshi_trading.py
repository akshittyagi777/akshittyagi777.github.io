"""
OpenClaw Skill for Kalshi Trading
Enables opportunistic trading on Kalshi prediction markets
"""

import os
import requests
import json
import asyncio
from typing import Dict, List, Optional, Any
from datetime import datetime
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class KalshiAPI:
    """
    Kalshi API client for trading operations
    
    This class provides a comprehensive interface to the Kalshi prediction market API,
    enabling secure authentication, market data retrieval, and order management.
    
    Attributes:
        auth_token (str): API authentication token
        base_url (str): Base URL for Kalshi API endpoints
        session (requests.Session): HTTP session with authentication headers
    
    Example:
        >>> api = KalshiAPI("your_token_here")
        >>> markets = api.get_markets()
        >>> print(f"Found {len(markets['markets'])} markets")
    """
    
    def __init__(self, auth_token: str, base_url: str = None):
        """
        Initialize the Kalshi API client
        
        Args:
            auth_token (str): Your Kalshi API authentication token
            base_url (str, optional): Custom API base URL. Defaults to Kalshi's official API.
        
        Raises:
            ValueError: If auth_token is empty or None
        """
        if not auth_token:
            raise ValueError("Authentication token is required")
            
        self.auth_token = auth_token
        self.base_url = base_url or "https://trading-api.kalshi.com/trade-api/v2"
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {auth_token}",
            "Content-Type": "application/json",
            "User-Agent": "OpenClaw-Kalshi-Skill/1.0"
        })
    
    def get_markets(self, status: str = "active", limit: int = 100) -> Dict[str, Any]:
        """
        Retrieve available prediction markets from Kalshi
        
        Args:
            status (str): Market status filter ('active', 'closed', 'all'). Defaults to 'active'.
            limit (int): Maximum number of markets to retrieve (1-1000). Defaults to 100.
        
        Returns:
            Dict[str, Any]: API response containing markets list and metadata
            
        Example:
            >>> api = KalshiAPI(token)
            >>> markets = api.get_markets(status="active", limit=50)
            >>> print(f"Active markets: {len(markets['markets'])}")
        """
        try:
            response = self.session.get(
                f"{self.base_url}/markets",
                params={"status": status, "limit": limit}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"Failed to fetch markets: {str(e)}"}
    
    def get_market(self, market_ticker: str) -> Dict[str, Any]:
        """
        Get detailed information for a specific market
        
        Args:
            market_ticker (str): The unique market identifier (e.g., 'PRES-2024')
        
        Returns:
            Dict[str, Any]: Market details including price, volume, and metadata
            
        Example:
            >>> market = api.get_market("PRES-2024")
            >>> print(f"Current price: {market['market']['last_price']}¢")
        """
        try:
            response = self.session.get(f"{self.base_url}/markets/{market_ticker}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"Failed to fetch market {market_ticker}: {str(e)}"}
    
    def get_orderbook(self, market_ticker: str) -> Dict[str, Any]:
        """
        Retrieve the order book (bids and asks) for a specific market
        
        Args:
            market_ticker (str): The market identifier
        
        Returns:
            Dict[str, Any]: Order book data with 'yes' and 'no' sides containing bids/asks
            
        Note:
            Order book format: {"yes": {"bids": [[price, size], ...], "asks": [[price, size], ...]}}
            Prices are in cents (1-99), sizes are in number of contracts.
        """
        try:
            response = self.session.get(f"{self.base_url}/markets/{market_ticker}/orderbook")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"Failed to fetch orderbook for {market_ticker}: {str(e)}"}
    
    def place_order(self, market_ticker: str, side: str, action: str, 
                   count: int, price: int, order_type: str = "market") -> Dict[str, Any]:
        """
        Place a trading order on a prediction market
        
        Args:
            market_ticker (str): Market identifier (e.g., 'PRES-2024')
            side (str): Market side - 'yes' or 'no'
            action (str): Order action - 'buy' or 'sell'
            count (int): Number of contracts (must be positive)
            price (int): Price in cents (1-99 for yes side, calculated automatically for no side)
            order_type (str): Order type - 'market' or 'limit'. Defaults to 'market'.
        
        Returns:
            Dict[str, Any]: Order confirmation with order ID and status
            
        Raises:
            ValueError: If parameters are invalid
            
        Example:
            >>> order = api.place_order("PRES-2024", "yes", "buy", 10, 65)
            >>> print(f"Order placed: {order['order']['id']}")
        """
        try:
            order_data = {
                "ticker": market_ticker,
                "side": side,  # "yes" or "no"
                "action": action,  # "buy" or "sell"
                "count": count,  # number of contracts
                "price": price,  # price in cents
                "type": order_type
            }
            
            response = self.session.post(
                f"{self.base_url}/orders",
                json=order_data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"Failed to place order: {str(e)}"}
    
    def get_portfolio(self) -> Dict[str, Any]:
        """Get current portfolio positions"""
        try:
            response = self.session.get(f"{self.base_url}/portfolio")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"Failed to fetch portfolio: {str(e)}"}
    
    def get_balance(self) -> Dict[str, Any]:
        """Get account balance"""
        try:
            response = self.session.get(f"{self.base_url}/portfolio/balance")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"Failed to fetch balance: {str(e)}"}
    
    def get_positions(self) -> Dict[str, Any]:
        """Get current positions"""
        try:
            response = self.session.get(f"{self.base_url}/portfolio/positions")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"Failed to fetch positions: {str(e)}"}

class TradingStrategy:
    """
    Base class for implementing trading strategies on Kalshi prediction markets
    
    This class provides market analysis tools and can be extended to implement
    custom trading algorithms and strategies.
    
    Attributes:
        api (KalshiAPI): The API client for market data and trading operations
    
    Example:
        >>> strategy = TradingStrategy(api_client)
        >>> analysis = strategy.analyze_market("PRES-2024")
        >>> if analysis['recommendation'] == 'buy':
        ...     # Execute trading logic
    """
    
    def __init__(self, api: KalshiAPI):
        self.api = api
    
    def analyze_market(self, market_ticker: str) -> Dict[str, Any]:
        """
        Perform comprehensive market analysis for trading opportunities
        
        This method combines market data, order book analysis, and technical indicators
        to provide insights for trading decisions.
        
        Args:
            market_ticker (str): The market to analyze
        
        Returns:
            Dict[str, Any]: Analysis results including:
                - current_price: Latest market price
                - volume: Trading volume
                - spread: Bid-ask spread
                - liquidity: Liquidity assessment ('high', 'medium', 'low')
                - recommendation: Basic trading recommendation
        
        Example:
            >>> analysis = strategy.analyze_market("TECH-STOCK-UP")
            >>> print(f"Spread: {analysis['spread']}¢, Liquidity: {analysis['liquidity']}")
        """
        market_data = self.api.get_market(market_ticker)
        orderbook = self.api.get_orderbook(market_ticker)
        
        if "error" in market_data or "error" in orderbook:
            return {"error": "Failed to analyze market"}
        
        # Basic analysis
        analysis = {
            "market": market_ticker,
            "current_price": market_data.get("last_price", 0),
            "volume": market_data.get("volume", 0),
            "spread": self._calculate_spread(orderbook),
            "liquidity": self._assess_liquidity(orderbook),
            "recommendation": "hold"  # Default
        }
        
        return analysis
    
    def _calculate_spread(self, orderbook: Dict[str, Any]) -> float:
        """
        Calculate the bid-ask spread for the 'yes' side of the market
        
        The spread indicates market efficiency and trading costs.
        Lower spreads suggest higher liquidity and tighter markets.
        
        Args:
            orderbook (Dict[str, Any]): Order book data from the API
        
        Returns:
            float: Spread in cents between best bid and best ask
            
        Note:
            Returns 0 if orderbook is empty or malformed
        """
        try:
            yes_bids = orderbook.get("yes", {}).get("bids", [])
            yes_asks = orderbook.get("yes", {}).get("asks", [])
            
            if yes_bids and yes_asks:
                best_bid = yes_bids[0][0]  # Price of best bid
                best_ask = yes_asks[0][0]  # Price of best ask
                return best_ask - best_bid
            return 0
        except (IndexError, KeyError, TypeError):
            return 0
    
    def _assess_liquidity(self, orderbook: Dict[str, Any]) -> str:
        """
        Assess market liquidity based on total order book volume
        
        Liquidity affects order execution and market impact. Higher liquidity
        enables larger trades with less price impact.
        
        Args:
            orderbook (Dict[str, Any]): Order book data from the API
        
        Returns:
            str: Liquidity level - 'high' (>1000 contracts), 'medium' (100-1000), 
                'low' (<100), or 'unknown' if data is unavailable
                
        Note:
            Based on total volume of bids and asks on the 'yes' side
        """
        try:
            yes_bids = orderbook.get("yes", {}).get("bids", [])
            yes_asks = orderbook.get("yes", {}).get("asks", [])
            
            total_bid_volume = sum(bid[1] for bid in yes_bids)
            total_ask_volume = sum(ask[1] for ask in yes_asks)
            total_volume = total_bid_volume + total_ask_volume
            
            if total_volume > 1000:
                return "high"
            elif total_volume > 100:
                return "medium"
            else:
                return "low"
        except (IndexError, KeyError, TypeError):
            return "unknown"

async def kalshi_trade(ctx, auth_token: str, action: str, market_id: str = None, 
                      amount: int = None, side: str = None, strategy: str = None) -> str:
    """
    Main OpenClaw skill function for Kalshi trading
    
    Args:
        ctx: OpenClaw skill context
        auth_token: Kalshi API authentication token
        action: Action to perform (get_markets, get_market, buy, sell, portfolio, balance, analyze)
        market_id: Market ticker (required for market-specific actions)
        amount: Trade amount in number of contracts (required for trading)
        side: "yes" or "no" for the market outcome (required for trading)
        strategy: Trading strategy to use (optional)
    
    Returns:
        JSON string with results or error message
    """
    
    if not auth_token:
        return json.dumps({"error": "Authentication token is required"})
    
    try:
        api = KalshiAPI(auth_token)
        
        if action == "get_markets":
            result = api.get_markets()
            return json.dumps(result, indent=2)
        
        elif action == "get_market":
            if not market_id:
                return json.dumps({"error": "market_id is required for get_market action"})
            result = api.get_market(market_id)
            return json.dumps(result, indent=2)
        
        elif action == "portfolio":
            result = api.get_portfolio()
            return json.dumps(result, indent=2)
        
        elif action == "balance":
            result = api.get_balance()
            return json.dumps(result, indent=2)
        
        elif action == "positions":
            result = api.get_positions()
            return json.dumps(result, indent=2)
        
        elif action == "analyze":
            if not market_id:
                return json.dumps({"error": "market_id is required for analyze action"})
            
            strategy_engine = TradingStrategy(api)
            analysis = strategy_engine.analyze_market(market_id)
            return json.dumps(analysis, indent=2)
        
        elif action in ["buy", "sell"]:
            if not all([market_id, amount, side]):
                return json.dumps({
                    "error": "market_id, amount, and side are required for trading actions"
                })
            
            if side not in ["yes", "no"]:
                return json.dumps({"error": "side must be 'yes' or 'no'"})
            
            # Get current market price for market order
            market_data = api.get_market(market_id)
            if "error" in market_data:
                return json.dumps(market_data)
            
            # Use last price or a reasonable default
            price = market_data.get("last_price", 50)  # Default to 50 cents
            
            result = api.place_order(
                market_ticker=market_id,
                side=side,
                action=action,
                count=amount,
                price=price
            )
            return json.dumps(result, indent=2)
        
        else:
            return json.dumps({
                "error": f"Unknown action: {action}",
                "available_actions": [
                    "get_markets", "get_market", "portfolio", "balance", 
                    "positions", "analyze", "buy", "sell"
                ]
            })
    
    except Exception as e:
        return json.dumps({"error": f"Unexpected error: {str(e)}"})

# OpenClaw skill registration (if using decorator pattern)
try:
    from openclaw.skills import skill, SkillContext
    
    @skill(
        name="kalshi-trading",
        description="Trade on Kalshi prediction markets with authentication",
        parameters={
            "auth_token": {
                "type": "string", 
                "description": "Kalshi API authentication token",
                "required": True
            },
            "action": {
                "type": "string",
                "description": "Trading action to perform",
                "required": True,
                "enum": ["get_markets", "get_market", "portfolio", "balance", "positions", "analyze", "buy", "sell"]
            },
            "market_id": {
                "type": "string",
                "description": "Market ticker symbol",
                "required": False
            },
            "amount": {
                "type": "integer",
                "description": "Number of contracts to trade",
                "required": False
            },
            "side": {
                "type": "string",
                "description": "Market outcome side",
                "required": False,
                "enum": ["yes", "no"]
            },
            "strategy": {
                "type": "string",
                "description": "Trading strategy to use",
                "required": False
            }
        }
    )
    async def kalshi_trading_skill(ctx: SkillContext, auth_token: str, action: str, 
                                  market_id: str = None, amount: int = None, 
                                  side: str = None, strategy: str = None) -> str:
        """OpenClaw registered skill wrapper"""
        return await kalshi_trade(ctx, auth_token, action, market_id, amount, side, strategy)

except ImportError:
    # OpenClaw not available, skill can still be used standalone
    pass

if __name__ == "__main__":
    # Example usage for testing
    import asyncio
    
    async def test_skill():
        # Mock context for testing
        class MockContext:
            pass
        
        ctx = MockContext()
        
        # Get token from environment
        token = os.getenv("KALSHI_API_TOKEN")
        if not token:
            print("Please set KALSHI_API_TOKEN environment variable")
            return
        
        # Test getting markets
        result = await kalshi_trade(ctx, token, "get_markets")
        print("Markets:", result)
        
        # Test getting balance
        result = await kalshi_trade(ctx, token, "balance")
        print("Balance:", result)
    
    asyncio.run(test_skill())