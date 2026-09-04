import pyodbc


def get_connection():

    connection = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER={.\\SQLEXPRESS};"
        "DATABASE=PlannerDB;"
        "Trusted_Connection=yes;"
    )

    return connection