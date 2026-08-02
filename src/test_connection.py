from db_connection import get_connection
try:
    conn=get_connection()
    if conn.is_connected():
        print("succesfully connection to mysql")
except Exception as e:
    print("Connection Failed")
    print(e)
finally:
    if "conn" in locals() and conn.is_connected():
        conn.close()
        print("connection close")