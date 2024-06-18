import copy

import networkx as nx

from database.DAO import DAO
from geopy.distance import geodesic


class Model:
    def __init__(self):
        self._cities = DAO.getAllCities()
        self._grafo = nx.Graph()
        self._idMap = {}


    def crea_grafo(self, citta):
        self._nodes = DAO.getAllNodes(citta)
        for b in self._nodes:
            self._idMap[b.business_id] = b

        self._grafo.add_nodes_from(self._nodes)
        archi = DAO.getAllEdges(citta, self._idMap)
        for a in archi:
            coordB1 = a[2]
            coordB2 = a[3]
            distanza = geodesic(coordB1, coordB2).km
            self._grafo.add_edge(a[0], a[1], weight=distanza)

    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    def locale_distante(self, locale):
        vicini = self._grafo.neighbors(locale)
        vicini_distanza = []
        for v in vicini:
            distanza = self._grafo[locale][v]["weight"]
            vicini_distanza.append((v, distanza))
        vicini_distanza.sort(key=lambda x: x[1], reverse=True)
        return vicini_distanza[0]



    def getCammino(self, partenza, arrivo, soglia):
        self._bestCammino = []
        self._bestDistanza = 0
        vicini_partenza = self._grafo.neighbors(partenza)
        for v in vicini_partenza:
            self._ricorsione(v, arrivo, [], soglia)
        return self._bestDistanza, self._bestCammino

    def _ricorsione(self, nodo, arrivo, parziale, soglia):
        if len(parziale) > 0 and parziale[-1][1] == arrivo:
            distanza_parziale = self.calcolaDistanza(parziale)
            if len(parziale) > len(self._bestCammino):
                self._bestDistanza = distanza_parziale
                self._bestCammino = copy.deepcopy(parziale)
        vicini = self._grafo.neighbors(nodo)
        for v in vicini:
            if v != arrivo and self.filtroNodi(v, parziale):
                if v.stars >= soglia :
                    distanza = self._grafo[nodo][v]["weight"]
                    parziale.append((nodo, v, distanza))
                    self._ricorsione(v, arrivo, parziale, soglia)
                    parziale.pop()
            elif v == arrivo and self.filtroNodi(v, parziale):
                distanza = self._grafo[nodo][v]["weight"]
                parziale.append((nodo, v, distanza))
                self._ricorsione(v, arrivo, parziale, soglia)
                parziale.pop()



    def calcolaDistanza(self, parziale):
        totD = 0
        for a in parziale:
            totD += a[2]
        return totD

    def filtroNodi(self, nodo, parziale):
        for a in parziale:
            if a[0] == nodo or a[1] == nodo:
                return False
        return True



