import pyTigerDriver as tg

# Version v1.0.11
# my used sample kit
# secret : junq2fhuji2hq9r0mg92folp82l33ufl
# curl -X GET 'https://ttl.i.tgcloud.io:9000/requesttoken?secret=junq2fhuji2hq9r0mg92folp82l33ufl&lifetime=1000000'
# {"code":"REST-0000","expiration":1613435591,"error":false,"message":"Generate new token successfully.","token":"ptkqg4c8tdncjvspbtkt2crird81dron"}


#
# def get(self, path, headers=None, resKey="results", skipCheck=False, params=None):
# def post(self, path, headers=None, data=None, resKey="results", skipCheck=False, params=None):
# def delete(self, path):
# def execute(self, query, local=False, options=None):

# All the params are listed for info only!
# you need : server_ip , user , pass , token , graph , and protocol ( by default local = False )

# tgcloud.io Case : /gsqlserver/gsql/
# tgCl = tg.Client(server_ip="ttl.i.tgcloud.io",gsPort="14240", restPort="9000"
#                  , username="tigergraph", password="tigergraph"
#                  , version="3.0.5",protocol="https"
#                  , graph="MyGraph",token="ptkqg4c8tdncjvspbtkt2crird81dron")

# Docker Case : /gsqlserver/gsql/
tgCl = tg.Client(server_ip="127.0.0.1",gsPort="14240", restPort="9000"
                 , username="tigergraph", password="tigergraph",local=False
                 , version="3.0.5",protocol="http"
                 , graph="ioT")

# Local installation  : /gsql/
# tgCl = tg.Client(server_ip="127.0.0.1",gsPort="14240", restPort="9000"
#                  , username="tigergraph", password="tigergraph",local=True
#                  , version="3.0.5",protocol="http"
#                  , graph="ioT")


def getUDT(endpoint,param=None):
    """
    GSQL Schema :  get(URL + "/gsqlserver/gsql/udtlist?graph=" + graphname, authMode="pwd")
    :param endpoint:
    :param param:
    :return:
    """
    res = tgCl.Gsql.get(endpoint,param)
    return res


def RunQuery(query_name,graph,params=None):
    """
    Run an installed query
    :param query_name:
    :param graph:
    :param params:
    :param timeout:
    :param sizeLimit:
    :return:
    """
    res = tgCl.Rest.get("/query/{0}/{1}".format(graph,query_name),parameters=params,resKey="results")
    return res




print("################ /GET UDT Listing : GSQL 14240 ##################")
endpoint = "udtlist"  # endpoint after /gsql/ or /gsqlserver/gsql/
param = {"graph":"MyGraph"} # 1 param
res = getUDT(endpoint,param)
print(res)

print("################ /GET echo :  RestPP 9000  ##################")
res = tgCl.Rest.get("/echo")
print(res)

print("################ /GET Catalog  ##################")
res = tgCl.Rest.get("/echo")
print(res)

print("################ Run Query #######################")
res = RunQuery("GetLocations","ioT")
print(res)


# print("################ GSQL  ##################")
# res = tgCl.Gsql.execute("ls")
# print(res)

print("################ Change Graph  ##################")

tgCl.Gsql.graph = "ioT"


res = []
res.append("Using Graph with GSQL")
res = tgCl.Gsql.execute("use GRAPH ioT")
res += tgCl.Gsql.execute("show loading  status all")
res.append("Using Global with GSQL")
res += tgCl.Gsql.execute("use Global")
res += tgCl.Gsql.execute("show loading  status all")
res.append("Changing back to  Graph with variable cookie")
tgCl.Gsql.graph = "ioT"
# res += tgCl.Gsql.execute("use GRAPH ioT")
res += tgCl.Gsql.execute("show loading  status all")
print("\n".join(res))



