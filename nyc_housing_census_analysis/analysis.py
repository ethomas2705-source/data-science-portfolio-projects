import pandas as pd
import matplotlib.pyplot as plt

def load_datasets(housing_path: str, income_path: str):
    housing_df = pd.read_csv(housing_path)
    income_df = pd.read_csv(income_path)
    return housing_df, income_df

def preprocess_and_merge(housing_df: pd.DataFrame, income_df: pd.DataFrame):
    # Example columns names; adjust based on actual dataset
    # Merge on neighborhood or borough column
    merged_df = pd.merge(housing_df, income_df, on="neighborhood", how="inner")
    # Compute income-to-rent ratio: average income / average rent
    merged_df["income_to_rent"] = merged_df["median_income"] / merged_df["average_rent"]
    return merged_df

def plot_affordability(merged_df: pd.DataFrame, group_col: str = "borough"):
    # Group by specified column and compute average income-to-rent ratio
    grouped = merged_df.groupby(group_col)["income_to_rent"].mean().reset_index()
    plt.figure()
    plt.bar(grouped[group_col], grouped["income_to_rent"])
    plt.xlabel(group_col.capitalize())
    plt.ylabel("Income to Rent Ratio")
    plt.title("Average Income-to-Rent Ratio by {}".format(group_col.capitalize()))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    housing_path = "housing.csv"
    income_path = "income.csv"
    housing_df, income_df = load_datasets(housing_path, income_path)
    merged_df = preprocess_and_merge(housing_df, income_df)
    plot_affordability(merged_df, group_col="borough")

if __name__ == "__main__":
    main()
