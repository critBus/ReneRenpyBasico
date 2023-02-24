from ReneRenpy.Utiles.Utiles import *
from ReneRenpy.Clases.Progresos.Ayuda import Ayuda
from ReneRenpy.Clases.Progresos.Etapa import Etapa
from ReneRenpy.Clases.Progresos.Progreso import Progreso



class ArbolDeProgresos:
    def __init__(self):
        self.__listaDeProgresos = []

    def newProgreso(self, nombre):
        progreso = Progreso(nombre)
        self.__listaDeProgresos.append(progreso)
        return progreso

    def seHaProgresadoHasta(self, etapa):
        for p in self.__listaDeProgresos:
            if p.seHaProgresadoHasta(etapa):
                return True
        return False
