# ===========================================
# Student Marks Analyzer using NumPy
# ===========================================

# Import NumPy library
import numpy as np

# Create a NumPy array of student marks
marks = np.array([78, 92, 65, 88, 95, 72, 81, 60])

# -----------------------------
# Array Properties
# -----------------------------

# Shape shows the structure of the array
print("Shape:", marks.shape)

# Size shows total number of elements
print("Size:", marks.size)

# Data type of the array
print("Data Type:", marks.dtype)

# Number of dimensions
print("Dimensions:", marks.ndim)

print()

# -----------------------------
# Indexing
# -----------------------------

# First student's marks
print("First Student:", marks[0])

# Last student's marks
print("Last Student:", marks[-1])

print()

# -----------------------------
# Slicing
# -----------------------------

# Display marks from index 2 to 5
print("Marks from index 2 to 5:")
print(marks[2:6])

print()

# -----------------------------
# Reshaping
# -----------------------------

# Convert 1D array into 2 rows and 4 columns
reshaped = marks.reshape(2,4)

print("Reshaped Array:")
print(reshaped)

print()

# -----------------------------
# Broadcasting
# -----------------------------

# Add 5 bonus marks to every student
bonus_marks = marks + 5

print("Marks After Bonus:")
print(bonus_marks)

print()

# -----------------------------
# Universal Functions
# -----------------------------

# Square root of every mark
print("Square Root:")
print(np.sqrt(marks))

print()

# -----------------------------
# Student Marks Analysis
# -----------------------------

# Calculate average marks
average = np.mean(marks)

# Find highest marks
highest = np.max(marks)

# Find lowest marks
lowest = np.min(marks)

# Calculate standard deviation
std = np.std(marks)

# Find students scoring above 80
above_80 = marks[marks > 80]

# Display results
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Standard Deviation:", std)

print()

print("Students Scoring Above 80:")
print(above_80)
