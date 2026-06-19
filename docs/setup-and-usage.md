# Setup and Usage

## Prerequisites

- Python 3.9 or higher
- Required Python packages (install using):
  ```
  pip install -r requirements.txt
  ```
- MongoDB (for importing the generated data)

## Generating OLAP Cubes

The scripts automatically download the Northwind database and transform it into MongoDB-compatible CSV files:

1. **Run all cubes at once:**

   ```
   python scripts/generate_all_cubes.py
   ```

   This will generate all cubes and validate them automatically.

2. **Run individual cube generators:**
   ```
   python scripts/generate_cube1.py  # Customer and employee data
   python scripts/generate_cube2.py  # Supplier and product data
   python scripts/generate_cube3.py  # Customer order and sales levels
   python scripts/generate_cube4.py  # Revenue analysis data
   ```

## Validating OLAP Cubes

You can validate the generated cube CSV files to ensure they're properly structured:

```bash
python scripts/validate_cubes.py
```

The validation script checks:

- File existence
- Presence of all required columns
- Data integrity (no missing critical values)
- Overall data quality

Each cube is validated against its expected schema, and a summary report is provided.

## Using MongoDB with Docker

### Setting Up MongoDB Container

If you don't have MongoDB installed locally, you can easily run it in a Docker container:

1. **Make sure Docker is installed** on your system. You can download it from [Docker's official website](https://www.docker.com/products/docker-desktop/).

2. **Run a MongoDB container** with the following command:

   ```bash
   docker run --name mongodb -d -p 27017:27017 mongo:latest
   ```

   This command:
   - Creates a container named "mongodb"
   - Runs it in detached mode (-d)
   - Maps the MongoDB port from the container to your local machine (-p 27017:27017)
   - Uses the latest MongoDB image

3. **Verify the container is running**:

   ```bash
   docker ps
   ```

4. **Restarting the container** (if needed):
   ```bash
   # Stop the container
   docker stop mongodb
   # Start it again
   docker start mongodb
   ```

### Executing MongoDB Commands

You can interact with the MongoDB container in several ways:

1. **Using Docker exec to run commands**:

   ```bash
   docker exec -it mongodb mongosh
   ```

   This opens the MongoDB shell where you can execute commands directly.

2. **Import the OLAP cube data into the container**:

   ```bash
   # First, copy all CSV files into the container
   docker cp northwind_csv_cubes/cube1.csv mongodb:/tmp/cube1.csv
   docker cp northwind_csv_cubes/cube2.csv mongodb:/tmp/cube2.csv
   docker cp northwind_csv_cubes/cube3.csv mongodb:/tmp/cube3.csv
   docker cp northwind_csv_cubes/cube4.csv mongodb:/tmp/cube4.csv

   # Then import each cube into MongoDB
   docker exec -it mongodb mongoimport --db northwind_olap --collection cube1 --type csv --headerline --file /tmp/cube1.csv
   docker exec -it mongodb mongoimport --db northwind_olap --collection cube2 --type csv --headerline --file /tmp/cube2.csv
   docker exec -it mongodb mongoimport --db northwind_olap --collection cube3 --type csv --headerline --file /tmp/cube3.csv
   docker exec -it mongodb mongoimport --db northwind_olap --collection cube4 --type csv --headerline --file /tmp/cube4.csv
   ```

### Exploring Data with MongoDB Compass

MongoDB Compass is a powerful GUI tool for exploring and manipulating MongoDB data visually.

1. **Download and install MongoDB Compass** from the [official MongoDB website](https://www.mongodb.com/products/compass).

2. **Connect to your MongoDB instance**:
   - Open MongoDB Compass
   - Connect using the connection string: `mongodb://localhost:27017`
   - You should see the `northwind_olap` database in the list

3. **Explore your OLAP cubes**:
   - Click on the `northwind_olap` database
   - Browse collections (cube1, cube2, etc.)
   - Use the query builder to construct OLAP queries
   - Visualize data using Compass's built-in charts and aggregation pipeline builder
