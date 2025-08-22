# Data Visualization Tool using Matplotlib & Seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (change path as needed)
file_path = "C:\\Users\\Shashwata\\Downloads\\amazon.csv"   # Replace with your CSV file path
df = pd.read_csv(file_path)

print("Dataset Loaded Successfully ✅")
print(df.head())

# Select chart type
def plot_chart(chart_type, x_axis, y_axis=None):
    plt.figure(figsize=(8,6))
    
    if chart_type == "Scatter Plot":
        sns.scatterplot(data=df, x=x_axis, y=y_axis)
        
    elif chart_type == "Line Chart":
        sns.lineplot(data=df, x=x_axis, y=y_axis)
        
    elif chart_type == "Bar Chart":
        sns.barplot(data=df, x=x_axis, y=y_axis)
        
    elif chart_type == "Histogram":
        sns.histplot(data=df, x=x_axis, bins=30, kde=True)
        
    elif chart_type == "Box Plot":
        sns.boxplot(data=df, x=x_axis, y=y_axis)
    
    plt.title(f"{chart_type} of {x_axis}" + (f" vs {y_axis}" if y_axis else ""))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Example usage
plot_chart("Scatter Plot", x_axis=df.columns[0], y_axis=df.columns[1])
plot_chart("Histogram", x_axis=df.columns[0])
plot_chart("Box Plot", x_axis=df.columns[0], y_axis=df.columns[1])
