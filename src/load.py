import pandas as pd
from db_connection import get_connection

data_path="data/raw/archive/r4.2/"

logon = pd.read_csv(data_path + "logon.csv", nrows=10000)
device = pd.read_csv(data_path + "device.csv", nrows=10000)
email = pd.read_csv(data_path + "email.csv", nrows=10000)
file = pd.read_csv(data_path + "file.csv", nrows=10000)
http = pd.read_csv(data_path + "http.csv", nrows=10000)
psychometric = pd.read_csv(data_path + "psychometric.csv")

logon.rename(columns={
    "date":"event_time",
    "user":"user_id"
},inplace=True)

device.rename(columns={
    "date":"event_time",
    "user":"user_id"
},inplace=True)

email.rename(columns={
    "date":"event_time",
    "user":"user_id",
    "to":"recipient_to",
    "from":"sender"
},inplace=True)

file.rename(columns={
    "date":"event_time",
    "user":"user_id"
},inplace=True)

http.rename(columns={
    "date":"event_time",
    "user":"user_id"
},inplace=True)

email["recipient_to"] = email["recipient_to"].fillna("")
email["cc"] = email["cc"].fillna("")
email["bcc"] = email["bcc"].fillna("")
email["sender"] = email["sender"].fillna("")
email["content"] = email["content"].fillna("")

file = file.fillna("")
http = http.fillna("")

#converting dates
logon["event_time"]=pd.to_datetime(logon["event_time"])
device["event_time"]=pd.to_datetime(device["event_time"])
email["event_time"]=pd.to_datetime(email["event_time"])
file["event_time"]=pd.to_datetime(file["event_time"])
http["event_time"]=pd.to_datetime(http["event_time"])

conn=None
cursor=None
try:
    conn=get_connection()
    cursor=conn.cursor()
    #users table
    print("Loading users...")
    users=psychometric[["user_id","employee_name"]]
    users_data=list(users.itertuples(index=False,name=None))
    insert_query="""insert into users(user_id,employee_name) values(%s,%s)"""
    cursor.executemany(insert_query,users_data)
    conn.commit()
    print(f"{cursor.rowcount} users inserted successfully!")

    #psychometric table 
    print("Loading psychometric...")
    psychometric_data = list(psychometric[["user_id", "O", "C", "E", "A", "N"]].itertuples(index=False, name=None))

    insert_query = """INSERT INTO psychometric
    (user_id, O, C, E, A, N)
    VALUES (%s,%s,%s,%s,%s,%s)
    """
    cursor.executemany(insert_query, psychometric_data)
    conn.commit()
    print(f"✓ {cursor.rowcount} psychometric records inserted.")

    #logon table
    print("Loading logon events...")
    logon_data = list(logon.itertuples(index=False, name=None))

    insert_query = """INSERT INTO logon_events
    (id, event_time, user_id, pc, activity)VALUES (%s,%s,%s,%s,%s)"""
    cursor.executemany(insert_query, logon_data)
    conn.commit()
    print(f"✓ {cursor.rowcount} logon events inserted.")

    #device table
    print("Loading device events...")

    device_data = list(device.itertuples(index=False, name=None))
    insert_query = """
    INSERT INTO device_events(id, event_time, user_id, pc, activity)VALUES (%s,%s,%s,%s,%s)"""
    cursor.executemany(insert_query, device_data)
    conn.commit()
    print(f"✓ {cursor.rowcount} device events inserted.")

    #email table
    print("Loading email events...")

    email_data = list(email.itertuples(index=False, name=None))
    insert_query = """
    INSERT INTO email_events
    (id, event_time, user_id, pc,
    recipient_to, cc, bcc, sender,
    size, attachments, content)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    cursor.executemany(insert_query, email_data)
    conn.commit()
    print(f"✓ {cursor.rowcount} email events inserted.")

    #file table
    print("Loading file events...")

    file_data = list(file.itertuples(index=False, name=None))

    insert_query = """
    INSERT INTO file_events
    (id, event_time, user_id, pc,
    filename, content)
    VALUES (%s,%s,%s,%s,%s,%s)
    """
    cursor.executemany(insert_query, file_data)
    conn.commit()
    print(f"✓ {cursor.rowcount} file events inserted.")

    #http table
    print("Loading http events...")
    http_data = list(http.itertuples(index=False, name=None))
    insert_query = """
    INSERT INTO http_events
    (id, event_time, user_id, pc,
    url, content)
    VALUES (%s,%s,%s,%s,%s,%s)
    """
    cursor.executemany(insert_query, http_data)
    conn.commit()
    print(f"✓ {cursor.rowcount} http events inserted.")
    print("===================================")
    print("All tables loaded successfully!")
except Exception as e:
    print("error:",e)
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("Database connection closed.")