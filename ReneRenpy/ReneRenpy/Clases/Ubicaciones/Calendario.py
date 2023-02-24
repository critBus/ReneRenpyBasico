from ReneRenpy.Utiles.Utiles import *
from ReneRenpy.Clases.Ubicaciones.Temporalidad import *

class Calendario:
    def __init__(self):
        self.temporalidad = Temporalidad.MADRUGADA

    def getTemporalidadActual(self):
        return self.temporalidad

    def setTemporalidad(self, temporalidad):
        self.temporalidad = temporalidad
        return self

    def avanzar(self, unidades=1):
        return self
