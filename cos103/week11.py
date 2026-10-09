import pandas as pd  # Reads and analyzes table data.
import matplotlib.pyplot as plt  # Creates visualizations of data.


# Load the dataset (keep Iris.csv in the same folder as this script).
iris = pd.read_csv("Iris.csv")

# Explore the dataset.
print("First five rows:")
print(iris.head())  # Preview the first five records.

print("\nDataset information:")
iris.info()  # Show column names, data types, and non-empty counts.

print("\nSummary statistics:")
print(iris.describe())  # Show count, mean, spread, and ranges.

print("\nMissing values in each column:")
print(iris.isnull().sum())  # Count missing values in each column.

print("\nNumber of flowers in each species:")
print(iris["Species"].value_counts())  # Count rows for each flower species.

# Plot histograms for the four flower measurements.
measurements = iris.drop(columns=["Id", "Species"])  # Keep only numeric measurements.
measurements.hist(figsize=(8, 6))  # Show each measurement's distribution.
plt.suptitle("Distributions of Iris Measurements")  # Add a title to the figure.
plt.tight_layout()  # Adjust spacing so labels do not overlap.
plt.show()  # Display the histograms.

# Compare sepal length and width for each species.
for species in iris["Species"].unique():
    species_data = iris[iris["Species"] == species]  # Select rows for this species.
    plt.scatter(
        species_data["SepalLengthCm"],
        species_data["SepalWidthCm"],
        label=species,  # Identify this species in the legend.
    )

plt.xlabel("Sepal Length (cm)")  # Label the horizontal axis.
plt.ylabel("Sepal Width (cm)")  # Label the vertical axis.
plt.title("Sepal Length vs Sepal Width")  # Title the scatter plot.
plt.legend()  # Show which points belong to each species.
plt.show()  # Display the scatter plot.

# Compare the number of flowers in each species.
iris["Species"].value_counts().plot(kind="bar")  # Draw a bar for each species count.
plt.xlabel("Species")  # Label the horizontal axis.
plt.ylabel("Number of Flowers")  # Label the vertical axis.
plt.title("Flowers per Species")  # Title the bar chart.
plt.tight_layout()  # Adjust spacing around the chart.
plt.show()  # Display the bar chart.

# Compare measurement ranges across species.
iris.boxplot(column="PetalLengthCm", by="Species")  # Compare petal lengths per species.
plt.title("Petal Length by Species")  # Set the box plot title.
plt.suptitle("")  # Remove the extra automatic title.
plt.xlabel("Species")  # Label the horizontal axis.
plt.ylabel("Petal Length (cm)")  # Label the vertical axis.
plt.show()  # Display the box plot.