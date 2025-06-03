import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.DiGraph()

    #ES 1
    def getIdStores(self):
        return DAO.getStores()

    def buildGraph(self, store, k):
        ordini = DAO.getOrdiniStore(store)
        self._idMap = {}
        for o in ordini:
            self._idMap[o.order_id] = o

        self._graph.clear()
        self._graph.add_nodes_from(ordini)






