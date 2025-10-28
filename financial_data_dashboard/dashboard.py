import pandas as pd
import matplotlib.pyplot as plt

# Uncomment the following import if you have yfinance installed
# import yfinance as yf

def load_stock_data(tickers, start_date, end_date):
    """Download historical price data for a list of tickers."""
    try:
        import yfinance as yf
    except ImportError:
        raise ImportError("yfinance is not installed. Install it with `pip install yfinance`.")
    data = yf.download(tickers, start=start_date, end=end_date, group_by='ticker', auto_adjust=True)
    return data

def compute_moving_average(series, window):
    """Compute a moving average for a price series."""
    return series.rolling(window=window).mean()

def plot_stock_with_moving_averages(ticker_data, ticker, windows=(50, 200)):
    """Plot the stock close price with moving averages."""
    plt.figure()
    plt.plot(ticker_data.index, ticker_data['Close'], label='Close')
    for window in windows:
        ma = compute_moving_average(ticker_data['Close'], window)
        plt.plot(ticker_data.index, ma, label=f'MA{window}')
    plt.title(f'{ticker} Stock Price with Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

def main():
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
    start_date = '2020-01-01'
    end_date = '2025-01-01'
    data = load_stock_data(tickers, start_date, end_date)
    for ticker in tickers:
        ticker_data = data[ticker]
        plot_stock_with_moving_averages(ticker_data, ticker, windows=(50, 200))

if __name__ == '__main__':
    main()
