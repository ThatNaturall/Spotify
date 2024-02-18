from loader import CsvToSqlLoader

def main():
    # CSV file and table information
    csv_file = 'data/input/songs_normalize.csv'
    table_name = 'Songs'

    # ODBC connection string
    conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};Server=tcp:kamogelo.database.windows.net,1433;Database=KamogeloTest;Uid=kamogelo.ramantsima;Pwd=Rehale&eria2;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

    # Load CSV data into SQL Server
    loader = CsvToSqlLoader(csv_file, table_name, conn_str)
    loader.load_csv_to_sql()

if __name__ == "__main__":
    main()
