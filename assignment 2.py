students = [
    {"name": "Alice", "marks": 85, "cgpa": 8.5, "percentage": 85},
    {"name": "Bob", "marks": 70, "cgpa": 7.0, "percentage": 70},
    {"name": "Charlie", "marks": 90, "cgpa": 9.0, "percentage": 90},
    {"name": "David", "marks": 75, "cgpa": 7.5, "percentage": 75}
]
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Step 1: Data Collection (already done)

# Step 2: Data Preprocessing (not much to do in this simple example)

# Step 3: Model Training
X = [[student['marks'], student['cgpa']] for student in students]
y = [student['percentage'] for student in students]

model = LinearRegression()
model.fit(X, y)

# Step 4: Model Evaluation
predictions = model.predict(X)
mae = mean_absolute_error(y, predictions)
print("Mean Absolute Error:", mae)


