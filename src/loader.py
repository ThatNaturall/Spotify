import pandas as pd
import pyodbc

class CsvToSqlLoader:
    def __init__(self, csv_file, table_name, conn_str):
        self.csv_file = csv_file
        self.table_name = table_name
        self.conn_str = conn_str

    def load_csv_to_sql(self):
        # Read CSV file into a pandas DataFrame
        df = pd.read_csv(self.csv_file)

        # Connect to SQL Server
        conn = pyodbc.connect(self.conn_str)
        cursor = conn.cursor()

        # Create table if it doesn't exist
        create_table_query = '''
            IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = ?) 
            CREATE TABLE {table_name} (
                [Artist] [nvarchar](max) NOT NULL,
                [Song] [nvarchar](max) NOT NULL,
                [Duration_ms] [float] NOT NULL,
                [Explicit] [nvarchar](50) NOT NULL,
                [Year] [int] NOT NULL,
                [Popularity] [int] NOT NULL,
                [Danceability] [float] NOT NULL,
                [Energy] [float] NOT NULL,
                [Key] [int] NOT NULL,
                [Loudness] [float] NOT NULL,
                [Mode] [int] NOT NULL,
                [Speechiness] [float] NOT NULL,
                [Acousticness] [float] NOT NULL,
                [Instrumentalness] [float] NOT NULL,
                [Liveness] [float] NOT NULL,
                [Valence] [float] NOT NULL,
                [Tempo] [float] NOT NULL,
                [Genre] [nvarchar](max) NOT NULL
            )
        '''.format(table_name=self.table_name)
        cursor.execute(create_table_query, [self.table_name])

        # Insert data into the table
        for index, row in df.iterrows():
            insert_query = f"INSERT INTO {self.table_name} VALUES ({', '.join(['?' for _ in df.columns])})"
            cursor.execute(insert_query, tuple(row))

        conn.commit()
        conn.close()
        
        print(f"Data from '{self.csv_file}' loaded into SQL Server table '{self.table_name}'.")
