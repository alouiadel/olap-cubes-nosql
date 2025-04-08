import sys
from pathlib import Path
from colorama import Fore, Style, init, Back

# Add the scripts directory to the Python path so we can find the modules
sys.path.append(str(Path(__file__).parent))

# Now import the cube generation functions
from generate_cube1 import generate_cube1
from generate_cube2 import generate_cube2
from generate_cube3 import generate_cube3
from generate_cube4 import generate_cube4
from validate_cubes import validate_all_cubes

# Initialize colorama
init(autoreset=True)

def main():
    """
    Run all cube generation scripts and provide instructions for MongoDB import.
    """
    print(f"{Fore.YELLOW}{Back.BLUE}{Style.BRIGHT} OLAP CUBES GENERATION FOR MONGODB {Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Starting OLAP cubes generation for MongoDB from Northwind data...{Style.RESET_ALL}")
    
    # Generate all cubes
    print(f"\n{Fore.CYAN}{Style.BRIGHT}1. Generating cubes...{Style.RESET_ALL}")
    generate_cube1()
    generate_cube2()
    generate_cube3()
    generate_cube4()
    
    # Validate the generated cubes
    print(f"\n{Fore.CYAN}{Style.BRIGHT}2. Validating cubes...{Style.RESET_ALL}")
    all_valid = validate_all_cubes()
    
    if all_valid:
        # Provide MongoDB import instructions
        print(f"\n{Fore.GREEN}{Style.BRIGHT}3. All cubes generated and validated successfully!{Style.RESET_ALL}")
        print(f"\n{Fore.MAGENTA}{Style.BRIGHT}MongoDB Import Instructions:{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}To import these CSV files into MongoDB, you can use the following commands:{Style.RESET_ALL}")
        print(f"\n{Fore.CYAN}mongoimport --db northwind_olap --collection cube1 --type csv --headerline --file northwind_csv_cubes/cube1.csv{Style.RESET_ALL}")
        print(f"{Fore.CYAN}mongoimport --db northwind_olap --collection cube2 --type csv --headerline --file northwind_csv_cubes/cube2.csv{Style.RESET_ALL}")
        print(f"{Fore.CYAN}mongoimport --db northwind_olap --collection cube3 --type csv --headerline --file northwind_csv_cubes/cube3.csv{Style.RESET_ALL}")
        print(f"{Fore.CYAN}mongoimport --db northwind_olap --collection cube4 --type csv --headerline --file northwind_csv_cubes/cube4.csv{Style.RESET_ALL}")
        
        print(f"\n{Fore.YELLOW}Or, use the MongoDB Compass GUI to import the CSV files.{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.RED}{Style.BRIGHT}3. Validation failed. Please fix the issues before importing to MongoDB.{Style.RESET_ALL}")
    
    print(f"\n{Fore.RED}Note: Make sure MongoDB is running and accessible before importing the data.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()