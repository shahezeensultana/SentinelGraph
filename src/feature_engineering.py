import pandas as pd
from db_connection import get_connection

conn=get_connection()
print("Connected successfully")

users=pd.read_sql("select * from users",conn)
device=pd.read_sql("select * from device_events",conn)
psychometric=pd.read_sql("select * from psychometric",conn)
logon=pd.read_sql("select * from logon_events",conn)
email=pd.read_sql("select * from email_events",conn)
file=pd.read_sql("select * from file_events",conn)
http=pd.read_sql("select * from http_events",conn)

print("tables loaded successfully")

print("Users:", users.shape)
print("Psychometric:", psychometric.shape)
print("Logon:", logon.shape)
print("Device:", device.shape)
print("Email:", email.shape)
print("File:", file.shape)
print("HTTP:", http.shape)

conn.close()
print("\nDatabase connection closed.")

login_count=(logon.groupby("user_id").size().reset_index(name="login_count"))
print(login_count.head())

#After-Hours Login Feature
after_hours=logon[
    (logon["event_time"].dt.hour<8)|
    (logon["event_time"].dt.hour>=18)
]
after_hours_login=(after_hours.groupby("user_id").size().reset_index(name="after_hours_login"))
print(after_hours_login.head())

#user activity
usb_events=(device.groupby("user_id").size().reset_index(name="usb_events"))
print(usb_events.head())

#Email Count
email_count=(email.groupby("user_id").size().reset_index(name="email_count"))
print(email_count.head())

#Attachment Count
attachment_count=(email.groupby("user_id")["attachments"].sum().reset_index(name="attachment_count"))
print(attachment_count.head())

#File Access Count
file_count = (file.groupby("user_id").size().reset_index(name="file_access_count"))
print(file_count.head())

#website_count
website_count = (http.groupby("user_id").size().reset_index(name="website_count"))
print(website_count.head())

features=users.copy()

features=features.merge(login_count,on="user_id",how="left")
features=features.merge(usb_events,on="user_id",how="left")
features=features.merge(email_count,on="user_id",how="left")
features=features.merge(attachment_count,on="user_id",how="left")
features=features.merge(file_count,on="user_id",how="left")
features=features.merge(website_count,on="user_id",how="left")
features=features.merge(psychometric,on="user_id",how="left")
features=features.merge(after_hours_login,on="user_id",how="left")

features.fillna(0, inplace=True)

print(features.head())
print(features.shape)
print(features.info())
features.to_csv("data/processed/features.csv",index=False)
print("Features saved successfully!")