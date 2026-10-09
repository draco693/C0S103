import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Load the Iris dataset.
iris = pd.read_csv("Iris.csv")

# Use the measurements to predict the species.
X = iris.drop(columns=["Id", "Species"])
y = iris["Species"]

# Split the data into training and testing sets.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y,
)

# Train the decision tree classifier.
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions and evaluate the model.
predictions = model.predict(X_test)

print(f"Accuracy:  {accuracy_score(y_test, predictions):.2f}")
print(f"Precision: {precision_score(y_test, predictions, average='macro'):.2f}")
print(f"Recall:    {recall_score(y_test, predictions, average='macro'):.2f}")