import pandas as pd
from utils import connect_to_northwind, save_to_csv, categorize_order_amount, categorize_sales
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def generate_cube3():
    """
    Generate Cube 3 with customer order and sales level data.
    
    Attributes:
        customerCity, customerCountry, orderLevel, salesLevel, customer_num
    """
    # Connect to the database
    conn = connect_to_northwind()
    
    # Query to get customer orders and sales data
    query = """
    SELECT 
        c.City as customerCity,
        c.Country as customerCountry,
        COUNT(o.OrderID) as orderCount,
        SUM(od.UnitPrice * od.Quantity * (1 - od.Discount)) as totalSales,
        COUNT(DISTINCT c.CustomerID) as customer_num
    FROM 
        Customers c
    JOIN 
        Orders o ON c.CustomerID = o.CustomerID
    JOIN 
        [Order Details] od ON o.OrderID = od.OrderID
    WHERE
        c.City IS NOT NULL OR c.Country IS NOT NULL
    GROUP BY 
        c.City, c.Country
    """
    
    print(f"{Fore.CYAN}Executing query for Cube 3...{Style.RESET_ALL}")
    
    # Execute query and create DataFrame
    df = pd.read_sql_query(query, conn)
    
    # Close connection
    conn.close()
    
    print(f"{Fore.CYAN}Query completed. Generated {len(df)} records.{Style.RESET_ALL}")
    
    # Additional check to filter out any rows where both city and country are null
    df = df[~(df['customerCity'].isnull() & df['customerCountry'].isnull())]
    
    # Categorize order and sales levels
    print(f"{Fore.CYAN}Categorizing order and sales levels...{Style.RESET_ALL}")
    df['orderLevel'] = df['orderCount'].apply(categorize_order_amount)
    df['salesLevel'] = df['totalSales'].apply(categorize_sales)
    
    # Drop the raw columns that were used for categorization
    df = df.drop(['orderCount', 'totalSales'], axis=1)
    
    # Save to CSV
    save_to_csv(df, "cube3")
    
    return df

if __name__ == "__main__":
    print(f"{Fore.YELLOW}Generating Cube 3 - Customer orders and sales level data...{Style.RESET_ALL}")
    generate_cube3()
    print(f"{Fore.GREEN}Cube 3 generation complete!{Style.RESET_ALL}")