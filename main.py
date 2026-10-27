import numpy as np
import pandas as pd

# Generate 1000 student records

np.random.seed(42)

n = 1000

data = {
"Student_ID": range(1, n + 1),
"Name": [f"Student_{i}" for i in range(1, n + 1)],
"Course": np.random.choice(["BCA", "BBA", "B.Tech", "B.Com"], n),
"City": np.random.choice(["Dehradun", "Delhi", "Noida", "Jaipur"], n),
"Marks": np.random.randint(30, 101, n),
"Attendance": np.random.randint(50, 101, n)
}

df = pd.DataFrame(data)

# Save CSV and JSON files

df.to_csv("students.csv", index=False)
df.to_json("students.json", orient="records", indent=4)

print("1000 student records generated successfully!")
print(df.head())
print("Total records:", len(df))
# STEP 2: DATA ANALYSIS USING PANDAS

print("\n========== STUDENT DATA ANALYSIS ==========")

# 1. Total number of students

print("\nTotal Students:", len(df))

# 2. Average marks

print("Average Marks:", round(df["Marks"].mean(), 2))

# 3. Highest marks

print("Highest Marks:", df["Marks"].max())

# 4. Lowest marks

print("Lowest Marks:", df["Marks"].min())

# 5. Average attendance

print("Average Attendance:", round(df["Attendance"].mean(), 2))

# 6. Course-wise student count

print("\nStudents in Each Course:")
print(df["Course"].value_counts())

# 7. Course-wise average marks

print("\nAverage Marks by Course:")
print(df.groupby("Course")["Marks"].mean().round(2))

# 8. Check missing values

print("\nMissing Values:")
print(df.isnull().sum())

# 9. NumPy analysis

marks = df["Marks"].to_numpy()

print("\n========== NUMPY ANALYSIS ==========")
print("Total Marks:", np.sum(marks))
print("Median Marks:", np.median(marks))
print("Standard Deviation:", round(np.std(marks), 2))
import matplotlib.pyplot as plt
import os

# Create a folder to save graphs

os.makedirs("visualizations", exist_ok=True)

# Graph 1: Students in Each Course

df["Course"].value_counts().plot(kind="bar")

plt.title("Number of Students in Each Course")
plt.xlabel("Course")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("visualizations/course_count.png")
plt.show()

# Graph 2: Marks Distribution

plt.figure(figsize=(8, 5))

plt.hist(df["Marks"], bins=10, edgecolor="black")

plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("visualizations/marks_distribution.png")
plt.show()

# Graph 3: Average Marks by Course

avg_marks = df.groupby("Course")["Marks"].mean()

avg_marks.plot(kind="bar")

plt.title("Average Marks by Course")
plt.xlabel("Course")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig("visualizations/average_marks.png")
plt.show()

print("All graphs created successfully!")
# PASS AND FAIL ANALYSIS

# Assume students scoring 40 or above pass

df["Result"] = np.where(df["Marks"] >= 40, "Pass", "Fail")

print("\n========== PASS/FAIL ANALYSIS ==========")

print("\nPass and Fail Count:")
print(df["Result"].value_counts())

# Calculate pass percentage

pass_percentage = (df["Result"] == "Pass").mean() * 100

print("\nPass Percentage:", round(pass_percentage, 2), "%")

# Create Pass/Fail graph

df["Result"].value_counts().plot(kind="bar")

plt.title("Student Pass vs Fail")
plt.xlabel("Result")
plt.ylabel("Number of Students")
plt.tight_layout()

plt.savefig("visualizations/pass_fail.png")
plt.show()
# STEP 5: CSV AND JSON FILE ANALYSIS

print("\n========== CSV AND JSON ANALYSIS ==========")

# Read CSV file
df_csv = pd.read_csv("students.csv")

# Read JSON file
df_json = pd.read_json("students.json")

# Display total records
print("\nTotal CSV Records:", len(df_csv))
print("Total JSON Records:", len(df_json))

# Display file shapes
print("\nCSV Shape:", df_csv.shape)
print("JSON Shape:", df_json.shape)

# Check missing values
print("\nMissing Values in CSV:")
print(df_csv.isnull().sum())

print("\nMissing Values in JSON:")
print(df_json.isnull().sum())

# Compare both datasets
print("\n========== DATA COMPARISON ==========")

if df_csv.equals(df_json):
    print("CSV and JSON data are identical.")
else:
    print("CSV and JSON data are different.")


# STEP 6: ATTENDANCE ANALYSIS

print("\n========== ATTENDANCE ANALYSIS ==========")

# Calculate average attendance
print(
    "Average Attendance:",
    round(df["Attendance"].mean(), 2), "%"
)

# Students with attendance 75% or above
eligible_students = df[df["Attendance"] >= 75]

print(
    "Students with 75% or More Attendance:",
    len(eligible_students)
)

# Students with attendance below 75%
low_attendance = df[df["Attendance"] < 75]

print(
    "Students with Less Than 75% Attendance:",
    len(low_attendance)
)

# Create attendance graph
attendance_counts = [
    len(eligible_students),
    len(low_attendance)
]

plt.figure(figsize=(8, 5))

plt.bar(
    ["75% or More", "Below 75%"],
    attendance_counts
)

plt.title("Student Attendance Analysis")
plt.xlabel("Attendance Category")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.savefig("visualizations/attendance_analysis.png")
plt.show()

print("Attendance graph created successfully!")

# STEP 7: CITY-WISE ANALYSIS

print("\n========== CITY-WISE ANALYSIS ==========")

# Count students in each city
city_count = df["City"].value_counts()

print("\nStudents in Each City:")
print(city_count)

# Create city-wise graph
plt.figure(figsize=(8, 5))

city_count.plot(kind="bar")

plt.title("City-Wise Student Distribution")
plt.xlabel("City")
plt.ylabel("Number of Students")

plt.tight_layout()

plt.savefig("visualizations/city_wise_students.png")

plt.show()

print("City-wise graph created successfully!")


# STEP 8: FINAL STUDENT PERFORMANCE SUMMARY

print("\n========== FINAL PROJECT SUMMARY ==========")

# Student statistics
total_students = len(df)
average_marks = df["Marks"].mean()
highest_marks = df["Marks"].max()
lowest_marks = df["Marks"].min()
average_attendance = df["Attendance"].mean()

# Pass and fail counts
pass_count = (df["Marks"] >= 40).sum()
fail_count = (df["Marks"] < 40).sum()
pass_percentage = (pass_count / total_students) * 100

# Display final report
print("Total Students:", total_students)
print("Average Marks:", round(average_marks, 2))
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Average Attendance:", round(average_attendance, 2), "%")
print("Students Passed:", pass_count)
print("Students Failed:", fail_count)
print("Pass Percentage:", round(pass_percentage, 2), "%")

print("\nCourse-wise Student Count:")
print(df["Course"].value_counts())

print("\nCity-wise Student Count:")
print(df["City"].value_counts())

# Save student performance summary
summary = pd.DataFrame({
    "Metric": [
        "Total Students",
        "Average Marks",
        "Highest Marks",
        "Lowest Marks",
        "Average Attendance",
        "Students Passed",
        "Students Failed",
        "Pass Percentage"
    ],
    "Value": [
        total_students,
        round(average_marks, 2),
        highest_marks,
        lowest_marks,
        round(average_attendance, 2),
        pass_count,
        fail_count,
        round(pass_percentage, 2)
    ]
})

summary.to_csv("student_performance_summary.csv", index=False)

print("\nFinal summary saved successfully!")
print("File: student_performance_summary.csv")


