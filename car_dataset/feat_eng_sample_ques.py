import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming df is the DataFrame containing the dataset
data = {
    'body-style': ['sedan', 'sedan', 'wagon', 'sedan', 'convertbl', 'convertbl', 'hatchback'],
    'num-of-doors': ['four', 'four', 'four', 'four', 'two', 'two', 'two'],
    'height': [55.9, 55.7, 55.5, 54.3, 48.8, 48.8, 54.1],
    'horsepower': [111, 154, 152, 110, 111, 111, 110],
    'peak-rpm': [5000, 5000, 5000, 5500, 5000, 5000, 5000],
    'price': [16500, 16500, 17450, 15250, 19350, 21950, 15550]
}
df = pd.DataFrame(data)

# Question 1: Displaying the data types
print(df.dtypes)

# Question 2: Correlation between 'height' and 'price'
correlation = df[['height', 'price']].corr()
print(correlation)

# Question 3: Statistical parameters
statistics = df[['height', 'peak-rpm', 'price', 'horsepower']].describe()
print(statistics)

# Question 4: Average price based on body-style
average_price = df.groupby('body-style')['price'].mean()
print(average_price)

# Question 5: Scatter plot and box plot
# Scatter plot
plt.figure(figsize=(10, 5))
sns.scatterplot(x='height', y='price', data=df)
plt.title('Scatter Plot of Height vs Price')
plt.xlabel('Height')
plt.ylabel('Price')
plt.show()

# Box plot
plt.figure(figsize=(10, 5))
sns.boxplot(x='body-style', y='price', data=df)
plt.title('Box Plot of Price by Body Style')
plt.xlabel('Body Style')
plt.ylabel('Price')
plt.show()