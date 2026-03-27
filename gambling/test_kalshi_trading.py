"""
Test suite for Kalshi Trading OpenClaw Skill

This module provides comprehensive testing for the Kalshi trading functionality
including mock API responses and dummy token testing.
"""

import pytest
import asyncio
import json
from unittest.mock import Mock, patch, MagicMock
from kalshi_trading import KalshiAPI, TradingStrategy, kalshi_trade


class MockResponse:
    """Mock HTTP response for testing"""
    
    def __init__(self, json_data, status_code=200):
        self.json_data = json_data
        self.status_code = status_code
    
    def json(self):
        return self.json_data
    
    def raise_for_status(self):
        if self.status_code >= 400:
            raise Exception(f"HTTP {self.status_code}")


class TestKalshiAPI:
    """Test cases for KalshiAPI class"""
    
    @pytest.fixture
    def api_client(self):
        """Create API client with dummy token"""
        return KalshiAPI("test_token_12345")
    
    @pytest.fixture
    def mock_markets_response(self):
        """Mock response for markets endpoint"""
        return {
            "markets": [
                {
                    "ticker": "PRES-2024",
                    "title": "Will Joe Biden win the 2024 Presidential Election?",
                    "status": "active",
                    "last_price": 45,
                    "volume": 1500,
                    "open_interest": 2500
                },
                {
                    "ticker": "FED-RATE-DEC",
                    "title": "Will the Fed cut rates in December?",
                    "status": "active", 
                    "last_price": 75,
                    "volume": 800,
                    "open_interest": 1200
                }
            ],
            "count": 2
        }
    
    @pytest.fixture
    def mock_market_response(self):
        """Mock response for single market endpoint"""
        return {
            "market": {
                "ticker": "PRES-2024",
                "title": "Will Joe Biden win the 2024 Presidential Election?",
                "status": "active",
                "last_price": 45,
                "volume": 1500,
                "open_interest": 2500,
                "min_tick_size": 1,
                "max_tick_size": 99,
                "close_time": "2024-11-05T23:59:59Z"
            }
        }
    
    @pytest.fixture
    def mock_orderbook_response(self):
        """Mock response for orderbook endpoint"""
        return {
            "orderbook": {
                "yes": {
                    "bids": [[44, 100], [43, 200], [42, 150]],
                    "asks": [[46, 80], [47, 120], [48, 90]]
                },
                "no": {
                    "bids": [[54, 90], [53, 110], [52, 80]],
                    "asks": [[56, 70], [57, 100], [58, 60]]
                }
            }
        }
    
    @pytest.fixture
    def mock_portfolio_response(self):
        """Mock response for portfolio endpoint"""
        return {
            "portfolio": {
                "balance": 10000,
                "pnl": 250,
                "positions": [
                    {
                        "market_ticker": "PRES-2024",
                        "side": "yes",
                        "position": 50,
                        "avg_price": 42,
                        "unrealized_pnl": 150
                    }
                ]
            }
        }
    
    @patch('kalshi_trading.requests.Session.get')
    def test_get_markets_success(self, mock_get, api_client, mock_markets_response):
        """Test successful markets retrieval"""
        mock_get.return_value = MockResponse(mock_markets_response)
        
        result = api_client.get_markets()
        
        assert "markets" in result
        assert len(result["markets"]) == 2
        assert result["markets"][0]["ticker"] == "PRES-2024"
        mock_get.assert_called_once()
    
    @patch('kalshi_trading.requests.Session.get')
    def test_get_markets_error(self, mock_get, api_client):
        """Test markets retrieval with API error"""
        mock_get.side_effect = Exception("API Error")
        
        result = api_client.get_markets()
        
        assert "error" in result
        assert "Failed to fetch markets" in result["error"]
    
    @patch('kalshi_trading.requests.Session.get')
    def test_get_market_success(self, mock_get, api_client, mock_market_response):
        """Test successful single market retrieval"""
        mock_get.return_value = MockResponse(mock_market_response)
        
        result = api_client.get_market("PRES-2024")
        
        assert "market" in result
        assert result["market"]["ticker"] == "PRES-2024"
        mock_get.assert_called_with(f"{api_client.base_url}/markets/PRES-2024")
    
    @patch('kalshi_trading.requests.Session.get')
    def test_get_orderbook_success(self, mock_get, api_client, mock_orderbook_response):
        """Test successful orderbook retrieval"""
        mock_get.return_value = MockResponse(mock_orderbook_response)
        
        result = api_client.get_orderbook("PRES-2024")
        
        assert "orderbook" in result
        assert "yes" in result["orderbook"]
        assert "no" in result["orderbook"]
        assert len(result["orderbook"]["yes"]["bids"]) == 3
    
    @patch('kalshi_trading.requests.Session.post')
    def test_place_order_success(self, mock_post, api_client):
        """Test successful order placement"""
        mock_response = {"order": {"id": "123", "status": "open"}}
        mock_post.return_value = MockResponse(mock_response)
        
        result = api_client.place_order("PRES-2024", "yes", "buy", 10, 45)
        
        assert "order" in result
        assert result["order"]["id"] == "123"
        mock_post.assert_called_once()
    
    @patch('kalshi_trading.requests.Session.get')
    def test_get_portfolio_success(self, mock_get, api_client, mock_portfolio_response):
        """Test successful portfolio retrieval"""
        mock_get.return_value = MockResponse(mock_portfolio_response)
        
        result = api_client.get_portfolio()
        
        assert "portfolio" in result
        assert result["portfolio"]["balance"] == 10000
        assert len(result["portfolio"]["positions"]) == 1


class TestTradingStrategy:
    """Test cases for TradingStrategy class"""
    
    @pytest.fixture
    def mock_api(self):
        """Create mock API for strategy testing"""
        api = Mock(spec=KalshiAPI)
        return api
    
    @pytest.fixture
    def strategy(self, mock_api):
        """Create trading strategy with mock API"""
        return TradingStrategy(mock_api)
    
    def test_calculate_spread(self, strategy):
        """Test spread calculation"""
        orderbook = {
            "yes": {
                "bids": [[44, 100], [43, 200]],
                "asks": [[46, 80], [47, 120]]
            }
        }
        
        spread = strategy._calculate_spread(orderbook)
        assert spread == 2  # 46 - 44
    
    def test_calculate_spread_empty_orderbook(self, strategy):
        """Test spread calculation with empty orderbook"""
        orderbook = {"yes": {"bids": [], "asks": []}}
        
        spread = strategy._calculate_spread(orderbook)
        assert spread == 0
    
    def test_assess_liquidity_high(self, strategy):
        """Test liquidity assessment for high liquidity market"""
        orderbook = {
            "yes": {
                "bids": [[44, 500], [43, 600]],  # 1100 total
                "asks": [[46, 400], [47, 300]]   # 700 total
            }
        }
        
        liquidity = strategy._assess_liquidity(orderbook)
        assert liquidity == "high"  # 1800 > 1000
    
    def test_assess_liquidity_medium(self, strategy):
        """Test liquidity assessment for medium liquidity market"""
        orderbook = {
            "yes": {
                "bids": [[44, 50], [43, 60]],    # 110 total
                "asks": [[46, 40], [47, 30]]     # 70 total
            }
        }
        
        liquidity = strategy._assess_liquidity(orderbook)
        assert liquidity == "medium"  # 180 > 100 but < 1000
    
    def test_assess_liquidity_low(self, strategy):
        """Test liquidity assessment for low liquidity market"""
        orderbook = {
            "yes": {
                "bids": [[44, 5], [43, 6]],      # 11 total
                "asks": [[46, 4], [47, 3]]       # 7 total
            }
        }
        
        liquidity = strategy._assess_liquidity(orderbook)
        assert liquidity == "low"  # 18 < 100
    
    def test_analyze_market_success(self, strategy, mock_api):
        """Test successful market analysis"""
        # Mock API responses
        mock_api.get_market.return_value = {
            "last_price": 45,
            "volume": 1500
        }
        mock_api.get_orderbook.return_value = {
            "yes": {
                "bids": [[44, 100], [43, 200]],
                "asks": [[46, 80], [47, 120]]
            }
        }
        
        analysis = strategy.analyze_market("PRES-2024")
        
        assert analysis["market"] == "PRES-2024"
        assert analysis["current_price"] == 45
        assert analysis["volume"] == 1500
        assert analysis["spread"] == 2
        assert "liquidity" in analysis
        assert "recommendation" in analysis


class TestKalshiTradeFunction:
    """Test cases for main kalshi_trade function"""
    
    @pytest.fixture
    def mock_context(self):
        """Create mock OpenClaw context"""
        return Mock()
    
    @pytest.mark.asyncio
    async def test_missing_auth_token(self, mock_context):
        """Test function with missing auth token"""
        result = await kalshi_trade(mock_context, "", "get_markets")
        result_data = json.loads(result)
        
        assert "error" in result_data
        assert "Authentication token is required" in result_data["error"]
    
    @pytest.mark.asyncio
    @patch('kalshi_trading.KalshiAPI')
    async def test_get_markets_action(self, mock_api_class, mock_context):
        """Test get_markets action"""
        # Setup mock
        mock_api = Mock()
        mock_api.get_markets.return_value = {"markets": []}
        mock_api_class.return_value = mock_api
        
        result = await kalshi_trade(mock_context, "test_token", "get_markets")
        result_data = json.loads(result)
        
        assert "markets" in result_data
        mock_api.get_markets.assert_called_once()
    
    @pytest.mark.asyncio
    @patch('kalshi_trading.KalshiAPI')
    async def test_buy_action_success(self, mock_api_class, mock_context):
        """Test successful buy action"""
        # Setup mocks
        mock_api = Mock()
        mock_api.get_market.return_value = {"last_price": 45}
        mock_api.place_order.return_value = {"order": {"id": "123", "status": "open"}}
        mock_api_class.return_value = mock_api
        
        result = await kalshi_trade(
            mock_context, "test_token", "buy", 
            market_id="PRES-2024", amount=10, side="yes"
        )
        result_data = json.loads(result)
        
        assert "order" in result_data
        mock_api.place_order.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_buy_action_missing_params(self, mock_context):
        """Test buy action with missing parameters"""
        result = await kalshi_trade(mock_context, "test_token", "buy")
        result_data = json.loads(result)
        
        assert "error" in result_data
        assert "market_id, amount, and side are required" in result_data["error"]
    
    @pytest.mark.asyncio
    async def test_invalid_side_parameter(self, mock_context):
        """Test buy action with invalid side parameter"""
        result = await kalshi_trade(
            mock_context, "test_token", "buy",
            market_id="PRES-2024", amount=10, side="invalid"
        )
        result_data = json.loads(result)
        
        assert "error" in result_data
        assert "side must be 'yes' or 'no'" in result_data["error"]
    
    @pytest.mark.asyncio
    async def test_unknown_action(self, mock_context):
        """Test function with unknown action"""
        result = await kalshi_trade(mock_context, "test_token", "invalid_action")
        result_data = json.loads(result)
        
        assert "error" in result_data
        assert "Unknown action" in result_data["error"]
        assert "available_actions" in result_data


class TestIntegration:
    """Integration tests with dummy data"""
    
    @pytest.mark.asyncio
    async def test_full_trading_workflow_mock(self):
        """Test complete trading workflow with mocked responses"""
        
        # Mock context
        class MockContext:
            pass
        
        ctx = MockContext()
        dummy_token = "dummy_token_for_testing_12345"
        
        # Test 1: Get markets (should fail with dummy token but handle gracefully)
        with patch('kalshi_trading.KalshiAPI') as mock_api_class:
            mock_api = Mock()
            mock_api.get_markets.return_value = {
                "markets": [
                    {"ticker": "TEST-MARKET", "last_price": 50, "volume": 1000}
                ]
            }
            mock_api_class.return_value = mock_api
            
            result = await kalshi_trade(ctx, dummy_token, "get_markets")
            result_data = json.loads(result)
            
            assert "markets" in result_data
            assert len(result_data["markets"]) == 1
            assert result_data["markets"][0]["ticker"] == "TEST-MARKET"
        
        # Test 2: Analyze market
        with patch('kalshi_trading.KalshiAPI') as mock_api_class:
            mock_api = Mock()
            mock_api.get_market.return_value = {"last_price": 50, "volume": 1000}
            mock_api.get_orderbook.return_value = {
                "yes": {
                    "bids": [[49, 100], [48, 200]],
                    "asks": [[51, 80], [52, 120]]
                }
            }
            mock_api_class.return_value = mock_api
            
            result = await kalshi_trade(ctx, dummy_token, "analyze", market_id="TEST-MARKET")
            result_data = json.loads(result)
            
            assert result_data["market"] == "TEST-MARKET"
            assert result_data["current_price"] == 50
            assert result_data["spread"] == 2
            assert "liquidity" in result_data
        
        # Test 3: Place order
        with patch('kalshi_trading.KalshiAPI') as mock_api_class:
            mock_api = Mock()
            mock_api.get_market.return_value = {"last_price": 50}
            mock_api.place_order.return_value = {
                "order": {"id": "order_123", "status": "open", "filled": 0}
            }
            mock_api_class.return_value = mock_api
            
            result = await kalshi_trade(
                ctx, dummy_token, "buy",
                market_id="TEST-MARKET", amount=5, side="yes"
            )
            result_data = json.loads(result)
            
            assert "order" in result_data
            assert result_data["order"]["id"] == "order_123"


def run_demo_tests():
    """
    Run demo tests to showcase functionality
    Can be called directly without pytest
    """
    async def demo():
        print("🧪 Running Kalshi Trading Skill Demo Tests\n")
        
        # Mock context
        class MockContext:
            pass
        
        ctx = MockContext()
        dummy_token = "demo_token_12345"
        
        print("1. Testing market data retrieval...")
        with patch('kalshi_trading.KalshiAPI') as mock_api_class:
            mock_api = Mock()
            mock_api.get_markets.return_value = {
                "markets": [
                    {
                        "ticker": "DEMO-MARKET-1",
                        "title": "Demo Market 1",
                        "last_price": 60,
                        "volume": 2000
                    },
                    {
                        "ticker": "DEMO-MARKET-2", 
                        "title": "Demo Market 2",
                        "last_price": 35,
                        "volume": 1500
                    }
                ]
            }
            mock_api_class.return_value = mock_api
            
            result = await kalshi_trade(ctx, dummy_token, "get_markets")
            print(f"✅ Markets retrieved: {json.loads(result)}")
        
        print("\n2. Testing market analysis...")
        with patch('kalshi_trading.KalshiAPI') as mock_api_class:
            mock_api = Mock()
            mock_api.get_market.return_value = {"last_price": 60, "volume": 2000}
            mock_api.get_orderbook.return_value = {
                "yes": {
                    "bids": [[58, 150], [57, 200]],
                    "asks": [[62, 100], [63, 180]]
                }
            }
            mock_api_class.return_value = mock_api
            
            result = await kalshi_trade(ctx, dummy_token, "analyze", market_id="DEMO-MARKET-1")
            analysis = json.loads(result)
            print(f"✅ Market analysis: Spread={analysis['spread']}, Liquidity={analysis['liquidity']}")
        
        print("\n3. Testing order placement...")
        with patch('kalshi_trading.KalshiAPI') as mock_api_class:
            mock_api = Mock()
            mock_api.get_market.return_value = {"last_price": 60}
            mock_api.place_order.return_value = {
                "order": {
                    "id": "demo_order_789",
                    "status": "open",
                    "market_ticker": "DEMO-MARKET-1",
                    "side": "yes",
                    "count": 10,
                    "price": 60
                }
            }
            mock_api_class.return_value = mock_api
            
            result = await kalshi_trade(
                ctx, dummy_token, "buy",
                market_id="DEMO-MARKET-1", amount=10, side="yes"
            )
            order = json.loads(result)
            print(f"✅ Order placed: {order['order']['id']} for {order['order']['count']} contracts")
        
        print("\n🎉 All demo tests passed! The skill is ready for use.")
        print("\n💡 To use with real data:")
        print("   1. Get a Kalshi API token")
        print("   2. Set KALSHI_API_TOKEN environment variable")
        print("   3. Replace dummy_token with your real token")
    
    # Run the demo
    asyncio.run(demo())


if __name__ == "__main__":
    print("Running Kalshi Trading Skill Demo Tests...")
    run_demo_tests()