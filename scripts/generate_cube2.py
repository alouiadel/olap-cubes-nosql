import pandas as pd
from utils import connect_to_northwind, save_to_csv, categorize_price, categorize_stock
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def generate_cube2():
    """
    Generate Cube 2 with supplier and product category data.
    
    Attributes:
        supplierID, supplierName, supplierCity, supplierCountry,
        categorieID, categorieName, priceLevel, stockLevel, produit_num
    """
    # Connect to the database
    conn = connect_to_northwind()
    
    # Query to get supplier, category, and product data
    query = """
    SELECT 
        s.SupplierID as supplierID,
        s.CompanyName as supplierName,
        s.City as supplierCity,
        s.Country as supplierCountry,
        c.CategoryID as categorieID,
        c.CategoryName as categorieName,
        p.UnitPrice as unitPrice,
        p.UnitsInStock as unitsInStock,
        COUNT(p.ProductID) as produit_num
    FROM 
        Products p
    JOIN 
        Suppliers s ON p.SupplierID = s.SupplierID
    JOIN 
        Categories c ON p.CategoryID = c.CategoryID
    GROUP BY 
        s.SupplierID, c.CategoryID
    """
    
    print(f"{Fore.CYAN}Executing query for Cube 2...{Style.RESET_ALL}")
    
    # Execute query and create DataFrame
    df = pd.read_sql_query(query, conn)
    
    # Close connection
    conn.close()
    
    print(f"{Fore.CYAN}Query completed. Generated {len(df)} records.{Style.RESET_ALL}")
    
    # Categorize price and stock levels
    print(f"{Fore.CYAN}Categorizing price and stock levels...{Style.RESET_ALL}")
    df['priceLevel'] = df['unitPrice'].apply(categorize_price)
    df['stockLevel'] = df['unitsInStock'].apply(categorize_stock)
    
    # Drop the raw columns that were used for categorization
    df = df.drop(['unitPrice', 'unitsInStock'], axis=1)
    
    # Save to CSV
    save_to_csv(df, "cube2")
    
    return df

if __name__ == "__main__":
    print(f"{Fore.YELLOW}Generating Cube 2 - Supplier and product category data...{Style.RESET_ALL}")
    generate_cube2()
    print(f"{Fore.GREEN}Cube 2 generation complete!{Style.RESET_ALL}")