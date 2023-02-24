from ReneRenpy.Utiles.Utiles import *
from ReneRenpy.Clases.Ubicaciones.Disparadores.DisparadorDeEscenario import DisparadorDeEscenario
class DisparadorBitMap(DisparadorDeEscenario):
    def __init__(self, escenario, listaDeCoordenadas, ctx):
        DisparadorDeEscenario.__init__(self, escenario, ctx)

        self.listaDeCoordenadas = listaDeCoordenadas
