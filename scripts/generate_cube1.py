import pandas as pd
from utils import connect_to_northwind, save_to_csv
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)


def generate_cube1():
    """
    Generate Cube 1 with customer and employee-related data along with order details.

    Attributes:
        customerID, customerName, customerCity, customerCountry,
        employeeID, employeeName, employeeCity, employeeCountry,
        orderMonth, orderYear, shipOrders, notShipOrders
    """
    # Connect to the database
    conn = connect_to_northwind()

    # Query to get customer, employee, and order data
    query = """
    SELECT 
        c.CustomerID as customerID,
        c.CompanyName as customerName,
        c.City as customerCity, 
        c.Country as customerCountry,
        e.EmployeeID as employeeID,
        (e.FirstName || ' ' || e.LastName) as employeeName,
        e.City as employeeCity,
        e.Country as employeeCountry,
        strftime('%m', o.OrderDate) as orderMonth,
        strftime('%Y', o.OrderDate) as orderYear,
        SUM(CASE WHEN o.ShippedDate IS NOT NULL THEN 1 ELSE 0 END) as shipOrders,
        SUM(CASE WHEN o.ShippedDate IS NULL THEN 1 ELSE 0 END) as notShipOrders
    FROM 
        Orders o
    JOIN 
        Customers c ON o.CustomerID = c.CustomerID
    JOIN 
        Employees e ON o.EmployeeID = e.EmployeeID
    GROUP BY 
        c.CustomerID, e.EmployeeID, orderMonth, orderYear
    """

    print(f"{Fore.CYAN}Executing query for Cube 1...{Style.RESET_ALL}")

    # Execute query and create DataFrame
    df = pd.read_sql_query(query, conn)

    # Close connection
    conn.close()

    print(f"{Fore.CYAN}Query completed. Generated {len(df)} records.{Style.RESET_ALL}")

    # Save to CSV
    save_to_csv(df, "cube1")

    return df


if __name__ == "__main__":
    print(
        f"{Fore.YELLOW}Generating Cube 1 - Customer, Employee, and Order data...{Style.RESET_ALL}"
    )
    generate_cube1()
    print(f"{Fore.GREEN}Cube 1 generation complete!{Style.RESET_ALL}")
