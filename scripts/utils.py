import os
import sqlite3
from pathlib import Path
import urllib.request
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)


def download_northwind_db(db_path):
    """
    Download the Northwind SQLite database from the official repository

    Args:
        db_path: Path where the database should be saved
    """
    print(
        f"{Fore.YELLOW}Northwind database not found. Downloading it now...{Style.RESET_ALL}"
    )

    # URL for the SQLite version of Northwind from the official repository
    url = "https://raw.githubusercontent.com/jpwhite3/northwind-SQLite3/main/dist/northwind.db"

    try:
        # Download the file
        print(f"{Fore.CYAN}Downloading from {url}...{Style.RESET_ALL}")
        urllib.request.urlretrieve(url, db_path)
        print(
            f"{Fore.GREEN}Successfully downloaded Northwind database to {db_path}{Style.RESET_ALL}"
        )
        return True
    except Exception as e:
        print(f"{Fore.RED}Error downloading Northwind database: {e}{Style.RESET_ALL}")
        return False


def connect_to_northwind():
    """
    Connect to the Northwind SQLite database. If the database doesn't exist,
    it will be downloaded automatically.

    Returns a connection object
    """
    # Define the path to the Northwind database
    data_dir = Path(__file__).parent.parent / "northwind_data"
    db_path = data_dir / "northwind.sqlite"

    # Create the data directory if it doesn't exist
    os.makedirs(data_dir, exist_ok=True)

    # Check if database exists, if not, download it
    if not db_path.exists():
        success = download_northwind_db(db_path)
        if not success:
            raise FileNotFoundError(
                f"{Fore.RED}Could not download Northwind database. Please download it manually and place it at {db_path}{Style.RESET_ALL}"
            )

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    return conn


def save_to_csv(df, cube_name):
    """
    Save a DataFrame to CSV for MongoDB import

    Args:
        df: pandas DataFrame to save
        cube_name: Name of the cube (used for filename)
    """
    # Create output directory if it doesn't exist
    output_dir = Path(__file__).parent.parent / "northwind_csv_cubes"
    os.makedirs(output_dir, exist_ok=True)

    # Save to CSV
    output_path = output_dir / f"{cube_name}.csv"
    df.to_csv(output_path, index=False)
    print(f"{Fore.GREEN}Data saved to {output_path}{Style.RESET_ALL}")


def categorize_price(price):
    """
    Categorize price into levels
    """
    if price is None:
        return "Unknown"
    elif price < 10:
        return "Low"
    elif price < 50:
        return "Medium"
    else:
        return "High"


def categorize_stock(units):
    """
    Categorize stock level
    """
    if units is None:
        return "Unknown"
    elif units < 10:
        return "Low"
    elif units < 50:
        return "Medium"
    else:
        return "High"


def categorize_order_amount(amount):
    """
    Categorize order amount into levels
    """
    if amount is None:
        return "Unknown"
    elif amount < 1000:
        return "Low"
    elif amount < 5000:
        return "Medium"
    else:
        return "High"


def categorize_sales(amount):
    """
    Categorize sales level
    """
    if amount is None:
        return "Unknown"
    elif amount < 5000:
        return "Low"
    elif amount < 20000:
        return "Medium"
    else:
        return "High"
