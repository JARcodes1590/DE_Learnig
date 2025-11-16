import pandas as pd

df=pd.read_csv("/home/raj/Desktop/DE_base/week1/Day5/sales_data.csv")
print("Original Data frame")
print(df)

df["total_revenue"]=df["price"]*df["quantity"]


df["date"]=pd.to_datetime(df["date"])

df["high_value"]=df["total_revenue"].apply(lambda x:"high" if x>=5000 else "normal")
df["unit_price_flag"]=df["price"].apply(lambda x:"premium" if x>=1000 else "standard")

rank_map={
    "Electronics":1,
    "Furniture":2,
    "Food":3,
    "Stationery":4
}
df["category_rank"]=df["category"].map(rank_map)

print("\n DataFrame with added column: ")
print(df)

top_products=df.sort_values("total_revenue",ascending=False).head(3)


category_revenue=df.groupby("category")["total_revenue"].sum()


high_values_count=df["high_value"].value_counts()


daily_revenue=df.groupby("date")["total_revenue"].sum()


df.to_csv("sales_cleaned.csv",index=False)
category_revenue.to_csv("category_summary.csv")
daily_revenue.to_csv("daily_summary.csv")
top_products.to_csv("top_products.csv")
print("\n Saved sales_cleaned.csv,category_summary.csv,daily_summary.csv,top_products.csv")


print("\n================= SALES REPORT =================")

print("\n💰 TOP 3 PRODUCTS BY REVENUE:")
print(top_products[["product", "total_revenue"]])

print("\n📂 REVENUE BY CATEGORY:")
print(category_revenue)

print("\n⚡ HIGH-VALUE VS NORMAL TRANSACTIONS:")
print(high_values_count)

print("\n📅 DAILY REVENUE TREND:")
print(daily_revenue)

print("\n================================================\n")
