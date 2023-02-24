from ReneRenpy.Utiles.Utiles import *
from ReneRenpy.Clases.Interfaces.TieneContexto import TieneContexto
from ReneRenpy.Clases.Progresos.Etapa import Etapa
class TieneCondicionDeVisibilidad(TieneContexto):
    def __init__(self, ctx):
        self.condicionDeVisibilidad = lambda ctx: True
        TieneContexto.__init__(self, ctx)

    def esVisible(self):
        return self.condicionDeVisibilidad(self.contexto)

    def _if(self, *a):

        def nuevaCondicion(ctx):
            for e in a:
                if isinstance(e, Etapa):
                    if not e.condicionDeInicio():
                        return False
                elif esFuncion(e):
                    if not e(ctx):
                        return False
            return True

        condicionActual = self.condicionDeVisibilidad
        self.condicionDeVisibilidad = lambda ctx: condicionActual(ctx) and nuevaCondicion(ctx)
        return self

    def _ifnot(self, *a):

        def nuevaCondicion(ctx):
            for e in a:
                if isinstance(e, Etapa):
                    if e.condicionDeInicio():
                        return False
                elif esFuncion(e):
                    if e(ctx):
                        return False
            return True

        condicionActual = self.condicionDeVisibilidad
        self.condicionDeVisibilidad = lambda ctx: condicionActual(ctx) and nuevaCondicion(ctx)
        return self

    def setCondicionDeVisbilidad(self, condicion):
        self.condicionDeVisibilidad = condicion
        return self
