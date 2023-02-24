from ReneRenpy.Utiles.Utiles import *
from ReneRenpy.Clases.Progresos.Ayuda import Ayuda
from ReneRenpy.Clases.Progresos.Etapa import Etapa
class Progreso:
    def __init__(self, nombre):  # arbolDeProgresos
        self.nombre = nombre
        self.__listaDeEtapas = []
        self.__indiceEtapaActual = -1
        # self.__arbolDeProgresos=arbolDeProgresos

    def getEtapaActual(self):
        self.__actualizarIndiceActual()
        if self.__indiceEtapaActual > -1:
            etapaActual = self.__listaDeEtapas[self.__indiceEtapaActual]
            return etapaActual
        return None

    def __actualizarIndiceActual(self):
        leng = len(self.__listaDeEtapas)
        if leng > 0:  # and self.__indiceEtapaActual>-1 and self.__indiceEtapaActual<leng
            indiceAnterior = self.__indiceEtapaActual
            if indiceAnterior == -1:
                indiceAnterior = 0

            for i, e in enumerate(self.__listaDeEtapas[indiceAnterior:]):  # , indiceAnterior
                if e.completado:
                    self.__indiceEtapaActual = i  # -1
        return self.__indiceEtapaActual

    def addEtapa(self, etapa, condicionDeInicio=None):
        if esString(etapa):
            etapa = Etapa(nombre=etapa, condicionDeInicio=condicionDeInicio)
        leng = len(self.__listaDeEtapas)
        if leng > 0:
            etapaAnterior = self.__listaDeEtapas[-1]
            condicionDeInicioActual = etapa.condicionDeInicio

            def nuevaCondicion():
                # print(self.nombre)
                # print(self.completado)
                # print(self.condicionDeInicio())
                # print("etapaAnterior=",etapaAnterior.nombre)
                # print("etapaAnterior=",etapaAnterior.completado)
                # print("etapaAnterior=",etapaAnterior.condicionDeInicio())
                return condicionDeInicioActual() and etapaAnterior.completado

            etapa.condicionDeInicio = nuevaCondicion
            # etapa.condicionDeInicio=lambda : condicionDeInicioActual() and etapaAnterior.completado

        self.__listaDeEtapas.append(etapa)
        return etapa

    def getEtapa(self, nombre):
        for e in self.__listaDeEtapas:
            if e.nombre == nombre:
                return e
        return None

    def getEtapaEIndice(self, nombre):
        for i, e in enumerate(self.__listaDeEtapas):
            if e.nombre == nombre:
                return i, e
        return None

    def seHaProgresadoHasta(self, etapa):
        indice, etapa = self.getEtapaEIndice(etapa.nombre)
        if etapa is not None:
            indiceActual = self.__actualizarIndiceActual()
            return indice <= indiceActual  # indiceActual<=indice
        return False
