import pandas as pd
# this reads the csv
df=pd.read_csv("/home/raj/Desktop/DE_base/week1/Day3/students.csv")
# print the whole table
print("Full Dataframe")
print(df)
# print first 2 line
print("\nHead (first 2 rows)")
print(df.head(2))
# basic info about the data
print("\nColumns names:",df.columns.tolist())
print("\nData Types")
print(df.dtypes)
print("\nSummary Statistics:")
print(df.describe())

# Marks Statistics
avg_marks=df["marks"].mean()
max_marks=df["marks"].max()
min_marks=df["marks"].min()

print("\nAverage marks=",avg_marks)
print("\nMaximum marks=",max_marks)
print("\nMinimum marks=",min_marks)

# Filtering passed and failed student
passed=df[df["marks"]>=70]
failed=df[df["marks"]<70]
print("\nPassed students")
print(passed)
print("\nFailed students")
print(failed)

print("\nNumber of Passed student",len(passed))
print("\nNumber of failed student",len(failed))