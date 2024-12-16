# Data Manipulation and Visualization with Python

## Objective
Learn how to manipulate and analyze data using Python libraries.

## Instructions

1. Work with libraries such as **Pandas** and **NumPy** to perform data manipulation tasks.
2. Use a publicly available dataset (Iris dataset) and perform tasks like filtering, grouping, and aggregating data.
3. Create basic data visualizations using **Matplotlib** and **Seaborn**.
4. Upload your data manipulation scripts and visualizations to your GitHub repository.

## Outcome
This task will enhance your ability to work with data in Python, a critical skill for any developer.

---

## Dataset: Iris Dataset
The Iris dataset is a classic dataset in machine learning, containing 150 samples of iris flowers, categorized into three species:
- Setosa
- Versicolor
- Virginica

### Features:
- `sepal_length`: Sepal length in cm
- `sepal_width`: Sepal width in cm
- `petal_length`: Petal length in cm
- `petal_width`: Petal width in cm
- `species`: The species of the iris flower

---

## Visualizations Created
Below are the visualizations implemented for the Iris dataset:

1. **Line Chart**
   - Visualizes the `sepal_length` across all samples.
2. **Area Chart**
   - Highlights the area under the curve for `sepal_length`.
3. **Bar Chart**
   - Displays the count of each iris species.
4. **Histogram**
   - Shows the distribution of `sepal_length`.
5. **Scatter Plot**
   - Plots the relationship between `sepal_length` and `sepal_width`.
6. **Bubble Chart**
   - Similar to the scatter plot but uses `petal_length` to size the bubbles.
7. **Pie Chart**
   - Illustrates the proportion of each iris species.
8. **Gauge Chart**
   - Displays the average `sepal_length` using an interactive gauge.
9. **Heatmap**
   - Shows correlations between numerical features in the dataset.

---

## How to Run the Code
1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```
2. **Install Dependencies:**
   Make sure you have Python installed. Then install the necessary libraries:
   ```bash
   pip install pandas matplotlib seaborn plotly
   ```
3. **Run the Script:**
   ```bash
   python script_name.py
   ```

---

## Sample Code Snippets

### Line Chart
```python
plt.plot(iris['sepal_length'], marker='o')
plt.title('Line Chart of Sepal Length')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.show()
```

### Heatmap
```python
iris_numeric = iris.select_dtypes(include=['float64', 'int64'])
corr = iris_numeric.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Heatmap of Correlations')
plt.show()
```

---

## Visualizations Example

| Visualization Type | Description |
|--------------------|-------------|
| Line Chart         | Tracks trends in Sepal Length over samples. |
| Area Chart         | Highlights variations in Sepal Length. |
| Bar Chart          | Displays species counts. |
| Histogram          | Visualizes the distribution of Sepal Length. |
| Scatter Plot       | Shows the relationship between Sepal Length and Sepal Width. |
| Bubble Chart       | Sizes bubbles based on Petal Length. |
| Pie Chart          | Represents the proportion of each species. |
| Gauge Chart        | Highlights average Sepal Length. |
| Heatmap            | Displays correlations between numerical features. |

---

## Files Included
1. `main.py`: Python script containing the data manipulation and visualization code.
2. `readme.md`: This file providing an overview of the project.

---

## Credits
- **Dataset Source:** [UCI Machine Learning Repository - Iris Dataset](https://archive.ics.uci.edu/ml/datasets/iris)
- Libraries Used:
  - Pandas
  - Matplotlib
  - Seaborn
  - Plotly

