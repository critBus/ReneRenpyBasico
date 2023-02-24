from ReneRenpy.Utiles.Utiles import *
from ReneRenpy.Clases.Interfaces.TieneContexto import TieneContexto
from ReneRenpy.Clases.Dialogos.ContextoDeDialogo import ContextoDeDialogo


class TieneAccionAlTerminar(TieneContexto):
    def __init__(self, ctx):
        self.accionAlTerminar = None
        TieneContexto.__init__(self, ctx)

    def realizarAccionAlterminar(self):  # ,ctx
        ctx = self.contexto
        if self.accionAlTerminar is not None:
            self.accionAlTerminar(ctx)

    def end(self, *etapasATerminar):
        accionAnterior = self.accionAlTerminar

        def nuevaAccion(ctx):
            if accionAnterior is not None:
                accionAnterior(ctx)
            for e in etapasATerminar:
                if e.condicionDeInicio():
                    e.completado = True

        self.accionAlTerminar = lambda ctx: nuevaAccion(ctx)
        return self

    def setAccionAlTerminar(self, accion):
        self.accionAlTerminar = accion
        return self

    def avanzarTiempo(self, unidades):
        accionAnterior = self.accionAlTerminar

        def nuevaAccion(ctx):
            if accionAnterior is not None:
                accionAnterior(ctx)
            contextoDePartida = self.contexto
            if isinstance(contextoDePartida, ContextoDeDialogo):
                contextoDePartida = self.contexto.contextoDePartida
            contextoDePartida.calendario.avanzar(unidades)

        self.accionAlTerminar = lambda ctx: nuevaAccion(ctx)

        return self

    def avan(self, unidades):
        return self.avanzarTiempo(unidades)

    def accion(self, metodo):
        accionAnterior = self.accionAlTerminar

        def nuevaAccion(ctx):
            if accionAnterior is not None:
                accionAnterior(ctx)
            metodo(ctx)

        self.accionAlTerminar = lambda ctx: nuevaAccion(ctx)
        return self
