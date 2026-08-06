import pandas as pd

data_path="data/raw/archive/r4.2/"
'''
email=pd.read_csv(data_path+"email.csv")
file=pd.read_csv(data_path+"file.csv")
http=pd.read_csv(data_path+"http.csv")
device=pd.read_csv(data_path+"device.csv")
psychometric=pd.read_csv(data_path+"psychometric.csv")

print("="*50)
print("datasets loaded succesfully")
print("="*50)

print(f"logon: {logon.shape}")
print(f"email: {email.shape}")
print(f"file: {file.shape}")
print(f"http: {http.shape}")
print(f"device: {device.shape}")
print(f"psychometric: {psychometric.shape}")
'''
print("Loading logon...")
logon = pd.read_csv(data_path + "logon.csv", nrows=10000)
print(f"✓ Logon loaded: {logon.shape}")

print("Loading device...")
device = pd.read_csv(data_path + "device.csv", nrows=10000)
print(f"✓ Device loaded: {device.shape}")

print("Loading email...")
email = pd.read_csv(data_path + "email.csv", nrows=10000)
print(f"✓ Email loaded: {email.shape}")

print("Loading file...")
file = pd.read_csv(data_path + "file.csv", nrows=10000)
print(f"✓ File loaded: {file.shape}")

print("Loading http...")
http = pd.read_csv(data_path + "http.csv", nrows=10000)
print(f"✓ HTTP loaded: {http.shape}")

print("Loading psychometric...")
psychometric = pd.read_csv(data_path + "psychometric.csv")
print(f"✓ Psychometric loaded: {psychometric.shape}")

print("\n" + "=" * 50)
print("All datasets loaded successfully!")