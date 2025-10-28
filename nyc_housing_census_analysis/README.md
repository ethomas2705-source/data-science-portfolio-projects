# NYC Housing & Census Data Analysis

## Goal
Compare housing affordability across New York City neighborhoods by examining rent levels and household incomes.

## Dataset
Use housing rent data and census income data from NYC Open Data. The **Unit Income Rent** table reports the number of bedrooms, maximum allowable household income, and initial legal and actual rents for each unit ([catalog.data.gov](https://catalog.data.gov/dataset/?organization=city-of-new-york&q=income&sort=score+desc%2C+name+asc#:~:text=Law%2044%20,and%20actual%20rents%20for%20each)).

## Tools
- SQL (optional) for querying the datasets
- Python (Pandas, Matplotlib)

## Deliverable
A Python script that merges rent and income datasets by neighborhood, calculates the income‑to‑rent ratio, and visualizes affordability by borough.

## Resume Line
“Analyzed NYC housing and census data using SQL and Python to evaluate affordability trends by borough, producing a visual report on income‑to‑rent ratios.”

## Usage
1. Download relevant datasets from NYC Open Data (e.g., unit income rent and census income by neighborhood).
2. Save them as `housing.csv` and `income.csv` in this directory.
3. Run `analysis.py` to compute the income‑to‑rent ratio and plot the results.
