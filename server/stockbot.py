import requests
import pandas as pd

# Function to fetch stock data from Alpha Vantage API
def fetch_stock_data(symbol, interval='1min', api_key='3Q125KZNIUVPXGP2'):
    url = f"https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
        "apikey": api_key,
        "outputsize": "compact"
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    # Extract the time series data for the given interval
    time_series = data.get(f"Time Series ({interval})", {})
    if not time_series:
        return None
    
    # Convert the time series data to a pandas DataFrame
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    df = df.astype(float)
    df.index = pd.to_datetime(df.index)
    return df.sort_index()

# Function to get the top 20 stocks with the highest value
def get_top_20_high_prices(symbols, interval='1min', api_key='3Q125KZNIUVPXGP2'):
    stocks_data = []
    
    for symbol in symbols:
        try:
            df = fetch_stock_data(symbol, interval, api_key)
            if df is not None:
                max_price = df['High'].max()  # Get the highest price for this stock
                stocks_data.append((symbol, max_price))
            else:
                print(f"No data for {symbol}. Skipping...")
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
    
    # Sort stocks by their highest price and return top 20
    top_20 = sorted(stocks_data, key=lambda x: x[1], reverse=True)[:20]
    return top_20

# Load the list of S&P 500 companies from your CSV file
def load_sp500_companies():
    file_path = './data/sp500.csv' 
    # Load the S&P 500 symbols and names into a DataFrame
    df = pd.read_csv(file_path)
    return df['Symbol'].tolist()  # Return the list of stock symbols

# Example usage
if __name__ == '__main__':
    # Load S&P 500 symbols from CSV
    symbols = load_sp500_companies()
    
    # Get the top 20 stocks with the highest price
    top_20_stocks = get_top_20_high_prices(symbols)
    
    # Print the top 20 stocks and their highest prices
    for symbol, max_price in top_20_stocks:
        print(f"Symbol: {symbol}, Highest Price: {max_price}")
