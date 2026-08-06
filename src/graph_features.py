import pickle
import networkx as nx
import pandas as pd
from db_connection import get_connection

with open("data/graph/user_graph.pkl","rb") as f:
    G=pickle.load(f)

degree=nx.degree_centrality(G)
pagerank=nx.pagerank(G)
betweeness=nx.betweenness_centrality(G,k=200,seed=42)
closeness=nx.closeness_centrality(G)
print("all calculated successfully")

graph_features=pd.DataFrame({
    "user_id": list(degree.keys()),
    "degree": list(degree.values()),
    "pagerank":list(pagerank.values()),
    "betweeness":list(betweeness.values()),
    "closeness": list(closeness.values())
})

conn=get_connection()
users=pd.read_sql("select user_id from users",conn)
conn.close()

graph_features=graph_features.merge(users, on="user_id",how="inner")

print(graph_features.head())
print(graph_features.shape)
print(graph_features.info())

graph_features.to_csv("data/processed/graph_features.csv",index=False)
print("Graph Features Saved Successfully!")