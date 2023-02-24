from ReneRenpy.Utiles.Utiles import *
from ReneRenpy.Clases.Interfaces.TieneContexto import TieneContexto
from ReneRenpy.Clases.Visual.Escenario import Escenario

class ElementoDeTransicion(TieneContexto):
    def __init__(self, ctx):
        TieneContexto.__init__(self, ctx)

    def setSiguienteEscenario(self, siguiente):
        if isinstance(siguiente, Escenario):
            anterior = siguiente
            siguiente = lambda ctx: anterior
        self.__getSiguienteEscenario = siguiente
        return self

    def getSiguienteEscenario(self):
        if self.__getSiguienteEscenario is None:
            return None
        return self.__getSiguienteEscenario(self.contexto)
