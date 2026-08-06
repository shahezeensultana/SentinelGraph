import pandas as pd
from db_connection import get_connection
import networkx as nx 
import pickle

conn=get_connection()
print("connected")

logon = pd.read_sql("SELECT * FROM logon_events",conn)
email = pd.read_sql("SELECT * FROM email_events",conn)
http = pd.read_sql("SELECT * FROM http_events",conn)
file = pd.read_sql("SELECT * FROM file_events",conn)
device = pd.read_sql("SELECT * FROM device_events",conn)

print("Tables Loaded Successfully")

conn.close()
print("connection closed")

G=nx.Graph()
print("empty graph created")

users=pd.concat(
    [logon["user_id"],email["user_id"],http["user_id"],file["user_id"],device["user_id"]]
).unique()
for user in users:
    G.add_node(user,node_type="User")
print("users added")

pcs = pd.concat([
    logon["pc"],device["pc"],email["pc"],http["pc"],file["pc"]
]).unique()

for pc in pcs:
    G.add_node(pc, node_type="PC")
print("PCs Added:", len(pcs))

#Connect Users → PCs
for _,row in logon.iterrows():
    G.add_edge(row["user_id"],row["pc"],relation="Logon")
print("logon edges added")

#Add Website Nodes
websites=http["url"].unique()
for website in websites:
    G.add_node(website,node_type="website")
print("Website Nodes Added")

#Connect Users → Websites
for _, row in http.iterrows():
    G.add_edge(row["user_id"],row["url"],relation="Visited")
print("Website Edges Added")

#Add File Nodes
files=file["filename"].unique()
for filename in files:
    G.add_node(filename,node_type="file")
print("File Nodes Added")

#Connect Users → Files
for _, row in file.iterrows():
    G.add_edge(row["user_id"],row["filename"],relation="Accessed")
print("File Edges Added")

#Add Email Nodes
receivers = email["recipient_to"].unique()
for receiver in receivers:
    G.add_node(receiver,node_type="Email")
print("Email Nodes Added")

#Connect Users → Email
for _, row in email.iterrows():
    G.add_edge(row["user_id"],row["recipient_to"],relation="Sent Email")
print("Email Edges Added")

with open("data/graph/user_graph.pkl","wb") as f:
    pickle.dump(G,f)
print("graph saved!!")

print("Nodes: ",G.number_of_nodes())
print("Edges: ",G.number_of_edges())