
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("your_dataset.csv")

# Descriptive statistics
desc_stats = data.describe()

# Correlation matrix visualization
plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Example visualization: Distribution of a numerical column
plt.figure(figsize=(8, 5))
sns.histplot(data['column_name'], kde=True)
plt.title("Distribution of Column_Name")
plt.show()

# Example descriptive analysis
print(desc_stats)
