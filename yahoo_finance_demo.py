import yfinance as yf

def get_stock_info(symbol):
    """
    Get basic stock information for a given symbol
    """
    try:
        # Create a Ticker object
        stock = yf.Ticker(symbol)
        
        # Get basic stock info
        info = stock.info
        
        # Print some basic information
        print(f"\nStock Information for {symbol}:")
        print(f"Current Price: ${info.get('currentPrice', 'N/A')}")
        print(f"52 Week High: ${info.get('fiftyTwoWeekHigh', 'N/A')}")
        print(f"52 Week Low: ${info.get('fiftyTwoWeekLow', 'N/A')}")
        print(f"Market Cap: ${info.get('marketCap', 'N/A')}")
        
        return info
    except Exception as e:
        print(f"Error fetching data for {symbol}: {str(e)}")
        return None

if __name__ == "__main__":
    # Example usage
    symbol = "AAPL"  # Apple Inc.
    get_stock_info(symbol) 