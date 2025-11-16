import pandas as pd

def load_data(path):
    df=pd.read_csv(path)
    df["date"]=pd.to_datetime(df["date"])
    df["total_revenue"]=df["price"]*df["quantity"]
    return df

def analyze_sale(df):
    category_summary=df.groupby("category")["total_revenue"].sum()
    daily_summary=df.groupby("date")["total_revenue"].sum()
    return category_summary,daily_summary

def saved_cleaned(df,path):
    df.to_csv(path,index=False)
    
if __name__ == "__main__":
    df=load_data("/home/raj/Desktop/DE_base/week1/Day5/sales_data.csv") 
    print("\nData with total revenue")
    print(df)
    
    category_summary,daily_summary=analyze_sale(df)
    
    print("\nRevenue by category:")
    print(category_summary)
    
    print("\nDaily Revenue")
    print(daily_summary)
    
    saved_cleaned(df,"sales_cleaned.csv")
    print("\nSaved sales_cleaned.csv")