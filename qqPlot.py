import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Load the dataset (replace 'dataset.csv' with the actual path to your dataset file)
data = pd.read_csv('premier_league_all_matches.csv')

# Extract the 'Home_xG' and 'Away_xG' columns
home_xg = data['Home_xG']
away_xg = data['Away_xG']

# Calculate quantiles from 0 to 1 with a step of 0.01 for both 'Home_xG' and 'Away_xG'
quantile_array = [i/100 for i in range(1, 100)]
quantiles_home_xg = home_xg.quantile(quantile_array)
quantiles_away_xg = away_xg.quantile(quantile_array)

# Create a Q-Q plot
plt.figure(figsize=(8, 6))
plt.scatter(quantiles_home_xg, quantiles_away_xg)
plt.xlabel("Quantiles of Home_xG")
plt.ylabel("Quantiles of Away_xG")
plt.title("Q-Q Plot : Comparing Home_xG and Away_xG Distributions")

# Add the identity line
min_value = min(quantiles_home_xg.min(), quantiles_away_xg.min())
max_value = max(quantiles_home_xg.max(), quantiles_away_xg.max())
plt.plot([min_value, max_value], [min_value, max_value], color='red', linestyle='--')
plt.show()