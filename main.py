import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
iris = pd.read_csv("iris.csv")

# Show basic info
print(iris.head())

# Line chart
plt.figure(figsize=(10, 6))
plt.plot(iris['sepal_length'], marker='o')
plt.title('Line Chart of Sepal Length')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.grid(True)
plt.show()

# Area chart
plt.figure(figsize=(10, 6))
plt.fill_between(iris.index, iris['sepal_length'], color="skyblue", alpha=0.4)
plt.title('Area Chart of Sepal Length')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.show()

# Bar chart
sns.countplot(x='species', data=iris)
plt.title('Bar Chart of Species Count')
plt.xlabel('Species')
plt.ylabel('Count')
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
plt.hist(iris['sepal_length'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(iris['sepal_length'], iris['sepal_width'], c='blue', edgecolors='k', alpha=0.6)
plt.title('Scatter Plot of Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.show()

# Bubble chart
plt.figure(figsize=(10, 6))
plt.scatter(iris['sepal_length'], iris['sepal_width'], s=iris['petal_length'] * 30, alpha=0.5, color='blue')
plt.title('Bubble Chart of Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.show()

# Pie chart
species_counts = iris['species'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', colors=['skyblue', 'orange', 'green'])
plt.title('Pie Chart of Species Distribution')
plt.show()

import plotly.graph_objects as go

# Create Gauge Chart for the average sepal length
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=iris['sepal_length'].mean(),
    title={'text': "Average Sepal Length (cm)"},
    gauge={'axis': {'range': [None, 10]},
           'bar': {'color': "skyblue"},
           'steps': [
               {'range': [0, 5], 'color': 'lightgreen'},
               {'range': [5, 8], 'color': 'yellow'},
               {'range': [8, 10], 'color': 'red'}
           ]}
))

fig.show()

# Exclude non-numerical columns
iris_numeric = iris.select_dtypes(include=['float64', 'int64'])

# Compute the correlation matrix
corr = iris_numeric.corr()

# Plot the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Heatmap of Correlations')
plt.show()

