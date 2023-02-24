from ReneRenpy.Utiles.Utiles import *
from ReneRenpy.Clases.Interfaces.TieneCondicionDeVisibilidad import TieneCondicionDeVisibilidad
from ReneRenpy.Clases.Interfaces.TieneAccionAlTerminar import TieneAccionAlTerminar
class DisparadorDeEscenario(TieneCondicionDeVisibilidad, TieneAccionAlTerminar):
    def __init__(self, escenario, ctx):
        if not esFuncion(escenario):
            anterior = escenario
            escenario = lambda ctx: anterior
        self.__metodoGetEscenario = escenario

        TieneCondicionDeVisibilidad.__init__(self, ctx)
        TieneAccionAlTerminar.__init__(self, ctx)

    def getEscenario(self):
        return self.__metodoGetEscenario(self.contexto)

