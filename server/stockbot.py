import pandas as pd

# Function to load the S&P 500 stock data from CSV
def load_sp500_data(file_path='./data/sp500.csv'):
    # Load the CSV data into a DataFrame
    df = pd.read_csv(file_path)
    # Ensure the 'date' column is in datetime format
    df['date'] = pd.to_datetime(df['date'])
    return df

# Function to get the highest stock on a given date
def get_highest_stock_on_date(date, data):
    # Filter the data for the given date
    daily_data = data[data['date'] == date]
    
    if daily_data.empty:
        print(f"No data available for {date}.")
        return None
    
    # Find the stock with the highest price for the day
    highest_stock = daily_data.loc[daily_data['high'].idxmax()]
    
    # Return the stock symbol, name, and highest price
    return highest_stock['Name'], highest_stock['high'], highest_stock['open'], highest_stock['close']

# Example usage
if __name__ == '__main__':
    # Load the S&P 500 data from the CSV file
    sp500_data = load_sp500_data()
    
    # Input: Enter a date (e.g., '2023-06-01')
    input_date = '2016-06-01'  # Example date (replace with the desired date)
    
    # Convert input date to datetime format
    input_date = pd.to_datetime(input_date)
    
    # Get the highest stock for the specified date
    result = get_highest_stock_on_date(input_date, sp500_data)
    
    if result:
        name, highest_price, open_price, close_price = result
        print(f"Highest stock on {input_date.strftime('%Y-%m-%d')}:")
        print(f"Stock Name: {name}")
        print(f"Opening Price: {open_price}")
        print(f"Closing Price: {close_price}")
        print(f"Highest Price: {highest_price}")