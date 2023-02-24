from ReneRenpy.Utiles.Utiles import *
from ReneRenpy.Clases.Visual.Fondos.TieneFondo import TieneFondo
from ReneRenpy.Clases.Visual.CreadorDeEscenario import CreadorDeEscenario
class Escenario(TieneFondo, CreadorDeEscenario):
    def __init__(self, ctx):
        TieneFondo.__init__(self, ctx)
