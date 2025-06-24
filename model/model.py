import copy

import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.DiGraph()

        #ES 2
        self._percorsoOttimo = []
        self._pesoOttimo = 0

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

        archi = DAO.getArchi(store, k, self._idMap)
        for a in archi:
            if a.ordine1 in self._graph and a.ordine2 in self._graph:
                self._graph.add_edge(a.ordine1, a.ordine2, weight=a.peso) #riga cambiata

    def getGraphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def getNodi(self, store):
        return DAO.getOrdiniStore(store)

    def camminoPiuLungo(self, source):
        sourceObj = self._idMap[int(source)]
        # Limita la ricerca ai cammini che partono da sourceObj:
        subgraph = nx.dfs_tree(self._graph, sourceObj)
        return nx.dag_longest_path(subgraph)

    #ES 2
    def getBestPath(self, source):
        self._percorsoOttimo = []
        self._pesoOttimo = 0

        sourceObj = self._idMap[source]
        parziale = [sourceObj]
        parziale_edges = []

        self._ricorsione(parziale, parziale_edges)

        return self._percorsoOttimo, self._pesoOttimo

    def _ricorsione(self, parziale, parziale_edges):
        # Calcola il peso attuale e aggiorna se serve
        peso = self._getPesoPercorso(parziale_edges)
        if peso > self._pesoOttimo:
            self._pesoOttimo = peso
            self._percorsoOttimo = copy.deepcopy(parziale_edges)
            print("---------------")
            print("Nuovo percorso ottimo trovato:", [a[2] for a in parziale_edges])

        ultimo_nodo = parziale[-1]
        nodi_da_esplorare = list(self._graph.neighbors(ultimo_nodo))

        for n in nodi_da_esplorare:
            if n not in parziale:
                peso_arco = self._graph[ultimo_nodo][n]["weight"]
                nuovo_arco = (ultimo_nodo, n, peso_arco)

                parziale_edges.append(nuovo_arco)

                if self._ammissibilitaArco(parziale_edges):
                    parziale.append(n)
                    self._ricorsione(parziale, parziale_edges)
                    parziale.pop()

                parziale_edges.pop()

    def _ammissibilitaArco(self, parziale_edges):
        if len(parziale_edges) < 2:
            return True
        result = parziale_edges[-2][2] > parziale_edges[-1][2]
        if not result:
            print('----------------')
            print(f"Bloccato: {parziale_edges[-2][2]} NON > {parziale_edges[-1][2]}")
        return result

    def _getPesoPercorso(self, parziale_edges):
        pesoTot = 0
        for a in parziale_edges:
            pesoTot += a[2]
        return pesoTot


 # def getBestPath(self, startStr):
 #        self._bestPath = []
 #        self._bestScore = 0
 #
 #        start = self._idMap[int(startStr)]
 #
 #        parziale = [start]
 #
 #        vicini = self._graph.neighbors(start)
 #        for v in vicini:
 #            parziale.append(v)
 #            self._ricorsione(parziale)
 #            parziale.pop()
 #
 #        return self._bestPath, self._bestScore

 #  def _ricorsione(self, parziale):
 #        if self.getScore(parziale) > self._bestScore:
 #            self._bestScore = self.getScore(parziale)
 #            self._bestPath = copy.deepcopy(parziale)
 #
 #        for v in self._graph.neighbors(parziale[-1]):
 #            if (v not in parziale and #check if not in parziale
 #                    self._graph[parziale[-2]][parziale[-1]]["weight"] >
 #                    self._graph[parziale[-1]][v]["weight"]): #check if peso nuovo arco è minore del precedente
 #                parziale.append(v)
 #                self._ricorsione(parziale)
 #                parziale.pop()

# def getScore(self, listOfNodes):
#     tot = 0
#     for i in range(len(listOfNodes) - 1):
#         tot += self._graph[listOfNodes[i]][listOfNodes[i + 1]]["weight"]
#
#     return tot







