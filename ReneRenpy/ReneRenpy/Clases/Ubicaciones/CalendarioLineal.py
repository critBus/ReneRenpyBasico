from ReneRenpy.Utiles.Utiles import *
from ReneRenpy.Clases.Ubicaciones.Temporalidad import *
from ReneRenpy.Clases.Ubicaciones.Calendario import Calendario
class CalendarioLineal(Calendario):
    def __init__(self, listaDeTemporalidades=None):
        Calendario.__init__(self)
        if listaDeTemporalidades is None:
            listaDeTemporalidades = [Temporalidad.MADRUGADA
                , Temporalidad.AMANECER
                , Temporalidad.MANANA
                , Temporalidad.MEDIA_MANANA
                , Temporalidad.MEDIODIA
                , Temporalidad.TARDE
                , Temporalidad.ATARDECER
                , Temporalidad.NOCHE
                , Temporalidad.MEDIA_NOCHE]
        self.listaDeTemporalidades = listaDeTemporalidades
        self.indiceTemporalidadActual = 0

    def setTemporalidad(self, temporalidad):
        for i, e in enumerate(self.listaDeTemporalidades):
            if e == temporalidad:
                self.indiceTemporalidadActual = i
                self.temporalidad = temporalidad
                break
        return self

    def avanzar(self, unidades=1):
        if esInt(unidades):
            self.indiceTemporalidadActual = (self.indiceTemporalidadActual + 1) % len(self.listaDeTemporalidades)
            self.temporalidad = self.listaDeTemporalidades[self.indiceTemporalidadActual]
        elif isinstance(unidades, Temporalidad):
            self.setTemporalidad(temporalidad=unidades)
        return self
