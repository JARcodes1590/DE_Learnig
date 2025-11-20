import psycopg2
import pandas as pd

# connect to Postgresql
def get_connection():
    """Create and return a PostgreSQL connection."""
    conn=psycopg2.connect(
        dbname="de_project",
        user="raj",
        password="raj123",
        host="localhost",
        port=5432
    )
    return conn

# Define query
def get_revenue_by_customer(conn):
    """Return revenue per customer+region as a DataFrame."""
    query="""
    SELECT c.region,
    c.name AS customer_name,
    SUM(s.total_revenue) AS revenue
    FROM sales AS s
    JOIN customers AS c
    On s.customer_id=c.id
    GROUP BY c.region,c.name
    ORDER BY revenue DESC;
    """
    df=pd.read_sql_query(query,conn)
    return df


def get_revenue_by_region(conn):
    query="""
    SELECT c.region,
    SUM(s.total_revenue) AS revenue
    FROM sales AS s
    JOIN customers AS c
    ON s.customer_id=c.id
    GROUP BY c.region
    ORDER BY revenue DESC;
    """
    df=pd.read_sql_query(query,conn)
    return df


def get_revenue_by_region_filtered(conn,region):
    """Return revenue for a single region."""
    query = """
        SELECT
            c.region,
            c.name AS customer_name,
            SUM(s.total_revenue) AS revenue
        FROM sales AS s
        JOIN customers AS c
        ON s.customer_id = c.id
        WHERE c.region = %s
        GROUP BY c.region, c.name
        ORDER BY revenue DESC;
        """
    df = pd.read_sql_query(query, conn, params=(region,))
    return df

def get_customer_revenue_for_region(conn,region):
    query="""
    SELECT c.region,
    c.name AS customer_name,
    SUM(s.total_revenue) AS revenue
    FROM sales AS s
    JOIN customers AS c
    ON s.customer_id = c.id
    WHERE c.region=%s
    GROUP BY c.region,c.name
    ORDER BY revenue DESC;
    """
    df=pd.read_sql_query(query,conn,params=(region,))
    return df
    


if __name__ == "__main__":
    
    conn=get_connection()
    
    print("\n Revenue by customer and revenue:")
    df_customer= get_revenue_by_customer(conn)
    print(df_customer) 
    
    print("\n Revenue by region:")
    df_region=get_revenue_by_region(conn)
    print(df_region)
    # ---- filtered examples ----
    region_to_check = "Lalitpur"

    print(f"\nRevenue ONLY for region = {region_to_check}:")
    df_region_filtered = get_revenue_by_region_filtered(conn, region_to_check)
    print(df_region_filtered)

    print(f"\nCustomer revenue in region = {region_to_check}:")
    df_customer_region = get_customer_revenue_for_region(conn, region_to_check)
    print(df_customer_region)
    conn.close()