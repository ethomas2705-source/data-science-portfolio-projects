import pandas as pd
import matplotlib.pyplot as plt

def load_sales_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def analyze_sales(df: pd.DataFrame):
    category_sales = df.groupby('Category')['Sales'].sum().reset_index()
    region_profit = df.groupby('Region')['Profit'].sum().reset_index()
    return category_sales, region_profit

def plot_category_sales(category_sales: pd.DataFrame):
    plt.figure()
    plt.bar(category_sales['Category'], category_sales['Sales'])
    plt.title('Total Sales by Category')
    plt.xlabel('Category')
    plt.ylabel('Sales')
    plt.show()

def plot_region_profit(region_profit: pd.DataFrame):
    plt.figure()
    plt.bar(region_profit['Region'], region_profit['Profit'])
    plt.title('Total Profit by Region')
    plt.xlabel('Region')
    plt.ylabel('Profit')
    plt.show()

def main():
    df = load_sales_data('superstore_sales.csv')
    category_sales, region_profit = analyze_sales(df)
    plot_category_sales(category_sales)
    plot_region_profit(region_profit)
    print(category_sales)
    print(region_profit)

if __name__ == '__main__':
    main()
