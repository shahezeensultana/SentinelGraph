import mysql.connector
def get_connection():
    connection=mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="apapapapap@786",
        database="sentinelgraph"
    )
    return connection