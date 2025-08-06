import pandas as pd
import matplotlib.pyplot as plt

# Load the two separate Excel files from the 'data' folder
gdp_file = 'data/GDP_WorldBank.xlsx'
pop_file = 'data/Population_WorldBank.xlsx'

# Read Excel while skipping 4 metadata rows
gdp_df = pd.read_excel(gdp_file, skiprows=4)
pop_df = pd.read_excel(pop_file, skiprows=4)

# Check what columns exist
print("Actual column names in GDP sheet:", gdp_df.columns.tolist())
print("Actual column names in Population sheet:", pop_df.columns.tolist())

print("GDP Sheet (after skipping 4 rows):")
print(gdp_df.head())

print("\nPopulation Sheet (after skipping 4 rows):")
print(pop_df.head())

# ----------------------------------------------------------
# Data Cleaning (auto-detect year columns)
# ----------------------------------------------------------

# Detect columns whose names are like digits (years)
year_columns = [col for col in gdp_df.columns if str(col).isdigit()]

# Keep Country Name + those year columns only
gdp_df_clean = gdp_df[['Country Name'] + year_columns]
pop_df_clean = pop_df[['Country Name'] + year_columns]

# Convert from Wide to Long format
gdp_long = gdp_df_clean.melt(id_vars='Country Name', var_name='Year', value_name='GDP')
pop_long = pop_df_clean.melt(id_vars='Country Name', var_name='Year', value_name='Population')

print("\nCleaned GDP (long):")
print(gdp_long.head())

print("\nCleaned Population (long):")
print(pop_long.head())
# ----------------------------------------------------------
# Merge and calculate GDP per Capita
# ----------------------------------------------------------

merged = pd.merge(gdp_long, pop_long, on=['Country Name', 'Year'], how='inner')
merged['GDP_per_Capita'] = merged['GDP'] / merged['Population']

print("\nMerged & Calculated GDP_per_Capita:")
print(merged.head())

# Save to Excel for reference
merged.to_excel('outputs/merged_gdp_population.xlsx', index=False)
print("\nSaved merged file to outputs/merged_gdp_population.xlsx")
# ----------------------------------------------------------
# Plotting GDP and GDP per Capita trends
# ----------------------------------------------------------

# Create GDP trend chart per country
for country in merged['Country Name'].unique():
    temp = merged[merged['Country Name'] == country]

    # GDP Trend
    plt.figure()
    plt.plot(temp['Year'], temp['GDP'])
    plt.title(f"GDP Trend: {country}")
    plt.xlabel('Year')
    plt.ylabel('GDP')
    plt.savefig(f"outputs/{country}_GDP_trend.png")
    plt.close()

    # GDP per Capita Trend
    plt.figure()
    plt.plot(temp['Year'], temp['GDP_per_Capita'])
    plt.title(f"GDP per Capita Trend: {country}")
    plt.xlabel('Year')
    plt.ylabel('GDP per Capita')
    plt.savefig(f"outputs/{country}_GDP_per_capita_trend.png")
    plt.close()

print("\nCharts saved inside the 'outputs' folder.")
# ----------------------------------------------------------
# Analytical Questions
# ----------------------------------------------------------

# Convert Year column to numeric
merged['Year'] = merged['Year'].astype(int)

# 1️⃣ Which country has performed best (GDP per Capita growth) over the last 10 years?
latest10 = merged[merged['Year'] >= (merged['Year'].max() - 9)]  # filter last 10 years
summary_growth = latest10.groupby('Country Name')['GDP_per_Capita'].agg(['first', 'last'])
summary_growth['Growth_%'] = ((summary_growth['last'] - summary_growth['first']) / summary_growth['first'])*100
best_country = summary_growth['Growth_%'].idxmax()

print("\nBest performing country over the last 10 years (by GDP per Capita growth):", best_country)
print(summary_growth.sort_values(by='Growth_%', ascending=False))

# 2️⃣ Identify general/common patterns (you can comment later in Excel)
general_trends = merged.groupby('Year')['GDP_per_Capita'].mean()
print("\nAverage Overall GDP per Capita trend:\n", general_trends.head())
# ----------------------------------------------------------
# Analytical Questions
# ----------------------------------------------------------

# Convert Year col to integer
merged['Year'] = merged['Year'].astype(int)

# 1️⃣ Which country has performed best over the last 10 years (based on GDP per Capita growth)?
last_year = merged['Year'].max()
latest10 = merged[merged['Year'] >= last_year - 9]

growth_calc = latest10.groupby('Country Name')['GDP_per_Capita'].agg(['first', 'last'])
growth_calc['Growth_%'] = ((growth_calc['last'] - growth_calc['first']) / growth_calc['first']) * 100

best_country = growth_calc['Growth_%'].idxmax()
print("\nBest Performing Country over last 10 years:", best_country)
print(growth_calc.sort_values(by='Growth_%', ascending=False).head())

# 2️⃣ Look at general trend during last 20 years (avg across all countries)
last20 = merged[merged['Year'] >= last_year - 19]
overall_trend = last20.groupby('Year')['GDP_per_Capita'].mean()
print("\nAverage overall GDP per Capita trend over past 20 years:")
print(overall_trend)
# ----------------------------------------------------------
# Analytical Questions
# ----------------------------------------------------------

# Convert Year col to integer
merged['Year'] = merged['Year'].astype(int)

# 1️⃣ Which country has performed best over the last 10 years (GDP per Capita growth rate)?
last_year = merged['Year'].max()
latest10 = merged[merged['Year'] >= last_year - 9]

growth_calc = latest10.groupby('Country Name')['GDP_per_Capita'].agg(['first', 'last'])
growth_calc['Growth_%'] = ((growth_calc['last'] - growth_calc['first']) / growth_calc['first']) * 100

best_country = growth_calc['Growth_%'].idxmax()
print("\nBest Performing Country over last 10 years:", best_country)
print("\nTop 5 countries by GDP-per-capita growth in last 10 years:\n", growth_calc.sort_values(by='Growth_%', ascending=False).head())

# 2️⃣ Look at general average trend in GDP-per-capita for last 20 years
last20 = merged[merged['Year'] >= last_year - 19]
overall_trend = last20.groupby('Year')['GDP_per_Capita'].mean()
print("\nAverage Global GDP per Capita trend (past 20 years):\n", overall_trend)
print("---- END OF SCRIPT ----")

