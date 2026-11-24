# Assignment 10: Data Visualization using Matplotlib
# Install the library with: python -m pip install matplotlib

import matplotlib.pyplot as plt

subjects = ["Python", "DS", "Math", "DBMS", "SE"]
marks = [85, 75, 90, 80, 70]

# 1. Line plot
plt.figure()
plt.plot(subjects, marks, marker="o")
plt.title("Line Plot - Subject Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Scatter plot
plt.figure()
plt.scatter(subjects, marks)
plt.title("Scatter Plot - Subject Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()

# 3. Box plot
plt.figure()
plt.boxplot(marks)
plt.title("Box Plot - Marks Distribution")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()

# 4. Bar chart
plt.figure()
plt.bar(subjects, marks)
plt.title("Bar Chart - Subject Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()

# 5. Pie chart
plt.figure()
plt.pie(marks, labels=subjects, autopct="%1.1f%%")
plt.title("Pie Chart - Marks Distribution")
plt.tight_layout()
plt.show()
