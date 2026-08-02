import pandas as pd

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

#converting dates
logon["event_time"]=pd.to_datetime(logon["event_time"])
device["event_time"]=pd.to_datetime(device["event_time"])
email["event_time"]=pd.to_datetime(email["event_time"])
file["event_time"]=pd.to_datetime(file["event_time"])
http["event_time"]=pd.to_datetime(http["event_time"])

print(logon.head())
print(email.head())
print(file.head())
print(logon.dtypes)

print(email.dtypes)