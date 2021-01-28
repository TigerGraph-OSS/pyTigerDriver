import pyTigerDriver as tg

tgCl = tg.Client(server_ip="127.0.0.1",username="tigergraph",password="tigergraph",version="3.0.5")
print("======================== SIMPLE RESTPP Queries ==================================")
print(tgCl.Rest.get("/echo"))
print("============================== SIMPLE LS ===========================================")
print(tgCl.Gsql.execute("ls"))

