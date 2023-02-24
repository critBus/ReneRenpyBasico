from ReneRenpy.Utiles.Utiles import *
from ReneRenpy.Clases.Visual.Escenario import Escenario
from ReneRenpy.Clases.Ubicaciones.CalendarioLineal import CalendarioLineal
class Ubicacion(Escenario):
    def __init__(self, ctx):
        Escenario.__init__(self, ctx)  # calendario
        self.__dicUbicacionesTemporales = {}  # key temporalidad o otra cosa y value UbicacionTemporal
        self.calendario = ctx.calendario

    def getUbicacionActual(self):
        return self.__dicUbicacionesTemporales[self.calendario.getTemporalidadActual()]

    def add(self, ubicacion, *keys):
        if len(keys) == 0:
            if isinstance(self.calendario, CalendarioLineal):
                keys = self.calendario.listaDeTemporalidades

        for k in keys:
            self.__dicUbicacionesTemporales[k] = ubicacion
        return self

    def setFondo(self, textoNombreImagen):
        self.getUbicacionActual().setFondo(textoNombreImagen)
        return self

    def getFondo(self):
        return self.getUbicacionActual().getFondo()
