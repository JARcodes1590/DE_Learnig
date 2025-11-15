import pandas as pd
df=pd.read_csv("/home/raj/Desktop/DE_base/week1/Day5/sales_data.csv")
print("\nOrginal dataset")
print(df)
df["total_revenue"]=df["price"]*df["quantity"]
print("\nDataFrame with total revenue")
print(df)

# clean column types
df["date"]=pd.to_datetime(df["date"])
print("\nAfter converting date column:")
print(df.dtypes)

# sorted data frame
df_sorted=df.sort_values("total_revenue",ascending=False)
print("\nData sorted by revenue")
print(df_sorted)

# filtering by category
electronics=df[df["category"] =="Electronics"]
print("\nElectronic products:")
print(electronics)

# grouping very important
category_summary=df.groupby("category")["total_revenue"].sum()
print("\nSummary of revenue by category:")
print(category_summary)

# total revenue by day
daily_revenue_summary=df.groupby("date")["total_revenue"].sum()
print("\nSummary of revenue by day")
print(daily_revenue_summary)