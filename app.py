import pyTigerDriver as tg

tgCl = tg.Client(server_ip="127.0.0.1",username="tigergraph",password="tigergraph",version="3.0.5")


print("======================== SIMPLE RESTPP Queries ==================================")
print(tgCl.Rest.query("Covid19","selects"))
print("======================== SIMPLE RESTPP Queries ==================================")
print(tgCl.Rest.version())

print("============================== SIMPLE LS ===========================================")
res = tgCl.Gsql.query("ls")
print(res)
print("==============================   LIST USERS   ======================================")
res = tgCl.Gsql.query("SHOW USER")
print(res)
print("==============================   Create a Secret   ======================================")
res = tgCl.Gsql.query("USE GRAPH MyGraph") # change MyGraph --> to your graph
res = tgCl.Gsql.query("create secret  mys") # Create a secret
print(res)
print("==============================   Get Secrets   ======================================")
res = tgCl.Gsql.get_secrets("MyGraph")
print(res)
# print("================================  SHOW SECRET  =======================================")
# res = gsql.query("SHOW SECRET")
# print(res)
print("=============================== Print Version =========================================")
print(tgCl.Gsql.version())
