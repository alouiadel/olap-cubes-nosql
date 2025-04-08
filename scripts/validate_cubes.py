import os
import pandas as pd
from pathlib import Path
from colorama import Fore, Style, init, Back

# Initialize colorama
init(autoreset=True)

# Expected schemas for each cube
EXPECTED_SCHEMAS = {
    "cube1": [
        "customerID", "customerName", "customerCity", "customerCountry",
        "employeeID", "employeeName", "employeeCity", "employeeCountry",
        "orderMonth", "orderYear", "shipOrders", "notShipOrders"
    ],
    "cube2": [
        "supplierID", "supplierName", "supplierCity", "supplierCountry",
        "categorieID", "categorieName", "priceLevel", "stockLevel", "produit_num"
    ],
    "cube3": [
        "customerCity", "customerCountry", "orderLevel", "salesLevel", "customer_num"
    ],
    "cube4": [
        "ProductID", "ProductName", "CategoryID", "ordersRevenue", "ShippedRevenue",
        "customerID", "customerName", "customerCity", "customerCountry",
        "orderMonth", "orderYear"
    ]
}

def check_file_exists(file_path):
    """Check if a file exists at the given path"""
    exists = os.path.isfile(file_path)
    if exists:
        print(f"{Fore.GREEN}✓ File exists: {file_path}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}✗ File does not exist: {file_path}{Style.RESET_ALL}")
    return exists

def validate_columns(df, cube_name):
    """Validate that the DataFrame has all the expected columns for the cube"""
    expected_columns = EXPECTED_SCHEMAS[cube_name]
    missing_columns = [col for col in expected_columns if col not in df.columns]
    
    if missing_columns:
        print(f"{Fore.RED}✗ Missing columns in {cube_name}: {', '.join(missing_columns)}{Style.RESET_ALL}")
        return False
    else:
        print(f"{Fore.GREEN}✓ All expected columns present in {cube_name}{Style.RESET_ALL}")
        return True

def validate_data_integrity(df, cube_name):
    """Validate basic data integrity for the cube"""
    # Check for null values in key columns
    issues = []
    
    # Common checks for all cubes
    if df.empty:
        issues.append("DataFrame is empty")
    
    # Cube-specific checks
    if cube_name == "cube1":
        if df["customerID"].isnull().any():
            issues.append("Missing customer IDs")
        if df["employeeID"].isnull().any():
            issues.append("Missing employee IDs")
            
    elif cube_name == "cube2":
        if df["supplierID"].isnull().any():
            issues.append("Missing supplier IDs")
        if df["categorieID"].isnull().any():
            issues.append("Missing category IDs")
            
    elif cube_name == "cube3":
        # Check if ANY record has both city AND country as null
        if (df["customerCity"].isnull() & df["customerCountry"].isnull()).any():
            issues.append("Missing both customer city and country")
            
    elif cube_name == "cube4":
        if df["ProductID"].isnull().any():
            issues.append("Missing product IDs")
        if df["customerID"].isnull().any():
            issues.append("Missing customer IDs")
    
    if issues:
        print(f"{Fore.RED}✗ Data integrity issues in {cube_name}: {', '.join(issues)}{Style.RESET_ALL}")
        return False
    else:
        print(f"{Fore.GREEN}✓ Data integrity checks passed for {cube_name}{Style.RESET_ALL}")
        return True

def validate_cube(cube_name):
    """Validate a specific cube CSV file"""
    output_dir = Path(__file__).parent.parent / 'northwind_csv_cubes'
    file_path = output_dir / f"{cube_name}.csv"
    
    print(f"\n{Fore.CYAN}{Style.BRIGHT}Validating {cube_name}...{Style.RESET_ALL}")
    
    # Check if the file exists
    if not check_file_exists(file_path):
        return False
    
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Print basic stats
        print(f"{Fore.CYAN}Found {len(df)} records{Style.RESET_ALL}")
        
        # Validate columns
        columns_valid = validate_columns(df, cube_name)
        
        # Validate data integrity
        data_valid = validate_data_integrity(df, cube_name)
        
        # Overall validation result
        is_valid = columns_valid and data_valid
        if is_valid:
            print(f"{Fore.GREEN}{Style.BRIGHT}✓ {cube_name} is valid!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}{Style.BRIGHT}✗ {cube_name} has validation issues!{Style.RESET_ALL}")
        
        return is_valid
        
    except Exception as e:
        print(f"{Fore.RED}✗ Error validating {cube_name}: {str(e)}{Style.RESET_ALL}")
        return False

def validate_all_cubes():
    """Validate all cube CSV files"""
    print(f"{Fore.YELLOW}{Back.BLUE}{Style.BRIGHT} OLAP CUBES VALIDATION {Style.RESET_ALL}")
    
    results = {}
    all_valid = True
    
    for cube_name in EXPECTED_SCHEMAS.keys():
        results[cube_name] = validate_cube(cube_name)
        all_valid = all_valid and results[cube_name]
    
    # Print summary
    print(f"\n{Fore.CYAN}{Style.BRIGHT}Validation Summary:{Style.RESET_ALL}")
    for cube_name, is_valid in results.items():
        status_symbol = "✓" if is_valid else "✗"
        status_color = Fore.GREEN if is_valid else Fore.RED
        print(f"{status_color}{status_symbol} {cube_name}: {'Valid' if is_valid else 'Invalid'}{Style.RESET_ALL}")
    
    # Overall result
    if all_valid:
        print(f"\n{Fore.GREEN}{Style.BRIGHT}All cubes are valid and ready for MongoDB import!{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.RED}{Style.BRIGHT}Some cubes have validation issues. Please fix before importing to MongoDB.{Style.RESET_ALL}")
    
    return all_valid

if __name__ == "__main__":
    validate_all_cubes()