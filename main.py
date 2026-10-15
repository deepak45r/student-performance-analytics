import pandas as pd
import numpy as np
df = pd.read_csv("students.csv")
df.columns = df.columns.str.strip()
subjects = ["Pythone", "NumPy", "Pandas"]
#df.loc[0, ["Pythone", "NumPy", "Pandas"]]

def calculate_total(marks):
    total = np.sum(marks)
    return total
totals = []
for i in range(len(df)):
    marks = df.loc[i, subjects].to_numpy(dtype=float)
    total = calculate_total(marks)
    average = np.mean(marks)
    totals.append(total)
    if marks[0] >= 40 and marks[1] >= 40 and marks[2] >= 40:
        result = "Pass"
    else:
        result = "Fail"

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"
    print(df.loc[i, "Name"], "Total:", total, "Average:", round(average, 2), "Result:", result, "Grade:", grade)


highest = max(totals)
lowest = min(totals)

for i in range(len(df)):
    if totals[i] == highest:
        print("Top Performer:", df.loc[i, "Name"], "Total:", totals[i])

for i in range(len(df)):
    if totals[i] == lowest:
        print("Lowest Performer:", df.loc[i, "Name"], "Total:", totals[i])

print("Class Average Total:", round(np.mean(totals), 2))

for subject in subjects:
    marks = df[subject].to_numpy(dtype=float)
    average = np.mean(marks)
    print(subject, "Average Marks:", round(average, 2))


print("\n--- Student Attendance Report ---")

for i in range(len(df)):
    print(df.loc[i, "Name"], "Attendance:", df.loc[i, "Attendance"], "%")
