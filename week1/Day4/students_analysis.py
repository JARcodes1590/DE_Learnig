import pandas as pd
df=pd.read_csv("/home/raj/Desktop/DE_base/week1/Day3/students.csv")
print("\nOrginal DataFrame ")
print(df)
pass_marks=70
df["result"]=df["marks"].apply(lambda m:"pass" if m>= pass_marks else "fail")
print("\nDataFrame with result columns:")
df["grade"]=df["marks"].apply(lambda m:"A" if m>=90 else("B" if m>=80 else("C" if m>=70 else "D")))
print(df)
# sort by marks, descending("highest first")
df_sorted=df.sort_values("marks",ascending=False)
print("\nSorted by marks(descending):")
print(df_sorted)

# filters pass and fail students
passed=df[df["result"] == "pass"]
failed=df[df["result"] == "fail"]
# save them to new files in same folder
passed.to_csv("student_pass.csv",index=False)
failed.to_csv("student_fail.csv",index=False)

print("\nSaved student_pass.csv and student_fail.csv")

# Group by result and shows count and average marks
grade_summary=df.groupby("grade")["marks"].agg(["count","mean"])
print("\nSummary by grade:")
print(grade_summary)