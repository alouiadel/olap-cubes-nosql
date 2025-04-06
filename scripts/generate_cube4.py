import pandas as pd
from utils import connect_to_northwind, save_to_csv
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def generate_cube4():
    """
    Generate Cube 4 with product, order, and customer data for revenue analysis.
    
    Attributes:
        ProductID, ProductName, CategoryID, ordersRevenue, ShippedRevenue,
        customerID, customerName, customerCity, customerCountry,
        orderMonth, orderYear
    """
    # Connect to the database
    conn = connect_to_northwind()
    
    # Query to get product, order, and customer data for revenue analysis
    query = """
    SELECT 
        p.ProductID,
        p.ProductName,
        p.CategoryID,
        SUM(od.UnitPrice * od.Quantity * (1 - od.Discount)) as ordersRevenue,
        SUM(CASE WHEN o.ShippedDate IS NOT NULL THEN od.UnitPrice * od.Quantity * (1 - od.Discount) ELSE 0 END) as ShippedRevenue,
        c.CustomerID as customerID,
        c.CompanyName as customerName,
        c.City as customerCity,
        c.Country as customerCountry,
        strftime('%m', o.OrderDate) as orderMonth,
        strftime('%Y', o.OrderDate) as orderYear
    FROM 
        Products p
    JOIN 
        [Order Details] od ON p.ProductID = od.ProductID
    JOIN 
        Orders o ON od.OrderID = o.OrderID
    JOIN 
        Customers c ON o.CustomerID = c.CustomerID
    GROUP BY 
        p.ProductID, c.CustomerID, orderMonth, orderYear
    """
    
    print(f"{Fore.CYAN}Executing query for Cube 4...{Style.RESET_ALL}")
    
    # Execute query and create DataFrame
    df = pd.read_sql_query(query, conn)
    
    # Close connection
    conn.close()
    
    print(f"{Fore.CYAN}Query completed. Generated {len(df)} records.{Style.RESET_ALL}")
    
    # Save to CSV
    save_to_csv(df, "cube4")
    
    return df

if __name__ == "__main__":
    print(f"{Fore.YELLOW}Generating Cube 4 - Product, order, and customer data for revenue analysis...{Style.RESET_ALL}")
    generate_cube4()
    print(f"{Fore.GREEN}Cube 4 generation complete!{Style.RESET_ALL}")