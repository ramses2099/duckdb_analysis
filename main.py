import duckdb as dd
import os

def main():
    # clear 
    os.system("cls")

    # path db
    path_db = os.path.join("C:\\Users\\d6920\\Sources\\Python\\duckdb_analysis\\db", "database.db")
    path_csv = os.path.join("C:\\Users\\d6920\\Sources\\Python\\duckdb_analysis\\datasets", "ai_job_trends_dataset.csv")
    
    # Create db in memory
    # db = dd.connect(':memory:')
    db = dd.connect('.\\db\\database.db')
    
    # Running a basic SQL query
    # result = db.sql("SELECT 'DuckDB_is_cool' as Answer").fetchall()

    # print(type(result))
    # print(result)

    # Create a relation from a SQL query
    # rel = db.sql("SELECT * FROM range(10_100) AS tbl(ID)")
    
    # Display the relation
    # rel.show()

    # tables = db.sql('SHOW ALL TABLES')
    # print(tables)

    # DuckDb read csv file into a virtual table
    # db.execute(f"""
    #     CREATE TABLE jo_trends AS
    #     SELECT * FROM read_csv_auto('{path_csv}')
    #     """)
    
    # preview schema
    # print("schema:")
    # print(db.execute("DESCRIBE jo_trends").fetch_df())

    df = db.execute("SELECT * FROM jo_trends").fetchdf()

    print("\n missing values")
    print(df.head(10))

    

if __name__ == "__main__":
    main()